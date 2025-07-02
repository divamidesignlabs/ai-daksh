# 🧠 Epic Creation Agent

## What It Is

The Epic Creation Agent is an LLM-powered tool that analyzes upstream planning documents — such as vision, specs, and business overviews — and generates a structured `project-epics.ini` file. This file serves as the first technical artifact in the DAKSH pipeline.

---

## Where It's Used

- 🔹 **First step in the DAKSH flow**: It creates the seed structure from which TRDs and tasklists are generated.
- 🔹 **Jira sync**: Upon generation of the `.ini`, the agent (or pipeline) can push epics and stories into Jira.
- 🔹 **Auditable planning**: The `.ini` references upstream `.md` sources, ensuring traceability and transparency.

---

## How to Use It

```bash
daksh agent create-epics --from docs/specifications/
```

Optional flags:
```bash
--vision docs/specifications/strategy/vision.md
--functional docs/specifications/functional/requirements.md
--business docs/specifications/business/overview.md
--output tasks/epics.ini
```

> 🔍 Default behavior assumes a directory containing `.md` files; the agent will auto-detect and prioritize files based on naming heuristics.

---

## How It Works

1. **Document Ingestion**
   - Parses and chunkifies relevant Markdown files
   - Builds a semantic graph of user needs, features, modules, and flows

2. **Clustering and Structuring**
   - Groups related ideas into potential epics
   - Assigns short `EPIC_ID` keys (slugified from headings)
   - Associates each epic with candidate stories

3. **INI Generation**
   - Each `[epic-name]` becomes a section in the `.ini`
   - Each story is listed as a `KEY = Description | Referenced Markdown`

4. **Validation**
   - Deduplicates story IDs and descriptions
   - Confirms referenced `.md` files exist
   - Can be run with `--dry-run` to preview output

---

## Sample Output

```ini
[onboarding]
ONBRD-001 = Setup project folder and README | docs/specifications/strategy/vision.md
ONBRD-002 = Define user personas and glossary | docs/non-technical/glossary/terms.md

[data-ingestion]
DATA-101 = Parse Markdown and resolve links | docs/specifications/technical/specs.md
DATA-102 = Validate task traceability | docs/specifications/functional/requirements.md
```

---

## Future Enhancements

- Support for multi-file `.ini` generation by domain or theme
- Confidence scores on each story line
- Integration with spec diffing tools
- Autocommit + PR creation for every new `.ini` file

---
