

# Jira CLI Specification

## 📦 Command Structure

```bash
daksh jira [COMMAND] [ARGS] [FLAGS]
```

---

## 🔧 Primary Commands

### Ticket Operations
- ✅ `daksh jira create` – Create a new issue  
  - Flags: `--project`, `--type`, `--summary`, `--description`, `--assignee`, `--labels`, `--priority`, `--parent`
- `daksh jira view ISSUE_KEY` – View issue details
- `daksh jira edit ISSUE_KEY` – Edit issue fields  
  - Flags: same as `create`
- `daksh jira comment ISSUE_KEY` – Add a comment  
  - Flags: `--text`, `--visibility`
- `daksh jira assign ISSUE_KEY USER` – Assign issue
- `daksh jira transition ISSUE_KEY` – Change status  
  - Flags: `--to`, `--comment`

### Querying & Listing
- ✅ `daksh jira list` – List issues (default: assigned to me)  
  - Flags: `--jql`, `--project`, `--status`, `--assignee`, `--limit`, `--open-only`, `--mine`
- `daksh jira search "JQL_QUERY"` – Raw JQL query
- `daksh jira backlog` – View current backlog
- `daksh jira board` – View board issues
- `daksh jira sprint` – View active sprint  
  - Flags: `--board`, `--include-done`

### Project & Config
- `daksh jira projects` – List available projects
- `daksh jira setup` – Configure server, token, defaults
- `daksh jira me` – Show current user info
- `daksh jira config` – Show/edit CLI config

---

## 🛠️ Optional Features

- `daksh jira open ISSUE_KEY` – Open in browser
- `daksh jira watch ISSUE_KEY` – Watch/unwatch issue
- `daksh jira clone ISSUE_KEY` – Clone issue
- `daksh jira link A B` – Link issue A to B
- `daksh jira attach ISSUE_KEY FILE` – Upload attachment
- `daksh jira log ISSUE_KEY` – Log work
  - Flags: `--time`, `--comment`, `--date`

---

## ⚡ Flag Shorthands

- `-p` → `--project`
- `-t` → `--type`
- `-s` → `--summary`
- `-d` → `--description`
- `-a` → `--assignee`