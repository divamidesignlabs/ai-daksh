# 🛠️ Technical Specifications: DAKSH

---

## 1. Overview

This document describes how DAKSH works under the hood — from reading Markdown-based indexes to managing traceability, validations, and external integrations (like Jira). It serves as a reference for contributors and integrators working with or extending DAKSH.

---

## 2. Core Architecture

-DAKSH is designed to parse structured Markdown documents and expose a consistent internal representation of project artifacts. Its architecture revolves around a clear generation and validation pipeline:

- **Input**: LLM-generated `project-epics.ini` based on upstream project specs and docs. These are verified by humans and serve as the technical single source of truth.
- **Expansion**: Each story in the project file is expanded into a standalone `project-trd.md` (one per story), and then into a `trd-task-list.md` (one per TRD).
- **Linkage**: Each TRD and task list is linked back to its parent story as well as the corresponding documentation (in the form of front-matter), ensuring traceability.
- **Parser**: Extracts hierarchical relationships from `project-epics.ini` (INI format) and associated Markdown: specs → epics/stories → TRDs → task lists
- **Validators**: Ensure references are correct, paths exist, and artifact linkages are complete
- **Output Consumers**:
  - CLI tools for validation, diff inspection, and sync
  - Jira integration for automatic issue creation and closure
  - Optional YAML/JSON or dashboard generation

---

## 3. Components

### 3.1 Artifact Types

- `project-epics.ini`: Contains epics and story breakdowns in `.ini` format, references source specs
- `project-trd.md`: One per story; technical requirements definition
- `trd-task-list.md`: Task breakdown per TRD; includes Jira-linked checklist
- All files live in Markdown and follow naming conventions for reliable mapping

### 3.2 Story-to-TRD Mapping

- There must be a 1:1 mapping between stories and TRDs
- Each TRD file declares its upstream story using frontmatter:
  ```yaml
  story_id: STORY-123
  ```
- The index or CLI must be able to trace stories ↔ TRDs explicitly

### 3.3 Copilot-Driven Task Completion

- Each `trd-task-list.md` contains a task list using `- [ ]` checkbox format
- When Copilot completes a task, it marks it as `- [x]`
- These completions are **not** automatically reflected in Jira
- Instead, task status updates go through a **code approval layer** (see below)
- Each task is assumed to trigger Copilot-generated code artifacts, which must be verified

### 3.3.1 Code Approval Flow

- When a task is marked as `- [x]`, it is treated as **code-complete**
- This triggers an internal approval process (via PR, checklist, or human review)
- Only after explicit approval is the corresponding Jira task moved to **Done**
- This process ensures traceability between task descriptions, Copilot output, and Jira tracking

### 3.4 Epic/Story Edit Flow

- Manual edits to epics or stories trigger a structured diff pipeline
- Diff output includes potential changes to TRDs or task lists
- Changes are reviewed and approved manually before syncing downstream artifacts or Jira

### 3.5 Jira Sync

- Generated epics, stories, and tasks are synced to Jira
- Updates maintain bi-directional traceability
- Edits to Markdown propagate to Jira only after explicit approval

---

## 4. Extensibility

DAKSH is modular. You can:
- Add new columns (e.g. `Design Links`) with parser changes
- Plug in alternative output formats (e.g., Mermaid diagrams)
- Swap Jira adapter with another task management system

---

## 5. Edge Cases & Constraints

- Index rows must be complete for traceability to work
- Duplicated artifact references across rows are flagged
- File path case sensitivity is enforced
- Mid-sprint changes to index structure are tracked but should be intentional
- Edits to epics or stories mid-sprint must trigger a diff + approval cycle before downstream artifacts are rewritten
- Copilot-generated completions must pass a human review stage before being marked complete in project tracking systems