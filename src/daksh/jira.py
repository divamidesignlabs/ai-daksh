import typer
import os
from dotenv import load_dotenv
from jira import JIRA
from fuzzywuzzy import process
from torch_snippets import AD

os.environ["AD_MAX_ITEMS"] = "1000"  # Set max items for AD display

jira_cli = typer.Typer(help="Jira CLI interface", no_args_is_help=True)

create_token_help = """
Go to 
https://id.atlassian.com/manage-profile/security/api-tokens
and create a new API token.
Copy the token and set it in your environment as JIRA_TOKEN.
Set your email as JIRA_EMAIL.

For example you can save both of them in your .zshrc file:
```bash
export JIRA_EMAIL="yeshwanth@divami.com"
export JIRA_TOKEN="your_api_token_here"
```
and then run `source ~/.zshrc` to apply the changes.
"""

USERS = [
    "Yeshwanth Reddy Yerraguntla",
    "Manisha Gundupaneedi",
    "Ganesh Danuri",
]


class JiraClient:
    """JIRA API client for managing issues"""

    def __init__(self):
        """Initialize JIRA client with configuration from environment"""
        load_dotenv()

        self.server = os.getenv("JIRA_SERVER", "https://divami.atlassian.net")
        self.email = os.getenv("JIRA_EMAIL")
        self.token = os.getenv("JIRA_TOKEN")
        self.epic_link_field = "customfield_10008"  # Default Epic Link field ID

        if not self.email or not self.token:
            typer.echo(
                f"❌ Error: JIRA_EMAIL and JIRA_TOKEN environment variables must be set,\n{create_token_help}",
                err=True,
            )
            raise typer.Exit(1)

        # Initialize JIRA client with basic auth
        self.jira = JIRA(server=self.server, basic_auth=(self.email, self.token))

    def handle_request_error(self, e):
        """Handle and display JIRA API request errors"""
        typer.echo(f"❌ Error: {e}", err=True)
        if hasattr(e, "response") and e.response is not None:
            try:
                error_details = e.response.json()
                if "errors" in error_details:
                    for field, error_msg in error_details["errors"].items():
                        typer.echo(f"  - {field}: {error_msg}", err=True)
                if "errorMessages" in error_details:
                    for error_msg in error_details["errorMessages"]:
                        typer.echo(f"  - {error_msg}", err=True)
            except Exception:
                typer.echo(f"  Response: {e.response.text}", err=True)
        raise typer.Exit(1)

    def create_issue(
        self,
        project,
        issue_type,
        summary,
        description="",
        assignee=None,
        labels=None,
        priority=None,
        parent=None,
    ):
        """Create a new JIRA issue"""
        # Build issue data for JIRA library
        issue_dict = {
            "project": {"key": project},
            "summary": summary,
            "description": description or f"{issue_type.upper()}: Created via CLI",
            "issuetype": {"name": issue_type},
        }

        if labels:
            label_list = [label.strip() for label in labels.split(",")]
            issue_dict["labels"] = label_list

        if priority:
            issue_dict["priority"] = {"name": priority}

        if parent:
            issue_dict["parent"] = {"key": parent}

        try:
            typer.echo(f"Creating {issue_type} in project {project}: {summary}")

            # Use JIRA library's create_issue method
            new_issue = self.jira.create_issue(fields=issue_dict)

            issue_key = new_issue.key
            issue_url = f"{self.server}/browse/{issue_key}"

            typer.echo(f"✅ Created {issue_type}: {issue_key}")
            typer.echo(f"🔗 URL: {issue_url}")

            if assignee:
                assign(issue_key, assignee)

            return new_issue

        except Exception as e:
            self.handle_request_error(e)


jira_client = JiraClient()


@jira_cli.command()
def create(
    project: str = typer.Option(..., "--project", "-p", help="Project key"),
    issue_type: str = typer.Option(..., "--type", "-t", help="Issue type"),
    summary: str = typer.Option(..., "--summary", "-s", help="Issue summary"),
    description: str = typer.Option(
        "", "--description", "-d", help="Issue description"
    ),
    assignee: str = typer.Option(None, "--assignee", "-a", help="Assign to user"),
    labels: str = typer.Option(None, "--labels", help="Comma-separated labels"),
    priority: str = typer.Option(None, "--priority", help="Issue priority"),
    parent: str = typer.Option(
        None, "--parent", help="Parent issue key (for sub-tasks)"
    ),
):
    """Create a new JIRA issue"""
    try:
        return jira_client.create_issue(
            project=project,
            issue_type=issue_type,
            summary=summary,
            description=description,
            assignee=assignee,
            labels=labels,
            priority=priority,
            parent=parent,
        )
    except Exception as e:
        typer.echo(f"❌ Unexpected error: {e}", err=True)
        raise typer.Exit(1)


@jira_cli.command()
def view(issue_key: str):
    issue = jira_client.jira.issue(issue_key)
    typer.echo(f"Viewing issue {issue_key}: {issue.fields.summary}")


@jira_cli.command()
def assign(issue_key: str, user: str):
    """Assign an issue to a user"""
    issue = jira_client.jira.issue(issue_key)
    if user not in USERS:
        user = process.extractOne(user, USERS)[0]  # Fuzzy match to find closest user
        typer.echo(f"Using closest match for user: {user}")
    jira_client.jira.assign_issue(issue, user)
    typer.echo(f"Assigning issue {issue_key} to {user}")


@jira_cli.command()
def list(
    jql: str = typer.Option(None, "--jql", help="JQL query"),
):
    jql = jql or "assignee = currentUser() order by priority desc"
    issues = [
        {
            "_key": i.key,
            "_summary": i.fields.summary,
            "_assignee": i.fields.assignee.displayName if i.fields.assignee else None,
            "_status": i.fields.status.name,
            "_parent": i.fields.parent.key if hasattr(i.fields, "parent") else None,
        }
        for i in jira_client.jira.search_issues(
            jql_str=jql, fields="key,summary,assignee,status,parent"
        )
    ]
    print(AD(issues))
