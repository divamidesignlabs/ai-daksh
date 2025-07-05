---
description:
globs:
alwaysApply: false
---
# Rule: Generating Project Epics Document

## Goal

To guide an AI assistant in creating a detailed Project Epics Document in INI format, based on an initial user prompt and existing documentation. The epics document should be structured, actionable, and suitable for breaking down complex features into manageable user stories with clear dependencies and outputs.

## Process

1.  **Receive Initial Prompt:** The user provides a brief description or request for new project epics or functionality.
2.  **Analyze Existing Documentation:** Review the `docs/` folder structure and existing documentation to understand the project context, requirements, and architecture.
3.  **Ask Clarifying Questions:** Before writing the epics document, the AI *must* ask clarifying questions to gather sufficient detail. The goal is to understand the scope, priorities, and relationships between epics. Make sure to provide options in letter/number lists so I can respond easily with my selections.
4.  **Generate Epics Document:** Based on the initial prompt, documentation analysis, and user's answers to clarifying questions, generate an epics document using the structure outlined below.
5.  **Save Epics Document:** Save the generated document as `epics.ini` inside the `/tasks` directory at `<project-root>/tasks/epics.ini`.

## Thinking and Guiding Principles

Before generating the epics document, consider these principles:

*   **Hierarchical Structure:** Epics should be broken down into logical user stories that build upon each other
*   **Clear Dependencies:** Each story should explicitly declare its dependencies on other stories
*   **Traceability:** Stories should reference relevant documentation and specify expected outputs
*   **Testability:** Each story should have corresponding test files for validation
*   **Incremental Value:** Stories should deliver incremental business value and be implementable independently where possible
*   **Documentation-First:** All outputs should align with existing documentation structure and contribute to project knowledge base

## Clarifying Questions (Examples)

The AI should adapt its questions based on the prompt and existing documentation, but here are some common areas to explore:

*   **Project Scope:** "What is the main area of functionality you want to focus on? (e.g., core parsing, integrations, user experience, deployment)"
*   **Priority Level:** "What is the priority level for these epics? a) High (foundational/critical path) b) Medium (important but not blocking) c) Low (nice-to-have)"
*   **Target Audience:** "Who are the primary users of these features? a) Developers b) Project managers c) End users d) System administrators"
*   **Dependencies:** "Are there any specific existing epics or stories that must be completed first?"
*   **Integration Points:** "Which external systems or APIs need to be integrated? a) Jira b) GitHub c) CI/CD tools d) Other"
*   **Documentation Requirements:** "What types of documentation should be generated when an epic is completed? a) Technical specs b) User guides c) API reference d) All of the above"
*   **Success Criteria:** "How will success be measured for these epics? a) Feature completeness b) Performance metrics c) User adoption d) Code quality e) Something else"
*   **Timeline Constraints:** "Are there any specific deadlines or milestone requirements?"
*   **Technical Constraints:** "Are there any technical limitations or architectural decisions that should influence the epic design?"

## Epics Document Structure

The generated epics document should follow this INI format structure:

```ini
[epic-name-1]
description = Brief description of the epic

[epic-name-1.story-name-1]
story_id = epic.story (e.g., 1.1, 1.2, etc.)
description = Detailed description of what this story accomplishes
goals = 
    as a developer I need to goal-1 short description
    as a maintainer I should be able to goal-2 short description
    ...
acceptance_criteria = 
    all tests generated for the story are passed
    the single config should be able to ...
    criteria-3 short description
    ...
dependent_stories = 
    ${epic-name-1.story-name-1.story_id}
    ${epic-name-2.story-name-2.story_id}
    ...
relevant_docs = 
    path/to/doc1
    path/to/doc2
    ...
outputs = 
    path/to/file1.py
    path/to/another/file2.py
    tests/test_story_name.py
    ...
```

### Key Structure Rules:

*   **Epic Sections:** Use `[epic-name]` for epic headers with a description
*   **Story Sections:** Use `[epic-name.story-name]` for individual stories
*   **Story IDs:** Use numeric format `epic.story` (e.g., 1.1, 1.2, 2.1)
*   **Multi-line Values:** Use indented continuation lines for lists
*   **Dependencies:** Reference other stories using `${epic-name.story-name.story_id}` format
*   **File Paths:** Use relative paths from project root
*   **Test Files:** Always include corresponding test files in outputs

## Documentation Analysis

Before generating epics, analyze the existing documentation structure:

*   **Architecture Docs:** `docs/architecture/` - for technical dependencies
*   **Business Specs:** `docs/specifications/business/` - for business context
*   **Technical Specs:** `docs/specifications/technical/` - for implementation details
*   **Functional Requirements:** `docs/specifications/functional/` - for feature requirements
*   **Implementation Guides:** `docs/implementation/` - for development context
*   **Executive Materials:** `docs/executive/` - for strategic alignment

## Target Audience

Assume the primary users of the epics document are:

*   **Development Teams:** For implementation planning and task breakdown
*   **Project Managers:** For tracking progress and dependencies
*   **Technical Architects:** For understanding system integration points
*   **Quality Assurance:** For test planning and validation

## Output Requirements

*   **Format:** INI configuration file (`.ini`)
*   **Location:** `/tasks/`
*   **Filename:** `epics.ini`
*   **Encoding:** UTF-8
*   **Line Endings:** Unix-style (LF)

## Final Instructions

**CRITICAL - DO NOT DEVIATE FROM THESE INSTRUCTIONS:**

1. **DO NOT** start implementing the epics document immediately
2. **ALWAYS** ask clarifying questions before generating the document
3. **MUST** analyze existing documentation in the `docs/` folder first
4. **MUST** follow the exact INI format structure specified above
5. **MUST** include story_id, description, goals, acceptance_criteria, dependent_stories, relevant_docs, and outputs for each story
6. **MUST** ensure all file paths are relative to project root
7. **MUST** include test files for every story in the outputs section
8. **MUST** validate that dependencies reference valid story IDs
9. **DO NOT** generate implementation code - only the epics document
10. **DO NOT** modify existing files - only create the new epics.ini file

**WARNING:** Deviating from these instructions or the specified format will result in an unusable epics document. Stay focused on the task of generating a well-structured INI file that follows the exact format requirements.
