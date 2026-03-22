# Prompt Engineering & Intent Specification

## Why It Matters

The quality of AI-generated outputs depends directly on the quality of human prompts. This is not a technical limitation - it's a fundamental principle: AI executes instructions literally. Ambiguity, underspecification, and hidden assumptions in prompts produce poor outputs.

Prompt engineering is not "learning to talk to AI." It is learning to articulate intent clearly enough for literal execution. This skill transfers: clear intent specification improves delegation, brief writing, requirements documentation, and cross-functional collaboration.

AI makes this skill visible because failures are immediate and unambiguous. A poorly specified prompt produces unusable output. This diagnostic feedback accelerates learning.

## Key Takeaways

**Intent vs. Request:**
- What you want (intent) is often different from what you ask for (request)
- Prompt engineering is surfacing the gap between intent and articulation
- Iteration reveals hidden assumptions about what "obvious" means

**Constraints Enable Creativity:**
- Unconstrained prompts produce generic outputs
- Well-specified constraints focus AI generation productively
- Source documents (style guides, requirements, examples) act as constraints

**Prompt Development IS Prototyping:**
- When language is material, prompt iteration is the design activity
- Refining prompts based on output evaluation builds understanding
- Document prompt evolution to capture learning

## Core Components of Effective Prompts

### 1. Context Provision

**What:** Background information AI needs to understand the task

**Why it matters:** AI cannot infer your context - it works from what you provide

**Examples:**
- Poor: "Summarise this research"
- Better: "Summarise this user research for a product team deciding which problems to prioritise. Focus on user pain points and their business impact."

**Application:** Provide role, audience, purpose, constraints upfront

---

### 2. Constraint Specification

**What:** Explicit boundaries, requirements, exclusions that shape output

**Why it matters:** Constraints focus generation, prevent drift, ensure relevance

**Examples:**
- Poor: "Generate ideas for improving our app"
- Better: "Generate ideas for improving our app that: (1) address the top 3 user pain points from testing, (2) require less than 2 weeks development, (3) don't require backend changes"

**Application:** Define what must be included, what must be avoided, what format required

**Types of constraints:**
- **Technical:** "Works within existing architecture," "No third-party dependencies"
- **User-centred:** "Addresses pain points identified in user testing," "Suitable for novice users"
- **Resource:** "Implementable within 2 weeks," "Requires no additional budget"
- **Format:** "Output as bullet list," "Maximum 3 sentences," "Include examples"

---

### 3. Success Criteria

**What:** How you'll evaluate whether output meets requirements

**Why it matters:** AI cannot assess quality without criteria - you must define what "good" means

**Examples:**
- Poor: "Make this better"
- Better: "Rewrite this problem statement to: (1) frame as question, (2) avoid embedding solutions, (3) specify target user group"

**Application:** Define evaluation criteria in prompt so AI can self-assess

---

### 4. Examples & Formats

**What:** Show AI what good outputs look like

**Why it matters:** Few-shot learning (providing examples) dramatically improves output quality

**Examples:**
- Poor: "Generate How Might We statements"
- Better: "Generate How Might We statements following this format: 'How might we [verb] [user need] [context]?' Example: 'How might we help busy parents track receipts without adding cognitive load during shopping?'"

**Application:** Provide 1-3 examples of desired output structure

---

### 5. Iterative Refinement

**What:** Treating prompt development as design activity with evaluation and iteration

**Why it matters:** First prompts rarely optimal - iteration reveals what was underspecified

**Process:**
1. Write initial prompt based on intent
2. Generate output
3. Evaluate: What works? What's missing? What's wrong?
4. Diagnose: Which constraints were unclear? What context was missing?
5. Refine prompt based on diagnosis
6. Regenerate and compare versions
7. Document: What changed in prompt, what changed in output?

**Application:** Budget time for 2-3 iterations, not single generation

---

## Stage-Specific Prompt Engineering

### Discovery Phase (Empathise)

**Task:** Synthesise interview notes to identify patterns

**Effective prompt structure:**
```
Context: We conducted 8 user interviews about [topic].
Task: Identify the top 3-5 patterns across these observations, noting contradictions and edge cases.
Constraints: 
- Ground patterns in specific quotes (cite observation numbers)
- Flag where observations contradict each other
- Note edge cases that don't fit patterns
Format: For each pattern, provide: (1) pattern description, (2) supporting evidence (observation citations), (3) contradictions if any
```

**Common failure:** "Summarise these interviews" (no context, constraints, or success criteria)

Related: [AI-Augmented Interventions - Discovery Phase](../../2_Interventions/resources/ai_augmented_interventions.md)

---

### Define Phase (Frame)

**Task:** Generate multiple problem statement framings

**Effective prompt structure:**
```
Context: Based on user research showing [summary of key insights], we need to frame a problem statement.
Task: Generate 5 alternative problem framings, each emphasizing different aspects or stakeholder perspectives.
Constraints:
- Frame as "How Might We..." questions
- Do NOT embed solutions in problem statements
- Each framing should reflect different user needs or system aspects
- Ground each framing in specific discovery insights
Format: For each HMW statement, provide: (1) the question, (2) which discovery insight it emphasises, (3) what makes this framing distinct
```

**Common failure:** "Write a problem statement" (too generic, no grounding, no variation requirement)

Related: [AI-Augmented Interventions - Define Phase](../../2_Interventions/resources/ai_augmented_interventions.md)

---

### Ideate Phase (Generate)

**Task:** Expand human-generated core concepts into variations

**Effective prompt structure:**
```
Context: We generated these 3 core solution concepts: [list concepts]. We need to explore variations.
Task: Generate 10 variations on each concept that maintain core intent whilst exploring different implementations.
Constraints:
- Variations must address [specific user need from research]
- Variations must respect [technical constraints]
- Show trade-offs (faster vs. simpler, cheaper vs. more robust, etc.)
- Range from incremental to ambitious
Format: For each variation, provide: (1) concept description (2 sentences), (2) what it trades off, (3) implementation complexity (low/med/high)
```

**Common failure:** "Give me more ideas" (no seed concepts, no constraints, overwhelming volume)

Related: [AI-Augmented Interventions - Ideate Phase](../../2_Interventions/resources/ai_augmented_interventions.md)

---

### Prototype Phase (Build)

**Task:** Generate low-resolution structural artifact (mind map, process flow)

**Effective prompt structure:**
```
Context: We're prototyping a solution for [problem]. Here are the key components: [list].
Task: Generate a process flow diagram showing how these components work together.
Constraints:
- Low-resolution only (structure, not visual design)
- Show decision points and error states
- Indicate which steps are automated vs. manual
- Format as Mermaid diagram or structured text
Source Documents: [attach style guide, component library, requirements doc]
Success criteria: Process should be clear enough for developer to identify integration points
```

**Common failure:** "Design an app for X" (no constraints, requests high-fidelity too early)

Related: [AI-Augmented Interventions - Prototype Phase](../../2_Interventions/resources/ai_augmented_interventions.md)

---

### Test Phase (Validate)

**Task:** Synthesise user feedback from testing

**Effective prompt structure:**
```
Context: We tested prototype with 6 users. Here are verbatim feedback notes.
Task: Identify themes across feedback, noting contradictions and edge cases.
Constraints:
- Ground themes in specific user quotes (cite which user, which session)
- Flag contradictions (where users disagreed or had opposite reactions)
- Identify edge cases (unusual responses that don't fit patterns)
- Do NOT interpret significance - describe what users said/did
Format: For each theme: (1) theme description, (2) supporting quotes with citations, (3) contradictions if any, (4) frequency (how many users mentioned)
```

**Common failure:** "What did users think?" (no source grounding, invites speculation, missing contradiction handling)

Related: [AI-Augmented Interventions - Test Phase](../../2_Interventions/resources/ai_augmented_interventions.md)

---

## Common Prompt Engineering Mistakes

### Mistake 1: Underspecification

**What it looks like:** "Improve this design," "Make it better," "Summarise this"

**Why it fails:** AI cannot infer your criteria for "good" or "better"

**Fix:** Define success criteria explicitly: "Rewrite this to [specific criteria]"

---

### Mistake 2: Hidden Assumptions

**What it looks like:** "Design a user-friendly interface" (assumes shared definition of user-friendly)

**Why it fails:** Your "obvious" is not universal - AI fills gaps with generic patterns

**Fix:** Make assumptions explicit: "User-friendly for [specific user group] means [specific characteristics]"

---

### Mistake 3: Single-Shot Prompts

**What it looks like:** Writing one prompt, accepting first output, moving on

**Why it fails:** Misses learning opportunity, accepts mediocre outputs

**Fix:** Budget time for 2-3 iterations, refine based on output evaluation

---

### Mistake 4: No Constraint Provision

**What it looks like:** "Generate ideas" without context, boundaries, or success criteria

**Why it fails:** Produces generic, disconnected outputs that don't fit your context

**Fix:** Provide Source Documents (style guides, requirements, examples) as constraints

---

### Mistake 5: Requesting Decisions

**What it looks like:** "Which solution should we choose?" "Is this a good idea?"

**Why it fails:** AI cannot make strategic decisions for your context - lacks values, priorities, strategy

**Fix:** Request synthesis or analysis, maintain human decision-making: "What are the trade-offs between these solutions?"

Related: [AI Tool Failure Modes](../../3_Tools/resources/ai_tool_failure_modes.md)

---

## Practical Application Tips

### Build a Prompt Library

Document prompts that work well:
- Categorise by stage (Discovery, Define, Ideate, Prototype, Test)
- Note what constraints improved outputs
- Share across team for consistency

### Start with Examples

When requesting formatted output, always provide 1-3 examples of desired structure

### Iterate Visibly

When refining prompts, document:
- What changed in prompt
- What changed in output
- What you learned about constraint specification

Makes learning explicit, builds team capability

### Use Source Documents

Rather than describing constraints in prompts, upload constraint sources:
- Style guides constrain visual outputs
- Component libraries constrain technical outputs
- Requirements docs constrain feature scope
- User research constrains problem framing

Source-grounded generation reduces hallucination, improves relevance

Related: [Tool Selection Framework](../../3_Tools/resources/tool_selection_framework.md)

### Verify Outputs Systematically

After generation, run Four Gates checks:
1. **Alignment:** Did AI answer your actual question?
2. **Tension:** Are trade-offs visible?
3. **Source Grounding:** Can claims be traced to sources?
4. **Bias Check:** Is AI challenging or confirming assumptions?

Related: [Four Gates Verification](./four_gates_verification.md), [Verification Discipline](../../6_Behaviours/resources/verification_discipline.md)

---

## Transferable Learning

Prompt engineering skills transfer directly to:

**Delegation:**
- Clear task specification
- Constraint communication
- Success criteria definition

**Brief Writing:**
- Context provision
- Constraint documentation
- Example provision

**Requirements Specification:**
- Functional requirements clarity
- Edge case identification
- Acceptance criteria definition

**Cross-Functional Collaboration:**
- Assumption surfacing
- Context alignment
- Shared understanding of "done"

AI makes intent specification visible through immediate feedback. This accelerates learning that applies across all communication requiring literal interpretation.

---

## Further Reading

**Official Documentation:**
- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) - Comprehensive guide for Claude
- [OpenAI Prompt Engineering Best Practices](https://platform.openai.com/docs/guides/prompt-engineering) - Official OpenAI guidance
- [Google NotebookLM Tips for Beginners](https://blog.google/technology/ai/notebooklm-beginner-tips) - Source-grounded synthesis practices

**Research & Analysis:**
- IDEO U: AI x Design Thinking Workshop Series - Practical application in innovation contexts
- Nielsen Norman Group: "Facilitating AI-Enhanced Workshops" - When and how to use AI in collaborative work

**Related Resources:**
- [AI-Augmented Interventions](../../2_Interventions/resources/ai_augmented_interventions.md) - Stage-specific methods
- [Four Gates Verification](./four_gates_verification.md) - Systematic output evaluation
- [AI Tool Failure Modes](../../3_Tools/resources/ai_tool_failure_modes.md) - What poor prompts produce

---

_Element: Skills and Competencies_  
_Prompt engineering and intent specification fundamentals_  
_Version: 1.0_  
_Created: 2026-03-21_
