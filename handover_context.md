# Handover Context: "Cyborg Design" Workshop Architecture
*A context document for new LLM collaborators covering the pedagogical pivot to a remote-friendly, AI-integrated workshop.*

## 1. Project Objective & Core Concept
The team is fundamentally redesigning the 90-minute foundational workshop session, specifically replacing the traditional Stanford d.school "Wallet Project". Running the physical Wallet Project remotely was deemed ineffective (described as looking at "JPEGs of capitalism" that neuters the visceral empathy of the exercise).

The pivot replaces the physical prototype with a "Cyborg Design" arc. Instead of crafting wallets, participants will use structured **Latent Steering** (or Inference-Time Intervention) to redesign a partner's **"Morning Digital Triage"** routine. This provides a low-stakes, high-emotion, universally relatable friction point to teach modern prototyping skills, systems thinking, and information architecture.

*(Note: The user strongly dislikes the term "vibe-coding". Prefer terms like "Latent Steering" and emphasize Technical Foundation and crash proofing over speed).*

## 2. Key Theoretical & Pedagogical Foundations
*   **"The Material of Modern Prototyping is Language (and Intent):"** Rapid prototyping has evolved. The *prompt* is now the prototype. The quality of the output depends directly on the strictness and clarity of the human intent and constraints.
*   **AI as a Rendering Engine (The "Mirror"), Not a Synthesizer:** Humans must own the difficult work of empathy, problem definition, and logic routing. The AI strictly acts as a literal execution engine that mercifully exposes the flaws in human logic.
*   **The "Holodeck" Metaphor for RAG (NotebookLM):** The AI is an empty room. The user provides the constraints via Source Documents (e.g., a Component Library, a Style Guide), and the Prompt acts as the assembly instruction. If the constraints or assembly instructions are weak, the Holodeck generates hallucinations.

## 3. The 5-Stage "Cyborg Design" Workshop Arc
The finalized 90-minute sequence is designed specifically for **NotebookLM's actual capabilities** (rendering Mind Maps and Infographics, *not* functional interactive apps):

1.  **EMPATHISE: The "Digital Triage" Interview (15 mins)**
    *   *Task:* Paired breakout rooms. Participants interview their partner about their "Morning Digital Triage" routine.
    *   *Focus:* Uncover emotional friction, existing workarounds, and specific stresses.
2.  **DEFINE: The Wingman Synthesis (15 mins)**
    *   *Task:* Participants paste raw interview notes into NotebookLM (Source 1).
    *   *Action:* They prompt NotebookLM to structure the messy data (e.g., "Identify the top 3 moments of emotional friction"). The human reviews the analysis and selects the *actual problem* to solve.
3.  **IDEATE: Semantic Mapping in Mural (15 mins)**
    *   *Task:* Using a Mural board, they map the logical flow of a proposed process solution.
    *   *Constraint:* Pure logic mapping using "Objects" (Nouns) and "Verbs" (Actions). No UI design.
4.  **PROTOTYPE: The "Holodeck" Configuration (25 mins)**
    *   *Task:* They translate their Mural logic map into a highly constrained prompt.
    *   *Execution:* They provide NotebookLM with Source Documents (e.g., a formal Style Guide) and ask it to generate a **Low-Resolution Structural Artifact** (specifically, a Mind Map or Infographic) of the new workflow.
5.  **TEST: The Logic Mirror (20 mins)**
    *   *Task:* The partner reviews the generated Mind Map or Infographic.
    *   *Iteration:* If the artifact hits a dead end or hallucinates steps, the logic is broken. The participant must go back and fix their *prompt logic*, not the AI output.

## 4. Key Documents & Context Files
To execute the upcoming tasks, you must be aware of the following relevant files discussed during the strategy session:

*   **Target Files for the Upcoming Rewrite:**
    *   `_Obsidian_Work/_Projects/FactoryXChange/FX2/Services/FundamentalsInnovationLiteracy/WEEK1_FACILITATION_GUIDE.md`: The primary guide that needs to be rewritten to incorporate the 5-stage Cyborg Design arc.
    *   `_Obsidian_Work/_Projects/FactoryXChange/FX2/Services/FundamentalsInnovationLiteracy/WORKSHOP_DESIGN_PROGRESS.md`: Tracking document to be updated.

*   **Deprecated/Reference Files:**
    *   `_Obsidian_Work/_Projects/FactoryXChange/FX2/Services/FundamentalsInnovationLiteracy/Resources/walletFacilitatorGuide.md`: The original "Wallet Project" guide being replaced.

*   **Aesthetic & Prompt Constraints (The "Holodeck" Source Documents):**
    *   `_tools/_notebookLM/_slidedeckPrompts/fuji/FUJI_METHOD_CONTEXT.md` (and related `tech_neon_art_elements.json` specs): These contain the structural and visual parameters (the "Fuji Tech Art / Avant-garde" theme) that will act as the constrained Style Guide for the workshop's Prototype stage. *(Originated from Note.com articles by Yoshifuji Design).*

*   **Additional Context/Tracking Files (Added to `.gitignore`):**
    *   `.../DESIGN_HANDOVER.md`
    *   `.../JACK_ONBOARDING.md`
    *   `.../outline.md`
    *   `.../_archive/` and `.../_development/` directories.

## 5. The Task Ahead
The immediate next task for the LLM collaborator is to completely rewrite **`WEEK1_FACILITATION_GUIDE.md`** (and any related tracking files like `WORKSHOP_DESIGN_PROGRESS.md`).

When approaching this rewrite, the LLM must:
*   **Tone & Focus:** Ensure the facilitation script clearly communicates the purpose of the AI to the participants—it is a literal mirror for their logic, not a magic solution generator. Focus on rigor, not speed.
*   **Detailing the Steps:** Explicitly write the facilitator instructions. You will need to define the exact structure of the Mural board templates for Ideation and provide the specific prompt templates and Source Document constraints the participants will use in NotebookLM during the Prototype stage.
*   **Leveraging Existing Work:** Integrate the "Fuji Tech Art" aesthetic principles as the baseline styling constraints (from the `FUJI_METHOD_CONTEXT.md` materials) to give participants a rigid but visually striking framework to work within.
