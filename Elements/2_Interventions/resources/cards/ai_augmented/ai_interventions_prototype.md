---
element: 2
element_name: Interventions
stage: prototype
type: structured-method
time_to_read: 3min
card_set: ai_augmented_interventions
related_cards:
  - four_gates_overview
  - failure_premature_convergence
  - failure_prompt_quality
  - prompts_prototype
source_doc: ../(../../ai_augmented_interventions.md)
image_meta_description: "A text prompt on the left transforming into a rough wireframe on the right — language becoming material, with visible iteration marks."
---

# AI-Augmented Interventions: Prototype Phase

## Why It Matters

AI as rendering engine transforms prototyping — but premature high-fidelity outputs kill iteration. The critical shift: prompt iteration IS the prototyping. Language becomes material. Interventions here manage fidelity discipline and ensure teams treat AI as a rendering engine, not a decision-maker.

## Pattern Interrupts

**"Prompt iteration IS the prototyping"**
- Refining prompts to get better outputs is the core activity
- Prevents: Treating prompt writing as incidental, focusing only on AI output
- Application: Frame prompt refinement as valuable work, document prompt evolution

**"Source documents = constraints"**
- Style guides, component libraries, user requirements uploaded as sources enable constrained generation
- Prevents: Unconstrained AI generation producing disconnected outputs
- Application: Require participants to provide constraint sources before prototyping with AI

**"Low-resolution first"**
- Use AI for structural artifacts (mind maps, wireframes, process flows) before high-fidelity
- Prevents: Premature convergence via polished outputs too early
- Application: Deliberately constrain AI fidelity: "Generate wireframe only, no visual design"

## Structured Methods

### Holodeck Configuration Protocol
1. Prepare Source Documents: Style guides, component libraries, requirements uploaded to NotebookLM or provided as context
2. Collaborative prompt writing: Pairs write prompt specifying desired output structure and assembly logic
3. Surface reasoning: "Why did we specify this constraint? What happens if we loosen it?"
4. Generate artifact: AI produces mind map, process flow, infographic, or wireframe
5. Evaluate output: Does it reflect our logic? Are gaps visible? Does structure make sense?
6. Iterate prompt based on evaluation, regenerate, compare versions

**Tools:** NotebookLM (structured docs → visual artifacts), ChatGPT/Claude (description → diagram), v0/Bolt.new (wireframe → functional prototype)
**Why it works:** Explicit constraint provision + iterative refinement makes "language as material" visible
**Prevents:** Prompt quality as incidental (Mode 7), Premature convergence (Mode 3)

### Iterative Refinement Protocol
1. Generate initial prototype from prompt
2. Evaluate against requirements: What works? What's missing? What's wrong?
3. Diagnose prompt logic: Which constraints were unclear? What did we fail to specify?
4. Refine prompt based on diagnosis
5. Regenerate, compare versions
6. Document: What prompt changes produced what output changes?

**Tools:** NotebookLM, v0, Bolt.new, Claude
**Why it works:** Explicit iteration loop makes learning visible
**Prevents:** Accepting first output, missing learning opportunity

## Fidelity Discipline

Match AI tool fidelity to phase certainty:
- **Early:** NotebookLM mind maps, Claude ASCII diagrams, paper + photo
- **Mid:** v0 wireframes, Figma AI with constraints, structured mockups
- **Late:** Bolt.new/Lovable functional tests, Cursor/Windsurf implementation

## Integration with Traditional

- Traditional: "Build it in 7 minutes" (time constraint forces simplicity)
- AI-augmented: "Prompt iteration IS prototyping" (language as material)
- Work together: Both emphasise rapid iteration over perfection

---

_Card Set: AI-Augmented Interventions · Prototype Phase_
_Source: [ai_augmented_interventions.md]((../../ai_augmented_interventions.md))_
