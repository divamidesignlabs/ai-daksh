# Instruction Template: Generating a Product Vision Document (`vision.md`)

## 🎯 Goal
Guide an AI assistant to create a clear, inspiring **Product Vision Document** (`vision.md`) in Markdown format, based **strictly** on a set of input `.md` files describing a project’s specifications. The Vision Document sets high-level direction, aligns stakeholders, and avoids hallucination by grounding every statement in the source files.

---

## 🛠️ Process Overview

1. **Receive Input Files**  
   The user provides one or more `.md` files (in a folder structure) containing functional requirements, user stories, business rules, data schemas, etc.

2. **Ask Clarifying Questions**  
   Before drafting `vision.md`, the AI **must** ask targeted questions to fill any gaps and ensure fidelity to source material:
   - **Product Name / Placeholder:** “What is the official product name, or should I use a placeholder?”  
   - **Primary Stakeholders / Personas:** “Which roles or personas should be highlighted?”  
   - **Success Metrics / KPIs:** “Do you have specific target metrics (e.g., <5% overdue rate)?”  
   - **Scope Boundaries:** “Are there modules explicitly out of scope?”  
   - **Timeline / Milestones:** “Do you have quarter-based phases or release dates?”  
   - **Strategic Differentiators:** “What unique strengths or differentiators should be called out?”

3. **Extract & Synthesize**  
   Systematically parse each `.md` file in the folder:
   - Identify **business objectives** and **problem statements**.
   - Collect **user needs** and **personas**.
   - Gather **core capabilities** and **features**.
   - Record any **explicit goals, metrics, timelines, and constraints**.

4. **Draft `vision.md`**  
   Using **only** the extracted information and user responses, generate a `vision.md` with the following structure. **Do not** introduce new content beyond source files and clarifications.

---

## 📐 Vision Document Structure

\`\`\`markdown
# Product Vision – [Product Name or Placeholder]

## 🚀 1. Vision Statement
A concise, inspirational summary of the product’s future state.  
_Focus on outcomes, not implementation details._

## 👤 2. Target Users / Personas
- **Persona A:** 1–2 line description of role and needs.  
- **Persona B:** 1–2 line description of role and needs.  

## 🧩 3. Problem Statements
- **Problem 1:** Description drawn directly from source files.  
- **Problem 2:** Description drawn directly from source files.  

## 🌟 4. Core Features / Capabilities
- **Feature A:** High-level capability (no deep tech detail).  
- **Feature B:** High-level capability (no deep tech detail).  

## 🎯 5. Business Goals / Success Metrics
- **Metric A:** Target value (e.g., “Reduce overdue tasks to <5%”).  
- **Metric B:** Target value (e.g., “80% of meetings logged via Smart Assistant”).  

## 🔭 6. Scope & Boundaries
**In Scope:**  
- Item 1  
- Item 2  

**Out of Scope:**  
- Item A  
- Item B  

## 📅 7. Timeline / Phases (Optional)
- **Q1 [Year]:** Milestone description.  
- **Q2 [Year]:** Milestone description.  

## 📌 8. Strategic Differentiators
- **Differentiator A:** What makes it unique?  
- **Differentiator B:** What makes it unique?  
\`\`\`

---

## ❓ Clarifying Questions Examples

1. **Product Identity**  
   - What is the product’s official name, or should I use a placeholder?  
2. **Target Users / Personas**  
   - Who are the primary end-users or stakeholder roles?  
3. **Business Goals / KPIs**  
   - Are there any specific targets (e.g., adoption rates, error reductions)?  
4. **Scope & Boundaries**  
   - Which modules/features are **in** scope vs. **out** of scope?  
5. **Timeline / Milestones**  
   - Do you have quarter-based phases or release milestones to include?  
6. **Strategic Differentiators**  
   - What makes this product stand out compared to alternatives?

---

## 👥 Target Audience
Primary readers: **product managers**, **designers**, **engineers**, **QA**, **leadership**, and **clients**.  
- The Vision Document should be:
  - Concise yet sufficiently detailed to guide roadmap decisions.
  - Strictly grounded in the provided `.md` source files.
  - Free of technical implementation specifics or hallucinated content.

---

## 📝 Output Details
- **Filename:** `create-visiondoc.md`  
- **Format:** Markdown (`.md`)  
- **Location:** Current working directory (or as specified by user)

---

## ✅ Final Instructions
1. **Do NOT** generate `vision.md` until all clarifying questions are answered.  
2. **Use only** facts and language present or implied in the input `.md` files.  
3. **Avoid hallucination:** If something is missing or ambiguous, seek clarification rather than invent.  
4. **Follow the prescribed structure** exactly for consistency across projects.  
5. Once clarifications are received, produce `vision.md`, ready for stakeholder review.
