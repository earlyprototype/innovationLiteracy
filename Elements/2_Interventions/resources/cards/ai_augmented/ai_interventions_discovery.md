---
element: 2
element_name: Interventions
stage: discovery
type: structured-method
time_to_read: 3min
card_set: ai_augmented_interventions
related_cards:
  - four_gates_overview
  - failure_hallucination
  - failure_outsourced_cognition
  - verification_core_actions
source_doc: ../(../../ai_augmented_interventions.md)
image_meta_description: "A human hand and a digital interface sorting through interview notes together — the human circling key quotes while the screen highlights patterns."
---

# AI-Augmented Interventions: Discovery Phase

## Why It Matters

Discovery synthesis with AI can accelerate pattern identification whilst maintaining grounding in real user data. Critical: humans must own interpretation, AI assists with analysis. Without intervention, teams outsource the most valuable cognitive work — deciding what matters.

## Pattern Interrupts

**"AI synthesises, humans interpret"**
- After using AI to extract patterns from interview notes, participants must select which patterns matter and why
- Prevents: Outsourcing interpretation to AI

**"Verify against source"**
- Always check AI synthesis against original quotes/observations
- Prevents: Hallucination acceptance, drift from actual user data

**"What did AI miss?"**
- Deliberate search for patterns AI didn't surface
- Prevents: Over-reliance on AI synthesis, missing contradictions or edge cases

## Structured Methods

### Assisted Synthesis Protocol
1. Humans extract key observations manually from interviews/research (5-7 per source)
2. Paste observations into NotebookLM or Claude with specific synthesis prompt
3. AI identifies patterns and contradictions across observations
4. Humans interpret significance: Which patterns matter for OUR context/users?
5. Humans select actual insights to carry forward

**Tools:** NotebookLM (source-grounded), Claude (large context)
**Why it works:** Humans do the difficult cognitive work, AI accelerates pattern recognition
**Prevents:** Outsourced cognition (Mode 4)

### Source-Grounded Analysis
1. Upload interview transcripts, observation notes as sources to NotebookLM
2. Use specific prompts: "Identify the top 3-5 moments where users expressed emotional friction with [specific process/tool]"
3. For each AI-identified moment, click through to source material to verify context
4. Flag any AI claims that can't be traced to specific quotes

**Tools:** NotebookLM (built for source grounding), Perplexity (cited research)
**Why it works:** RAG-based tools reduce hallucination risk by tying outputs to uploaded sources
**Prevents:** Hallucination acceptance (Mode 5), Synthetic user substitution (Mode 2)

## Technology Adoption Specific

- **Current State Workflow Mapping:** Human observation → AI generates process map → Human verifies against reality
- **Pain Point Synthesis:** Collect from multiple stakeholders → AI clusters themes → Human prioritises based on strategy

## Integration with Traditional

- Traditional: "Dig deeper" (ask why five times)
- AI-augmented: "Verify against source" (check AI synthesis against original quotes)
- Work together: Both ensure depth and grounding

---

_Card Set: AI-Augmented Interventions · Discovery Phase_
_Source: [ai_augmented_interventions.md]((../../ai_augmented_interventions.md))_
