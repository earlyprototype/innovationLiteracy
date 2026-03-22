# Four Gates Verification

## Introduction

Four Gates Verification is a systematic methodology for evaluating AI outputs before accepting or acting on them. Developed by Jan Szczepanski (2026), it provides a structured framework for catching failures that don't appear as failures - plausible but flawed AI generation.

**Core principle:** "Comfort with AI output is inversely correlated with verification quality."

When AI output feels perfect, verification is most needed.

Related: [What are Skills and Competencies](../What%20are%20Skills%20and%20Competencies.md), [Verification Discipline](../../6_Behaviours/resources/verification_discipline.md), [AI-Augmented Interventions](../../2_Interventions/resources/ai_augmented_interventions.md)

---

## The Four Gates

### Gate 1: Alignment Check

**Question:** Did AI answer your actual question or drift to an adjacent easier problem?

**Why it matters:** AI optimises for plausible-sounding answers. When your question is complex or ambiguous, AI may drift to simpler related questions it can answer confidently.

**How to check:**
1. Compare AI output to your original prompt intent
2. Ask: "Is this answering what I asked, or something adjacent?"
3. Look for scope drift (broader or narrower than requested)
4. Check if AI reframed your question without acknowledgment

**Red flags:**
- Output feels complete but addresses different problem than asked
- Solution to adjacent problem that's easier to solve
- Output that sounds authoritative but isn't what you need

**Example failure:**
- **Prompt:** "How can we help users track receipts without adding cognitive load?"
- **AI Output:** "Here are 5 receipt tracking apps users can adopt"
- **Problem:** AI answered "what tools exist?" not "how to reduce cognitive load"

**When to apply:** After every AI generation, before accepting output

**Recovery:** Refine prompt to specify what you're NOT asking for: "Do not suggest existing apps - focus on reducing friction in current workflow"

Related: [Prompt Engineering](./prompt_engineering.md)

---

### Gate 2: Tension Check

**Question:** Are trade-offs and complexities visible, or is this suspiciously neat?

**Why it matters:** Real problems have inherent tensions - cost vs. speed, simplicity vs. power, accessibility vs. security. AI often smooths over these tensions to produce coherent-sounding outputs.

**How to check:**
1. Scan output for counterarguments, limitations, conflicting requirements
2. Ask: "Where are the downsides? What am I not seeing?"
3. Look for "perfect" solutions with no trade-offs mentioned
4. Check if output acknowledges uncertainties or unknowns

**Red flags:**
- Solution appears flawless with no downsides
- No mention of implementation challenges
- Missing discussion of what you'd have to give up
- Overly confident conclusions with no caveats

**Example failure:**
- **Prompt:** "Evaluate whether we should build vs. buy this capability"
- **AI Output:** "Building in-house provides complete control, customisation, and long-term cost savings"
- **Problem:** Missing trade-offs (upfront cost, maintenance burden, slower time-to-market, expertise requirements)

**When to apply:** When evaluating AI-generated ideas, synthesis, or recommendations

**Recovery:** Explicitly prompt for tensions: "What are the trade-offs between these approaches? What am I giving up if I choose option A?"

Related: [AI-Augmented Interventions - Ideate Phase](../../2_Interventions/resources/ai_augmented_interventions.md)

---

### Gate 3: Source Grounding Check

**Question:** Can you trace claims back to source material?

**Why it matters:** AI synthesises patterns, but also hallucinates - generates plausible-sounding claims not grounded in provided sources. For research synthesis, feedback analysis, and documentation tasks, source grounding is critical.

**How to check:**
1. For each AI-synthesised insight, identify which source material supports it
2. Click through to source quotes (in tools like NotebookLM) or manually verify
3. Ask: "Which interview/document/feedback session mentioned this?"
4. Flag claims that sound right but can't be linked to specific sources

**Red flags:**
- Insights that sound plausible but lack source citations
- Quantification without data ("most users," "primary concern") when sources don't support
- Patterns that smooth over contradictions in source material
- Claims that go beyond what sources actually said

**Example failure:**
- **AI Output:** "Users primarily struggle with navigation complexity"
- **Source Check:** Only 2 of 8 interview transcripts mentioned navigation; 6 mentioned data entry friction
- **Problem:** AI elevated minor theme to "primary" without grounding

**When to apply:** Any time AI synthesises research, feedback, or documentation

**Recovery:** Request citations: "For each theme, provide supporting quotes with source identifiers (which user, which session)"

Related: [AI-Augmented Interventions - Discovery Phase](../../2_Interventions/resources/ai_augmented_interventions.md), [AI-Augmented Interventions - Test Phase](../../2_Interventions/resources/ai_augmented_interventions.md)

---

### Gate 4: Bias Amplification Check

**Question:** Is AI reflecting your assumptions back or challenging them?

**Why it matters:** AI trained on existing patterns tends to reinforce conventional thinking. When you prompt with embedded assumptions, AI often validates rather than challenges them. This creates echo chamber effect.

**How to check:**
1. Review AI output for whether it challenges any of your initial framing
2. Ask: "Is this telling me what I want to hear?"
3. Look for outputs that perfectly validate your hypothesis
4. Check if AI surfaced contradictions or alternative perspectives

**Red flags:**
- Output confirms all your assumptions
- No counter-arguments or alternative framings offered
- Missing contradictory evidence from sources
- Solutions that align suspiciously well with your preferences

**Example failure:**
- **Prompt:** "Our users need more features to be satisfied"
- **AI Output:** Lists 10 feature ideas that would improve satisfaction
- **Problem:** AI reinforced assumption that more features = satisfaction, didn't challenge whether feature bloat might reduce satisfaction

**When to apply:** When using AI for critique, problem framing, or evaluation

**Recovery:** Explicitly request challenge: "What's wrong with this approach? What assumptions am I making that might be flawed?"

Related: [Cognitive Biases in Innovation](../../5_Mindset/resources/cognitive_biases_in_innovation.md), [AI Tool Failure Modes - Echo Chamber Effect](../../3_Tools/resources/ai_tool_failure_modes.md)

---

## Quick Reference: Running the Four Gates

**After every AI generation, ask:**

1. **Alignment:** Did it answer my actual question? ✓/✗
2. **Tension:** Are trade-offs visible? ✓/✗
3. **Source Grounding:** Can I trace claims to sources? ✓/✗
4. **Bias:** Is it challenging my assumptions? ✓/✗

**If any gate fails:** Don't accept output as-is. Diagnose and iterate.

---

## Stage-Specific Application

### Discovery Phase (Empathise)

**Primary gates to emphasise:**
- **Gate 3 (Source Grounding):** Critical for research synthesis
- **Gate 4 (Bias Amplification):** Prevent confirmation bias

**Application:**
- After AI synthesises interview notes, verify patterns against source quotes
- Check if AI smoothed over contradictions in user feedback
- Ensure edge cases and outliers weren't dismissed

Related: [AI-Augmented Interventions - Discovery Phase](../../2_Interventions/resources/ai_augmented_interventions.md)

---

### Define Phase (Frame)

**Primary gates to emphasise:**
- **Gate 1 (Alignment):** Ensure problem framing stays on target
- **Gate 4 (Bias Amplification):** Challenge embedded assumptions

**Application:**
- After AI generates problem reframings, check they address YOUR question
- Verify problem statements ground in discovery insights
- Check if AI embedded solutions in problem framing

Related: [AI-Augmented Interventions - Define Phase](../../2_Interventions/resources/ai_augmented_interventions.md)

---

### Ideate Phase (Generate)

**Primary gates to emphasise:**
- **Gate 2 (Tension):** Ensure ideas show trade-offs
- **Gate 1 (Alignment):** Verify ideas address the defined problem

**Application:**
- After AI expands ideation, check for realistic constraints and trade-offs
- Verify ideas maintain connection to user needs
- Flag ideas that sound good but ignore implementation realities

Related: [AI-Augmented Interventions - Ideate Phase](../../2_Interventions/resources/ai_augmented_interventions.md)

---

### Prototype Phase (Build)

**Primary gates to emphasise:**
- **Gate 1 (Alignment):** Does output match prompt intent?
- **Gate 2 (Tension):** Are implementation complexities visible?

**Application:**
- After AI generates structural artifacts, verify they reflect your logic
- Check if outputs show decision points and error states realistically
- Ensure constraints specified in prompt actually constrained output

Related: [AI-Augmented Interventions - Prototype Phase](../../2_Interventions/resources/ai_augmented_interventions.md)

---

### Test Phase (Validate)

**Primary gates to emphasise:**
- **Gate 3 (Source Grounding):** Critical for feedback synthesis
- **Gate 2 (Tension):** Ensure contradictions in feedback preserved

**Application:**
- After AI synthesises test feedback, trace themes to specific user quotes
- Check if AI smoothed over conflicting user reactions
- Verify quantifications ("most users") supported by actual data

Related: [AI-Augmented Interventions - Test Phase](../../2_Interventions/resources/ai_augmented_interventions.md)

---

## Integration with Workflow

### Individual Practice

**After every AI interaction:**
1. Generate output
2. Run Four Gates checks (30 seconds)
3. If any gate fails, refine prompt and regenerate
4. Document what changed and why

**Build muscle memory:** Verification becomes automatic with repetition

---

### Team Practice

**In workshop settings:**
- Facilitator runs Four Gates checks visibly
- "Before we accept this synthesis, let's verify it"
- Model the behaviour: Talk through each gate check aloud
- Make verification a shared team activity, not just facilitator's private check

**Shared language:** "Let's run a tension check on this" becomes team norm

Related: [AI-Augmented Facilitation](../../9_Facilitation/resources/ai_augmented_facilitation.md)

---

### Documentation

**Capture verification decisions:**
- Which gates flagged concerns
- What was revised based on checks
- What you learned about prompt quality

**Builds prompt library:** Document which prompt patterns pass gates consistently

---

## When Verification Catches Issues

### Gate 1 (Alignment) Failure

**Symptom:** Output addresses adjacent problem, not your question

**Diagnosis:** Prompt ambiguous or AI found easier question to answer

**Action:**
1. Refine prompt to specify what you're NOT asking
2. Provide examples of desired output format
3. Add constraints to narrow scope

**Learning:** What did you assume was obvious that AI missed?

---

### Gate 2 (Tension) Failure

**Symptom:** Solution appears perfect, no trade-offs mentioned

**Diagnosis:** AI smoothing over inherent tensions to produce coherent output

**Action:**
1. Explicitly prompt for trade-offs: "What are the downsides?"
2. Request multiple perspectives: "What would critics say?"
3. Add constraint: "Include implementation challenges"

**Learning:** What tensions exist that prompt should surface?

---

### Gate 3 (Source Grounding) Failure

**Symptom:** Claims sound right but can't be traced to sources

**Diagnosis:** AI hallucinating or over-interpreting source material

**Action:**
1. Request citations: "Provide source quotes for each claim"
2. Use source-grounded tools (NotebookLM) over general LLMs
3. Manually verify synthesis against original sources

**Learning:** Which sources were ambiguous? What additional context needed?

---

### Gate 4 (Bias) Failure

**Symptom:** AI validates all your assumptions perfectly

**Diagnosis:** Echo chamber effect - AI reinforcing your thinking

**Action:**
1. Explicitly request challenge: "What's wrong with this?"
2. Prompt for alternative framings: "How else could we see this?"
3. Use human peer review for critique, not AI

**Learning:** What assumptions were embedded in prompt? How can you surface them?

---

## Common Questions

**Q: Doesn't this slow down AI use?**

A: Four Gates checks take 30 seconds. Catching failures early saves hours of work building on flawed foundations. Fast wrong outputs are expensive.

---

**Q: When can I skip verification?**

A: When output is low-stakes and easily reversible. For decisions, synthesis, or problem framing - always verify.

---

**Q: What if all four gates pass?**

A: Output is likely sound, but not guaranteed perfect. Four Gates catches common failures, not all failures. Still apply human judgement.

---

**Q: Can AI verify its own outputs?**

A: Partially. You can prompt AI to check alignment and tension, but source grounding and bias checks require human judgement.

---

## Practical Tips

### Build Verification Habit

**Week 1:** Deliberately run all four gates on every AI interaction, document results

**Week 2:** Notice which gates catch issues most frequently in your context

**Week 3:** Verification becomes automatic, takes seconds

---

### Create Verification Checklists

For repeated tasks (synthesis, ideation expansion, feedback analysis), create task-specific gate checks:

**Synthesis checklist:**
- [ ] Gate 3: Can trace each pattern to source quotes?
- [ ] Gate 2: Are contradictions preserved?
- [ ] Gate 4: Am I seeing confirming or challenging data?

---

### Share Failure Examples

When gates catch issues, share with team:
- "Gate 1 caught this - AI answered wrong question"
- "Gate 3 caught this - claim wasn't in sources"

Builds collective understanding of verification value

---

## Further Reading

**Source:**
- Szczepanski, J. (2026). ["The Four Gates – A Verification Methodology for AI Outputs."](https://jszczepanski.medium.com/the-four-gates-a-verification-methodology-for-ai-outputs-6fb92104469f) Medium.

**Related Resources:**
- [Verification Discipline](../../6_Behaviours/resources/verification_discipline.md) - Making verification a team behaviour
- [Prompt Engineering](./prompt_engineering.md) - Improving prompt quality to pass gates
- [AI Tool Failure Modes](../../3_Tools/resources/ai_tool_failure_modes.md) - What gates are preventing
- [AI-Augmented Interventions](../../2_Interventions/resources/ai_augmented_interventions.md) - Applying gates in each process stage

**Research & Best Practices:**
- Nielsen Norman Group: "Facilitating AI-Enhanced Workshops" - Team verification practices
- IDEO U: AI x Design Thinking - Integrating verification into workflow

---

_Element: Skills and Competencies_  
_Systematic AI output verification methodology_  
_Version: 1.0_  
_Created: 2026-03-21_
