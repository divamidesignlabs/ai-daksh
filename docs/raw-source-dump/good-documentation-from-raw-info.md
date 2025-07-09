

# Notes from Chat: Creating and Maintaining Good Documentation

## Guiding Principles

- Start with structure. Every doc should answer: *what*, *why*, *how*, *who*, *when*.
- Use a clear hierarchy:
  - `README.md` → overview
  - `docs/specs/` → functional + technical specs
  - `docs/usage/` → setup, API, usage guides
  - `docs/dev/` → architecture, code structure, contribution guide
- Avoid prose. Prefer bullet points, diagrams (`mermaid`), tables, fenced code blocks.
- Consistency matters more than perfection.
- Treat docs as code: version-controlled, reviewed, refactored.
- Use TODOs, last-updated tags, and changelogs to track relevance.

## README.md Content

- What is this? → One-liner purpose.
- Why does it exist? → Problem it solves.
- How to use it? → Quickstart guide.
- How to run locally? → Dev setup, env vars, dependencies.
- Where to go next? → Links to deeper docs, issues, or contributors.

## Documentation Order of Creation

- README is written last, read first.
- First document should be `index.md` or `overview.md`.

## Purpose of First Document

- Maps all incoming artefacts by type and relevance.
- States the intent of the project as currently understood.
- Lists what’s missing, unknown, or ambiguous.
- Serves as scaffolding, not final truth.