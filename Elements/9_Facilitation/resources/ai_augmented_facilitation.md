# AI-Augmented Facilitation

## Introduction

When AI tools are present in innovation workshops, the facilitation role expands: facilitators orchestrate human-AI interaction patterns, prevent common failure modes, and ensure AI accelerates human thinking rather than substitutes for it.

This is not "teaching people to use ChatGPT" - it is managing group dynamics when AI is participant in the process.

Related: [What is Facilitation](../What%20is%20Facilitation.md), [AI-Augmented Interventions](../../2_Interventions/resources/ai_augmented_interventions.md), [AI Tools Landscape](../../3_Tools/resources/ai_tools_landscape.md)

---

## Pre-Session Preparation

### Tool Selection & Setup

**Match AI tool capability to task:**
- NotebookLM for research synthesis and document analysis (source-grounded)
- ChatGPT/Claude for ideation expansion and reframing
- Perplexity for cited research and background context
- Mural AI for visual clustering and organisation
- v0/Bolt.new for rapid functional prototyping (later stages only)

**Pre-test prompts and source documents:**
- Run through planned AI interactions before session
- Understand output patterns and quality thresholds
- Prepare fallback plans for when AI generates unusable output
- Test time requirements: How long does synthesis actually take?

**Decide control model:**
- Facilitator-controlled AI: Facilitator operates tools, group observes (faster but less ownership)
- Participant-controlled AI: Participants operate tools directly (slower but builds capability)
- **Recommendation:** Participant-controlled where possible (co-creation preferred)

Related: [AI Tools Landscape](../../3_Tools/resources/ai_tools_landscape.md)

### Time Budgeting Adjustment

**Critical principle: Budget MORE time than expected for AI-augmented tasks, not less**

Traditional time estimates don't apply:
- Manual synthesis: 15 mins of pattern identification
- AI-augmented synthesis: 5 mins generation + 15 mins interpretation/iteration = 20 mins total

**Why tasks take longer:**
- Reading AI outputs takes time
- Verification against sources takes time
- Group discussion of interpretation takes time
- Prompt iteration when first output inadequate takes time

**Where speed gains occur:**
- Documentation and synthesis grunt work
- Generating variations and expansions
- Structuring messy data into organised formats
- Post-workshop synthesis and follow-up

**Not in real-time generation and interpretation** - this is slower with AI present

### Framing AI Role

Prepare explicit positioning language:

**"AI is rendering engine for your logic, not solution generator"**
- Sets expectation that quality of output depends on quality of human thinking
- Positions AI as literal executor of instructions, not creative partner

**"Bad AI output is useful diagnostic data"**
- Creates permission structure for failures
- Frames poor outputs as learning moments about prompt clarity

**"We're teaching two things simultaneously"**
- Innovation process AND AI-augmented practice
- Both have value, both require attention
- This is why tasks take longer

**Plan language for failure moments:**
- "This nonsense is useful - what did we fail to specify?"
- "What does this output reveal about our prompt logic?"
- "Let's diagnose this together"

Prevents: Frustration with AI failures, skipping valuable learning moments

---

## During Session: Managing AI Interaction Patterns

### Pattern 1: Assisted Synthesis (Define Phase)

**Use case:** Participants have conducted empathy interviews, need to synthesise findings

**Traditional approach:** Participants write observations on sticky notes, manually cluster, identify patterns (20-30 mins)

**AI-augmented approach:**

**Facilitation moves:**

1. **Human extraction first (10 mins)**
   - Participants manually extract 5-7 key observations from their interview notes
   - Write on sticky notes or digital canvas
   - No AI yet

2. **AI pattern identification (5 mins)**
   - Participants paste observations into NotebookLM or Claude
   - Prompt: "Identify patterns and contradictions across these observations"
   - AI generates synthesis

3. **Facilitate interpretation (15 mins)**
   - "What patterns did AI identify?"
   - "Which ones matter for OUR context?"
   - "What did AI miss?" (manually scan for gaps)
   - "Can we trace each pattern back to specific source quotes?"

4. **Human decision**
   - Participants select and frame the actual problem (not AI)
   - Document decision rationale

**Failure mode prevented:** AI doing all synthesis, participants just approving output

**Key facilitation language:**
- "AI spotted these patterns - which ones resonate with what you heard?"
- "Don't just accept this - verify it against your notes"
- "You own the interpretation, not the AI"

Related: [AI-Augmented Interventions - Discovery Phase](../../2_Interventions/resources/ai_augmented_interventions.md)

### Pattern 2: Expanded Ideation (Ideate Phase)

**Use case:** Generate wide range of solutions, avoid premature convergence on first ideas

**Traditional approach:** Brainstorming, quantity targets, deferred judgement (20 mins, produces 30-50 ideas)

**AI-augmented approach:**

**Facilitation moves:**

1. **Generate human ideas first (10 mins)**
   - Traditional brainstorming, no AI
   - Participants generate 10-15 core concepts
   - Document on board

2. **Feed best concepts to AI (5 mins)**
   - Select 3-5 strongest human ideas as seeds
   - Prompt AI: "Generate variations on these concepts that maintain [specific user needs] and [technical constraints]"
   - AI produces expanded set (50-100 ideas)

3. **Narrow strategically (5 mins)**
   - Facilitator or small group uses AI to filter against evaluation criteria
   - "Of these 100 AI variations, show me only those that [meet criteria]"
   - Curate to manageable set (15-20 ideas)

4. **Present curated set (10 mins)**
   - Show original human ideas + selected AI variations
   - Facilitate evaluation and selection

**Failure mode prevented:** Overwhelming participants with 100 AI ideas, skipping human creative thinking

**Key facilitation language:**
- "We start with human thinking, then use AI to expand"
- "AI gave us 100 variations - I've narrowed to these 20 based on [criteria]"
- "Which of these ideas - human or AI-expanded - merit prototyping?"

Related: [AI-Augmented Interventions - Ideate Phase](../../2_Interventions/resources/ai_augmented_interventions.md)

### Pattern 3: Prompt Co-Creation (Prototype Phase)

**Use case:** Generate low-resolution structural artifacts (mind maps, process flows, wireframes)

**Traditional approach:** Participants sketch on paper, photograph, share (15 mins)

**AI-augmented approach:**

**Facilitation moves:**

1. **Pairs collaborate to write prompt (8 mins)**
   - Not facilitator writing for group
   - Pairs discuss: What output do we need? What constraints matter?
   - Document prompt collaboratively

2. **Surface reasoning (5 mins)**
   - Facilitator asks: "Why did you specify that constraint?"
   - "What happens if we remove this phrase?"
   - "What information does AI need that we haven't provided?"

3. **Generate output together (2 mins)**
   - Run prompt, observe generation
   - Evaluate alignment with intent

4. **Frame iteration as the work (10 mins)**
   - "Refining the prompt IS prototyping when language is your material"
   - If output misses mark, diagnose prompt logic together
   - Iterate prompt, regenerate, compare versions
   - Document: What changed in prompt, what changed in output?

**Failure mode prevented:** Facilitator controlling AI, participants just watching; prompt quality as incidental

**Key facilitation language:**
- "You're writing the prompt, not me - I'm here to help you surface your reasoning"
- "This output isn't what you wanted - what constraint did we miss?"
- "Each prompt iteration teaches us about articulating intent"

Related: [AI-Augmented Interventions - Prototype Phase](../../2_Interventions/resources/ai_augmented_interventions.md), [Prompt Engineering](../../4_Skills_and_Competencies/resources/prompt_engineering.md)

### Pattern 4: Verification Protocol (Test Phase)

**Use case:** Synthesise feedback from user testing sessions

**Traditional approach:** Participants review feedback notes, identify themes manually (20 mins)

**AI-augmented approach:**

**Facilitation moves:**

1. **Collect human feedback (outside workshop)**
   - Structured testing: think-aloud, observation, interviews
   - Document verbatim

2. **AI synthesis (5 mins)**
   - Upload feedback notes to NotebookLM
   - Prompt: "Identify top 3-5 themes, noting contradictions and edge cases"

3. **Run Four Gates check as group exercise (15 mins)**
   - **Alignment:** "Did AI answer our question or something adjacent?"
   - **Tension:** "Are trade-offs visible or is this suspiciously neat?"
   - **Source grounding:** "Can we trace this insight back to specific user feedback?"
   - **Bias check:** "Is AI reflecting our assumptions or challenging them?"

4. **Human interpretation (10 mins)**
   - "Which themes matter most?"
   - "What do they reveal about our solution/problem framing?"
   - "How do we iterate based on this?"

**Failure mode prevented:** Accepting AI synthesis without verification, outsourcing interpretation

**Key facilitation language:**
- "AI identified these themes - now let's verify them"
- "For each theme, find the actual user quotes that support it"
- "What's missing from this synthesis that you saw in testing?"

Related: [AI-Augmented Interventions - Test Phase](../../2_Interventions/resources/ai_augmented_interventions.md), [Four Gates Verification](../../4_Skills_and_Competencies/resources/four_gates_verification.md)

---

## Handling AI Failures

### When AI Produces Nonsense

**Don't apologize or skip** - frame as diagnostic moment

**Facilitation script:**

1. **Pause and acknowledge**
   - "This output is nonsense. That's useful."
   - Don't move on quickly, don't blame the tool

2. **Facilitate analysis**
   - "What did we ask for?"
   - "What did we get?"
   - "What's the mismatch?"

3. **Diagnose prompt logic**
   - "What constraint did we fail to specify?"
   - "Was our question actually clear?"
   - "What context did AI need that we didn't provide?"

4. **Iterate visibly**
   - Refine prompt as group, regenerate
   - Compare outputs: "How did changing X affect the output?"

5. **Extract learning**
   - "What does this teach us about articulating intent?"
   - "When might this same lack of clarity hurt us with human delegation?"

**Why this matters:** Most valuable learning often comes from failures. Rushing past them wastes the diagnostic moment.

### When AI Validates Everything

**Call it out** - suspiciously neat outputs are red flags

**Facilitation script:**

1. **Name the pattern**
   - "This output confirms all our assumptions. That's a red flag."
   - "AI is reflecting our thinking back to us, not challenging it"

2. **Deliberately seek tension**
   - "Let's prompt AI to generate counter-arguments to this idea"
   - "Ask AI: 'What's wrong with this approach?'"

3. **Source check**
   - "Which user feedback supports this conclusion?"
   - "Can you find actual quotes, or is this speculative?"

4. **Reframe AI role**
   - "AI isn't here to validate our thinking"
   - "We need critique, not confirmation"

Related: [AI Tool Failure Modes - Echo Chamber Effect](../../3_Tools/resources/ai_tool_failure_modes.md)

### When Participants Want AI to Decide

**Redirect ownership** - AI can't tell you what matters for your context

**Facilitation script:**

1. **Acknowledge the impulse**
   - "I hear you wanting AI to just tell us which solution is best"
   - "That's tempting because it feels objective"

2. **Clarify AI limitation**
   - "AI can synthesise patterns, but it can't tell you what matters for YOUR users in YOUR context"
   - "That requires human judgement about strategy, values, priorities"

3. **Redirect to human decision**
   - "AI synthesised these options - which one serves your users best and why?"
   - "What criteria matter most in your context?"

4. **Make human judgement visible**
   - Capture decision rationale, not just AI output
   - Document: Why did we select this? What did we prioritise?

**Why this matters:** If AI makes decisions, no learning transfers to humans. The capability stays with the tool.

---

## Stage-Specific Guidance

### Discovery (Empathise)

**AI role:** Synthesis assistant (pattern identification in interview notes)

**Facilitation focus:** 
- Ensure participants verify AI patterns against source quotes
- Maintain ownership of interpretation
- Human observation remains primary, AI assists with analysis

**Time allocation:**
- 40% data collection (human empathy work)
- 20% AI synthesis (pattern generation)
- 40% human interpretation (significance, selection, framing)

**Common pitfalls:**
- Skipping empathy, jumping to AI research
- Accepting AI synthesis without verification
- Outsourcing interpretation to AI

**Facilitation interventions:**
- "Test with humans, not AI" (hard rule)
- "Verify against source" (for every pattern)
- "What did AI miss?" (deliberate gap search)

Related: [AI-Augmented Interventions - Discovery Phase](../../2_Interventions/resources/ai_augmented_interventions.md)

### Define (Frame)

**AI role:** Reframing assistant (generate multiple problem statement variations)

**Facilitation focus:**
- Use AI variations to spark thinking
- Ensure participants select/refine actual problem
- Run Alignment checks (did AI answer our question?)

**Time allocation:**
- 30% manual problem framing attempts
- 20% AI reframing generation
- 50% evaluation and selection

**Common pitfalls:**
- Accepting first plausible AI-generated problem statement
- Missing solution-masquerading-as-problem in AI outputs
- Failing to verify problem grounds in discovery insights

**Facilitation interventions:**
- "Whose problem is this?" (verify user-centricity)
- "Alignment check" (did AI drift?)
- "Remove solution from problem statement" (traditional intervention still applies)

Related: [AI-Augmented Interventions - Define Phase](../../2_Interventions/resources/ai_augmented_interventions.md)

### Ideate (Generate)

**AI role:** Expansion engine (generate variations on human-generated core concepts)

**Facilitation focus:**
- Human ideas first, then AI expansion
- Narrow strategically before overwhelming group
- Maintain deferred judgement during generation

**Time allocation:**
- 40% human ideation (core concepts)
- 20% AI expansion (variations)
- 20% strategic narrowing (curation)
- 20% group evaluation (selection)

**Common pitfalls:**
- Skipping human ideation, going straight to AI
- Presenting all 100 AI ideas to group (overwhelming)
- Treating AI ideas as better because they're numerous

**Facilitation interventions:**
- "Human ideas first" (strict sequencing)
- "Narrow strategically" (curate before presenting)
- "Tension check" (are trade-offs visible?)

Related: [AI-Augmented Interventions - Ideate Phase](../../2_Interventions/resources/ai_augmented_interventions.md)

### Prototype (Build)

**AI role:** Rendering engine (generate low-res structural artifacts from prompts)

**Facilitation focus:**
- Prompt co-creation (collaborative prompt writing)
- Iteration as prototyping activity (language as material)
- Constraint specification (source documents, requirements)

**Time allocation:**
- 30% constraint documentation and prompt writing
- 20% generation
- 30% evaluation and diagnosis
- 20% iteration and refinement

**Common pitfalls:**
- Over-production (high-fidelity too early)
- Prompt quality as incidental rather than central
- Accepting first output without iteration

**Facilitation interventions:**
- "Prompt iteration IS prototyping" (reframe the work)
- "Source documents = constraints" (require constraint provision)
- "Low-resolution first" (deliberately constrain fidelity)

Related: [AI-Augmented Interventions - Prototype Phase](../../2_Interventions/resources/ai_augmented_interventions.md)

### Test (Validate)

**AI role:** Feedback synthesis (identify themes in user reactions)

**Facilitation focus:**
- AI synthesises, humans interpret significance
- Four Gates verification as routine practice
- Plan iterations based on human judgement

**Time allocation:**
- 60% human user testing (collecting feedback)
- 15% AI synthesis (theme identification)
- 25% human interpretation (significance, iteration planning)

**Common pitfalls:**
- AI substituting for actual user testing
- Accepting synthesis without source verification
- Missing contradictions AI smoothed over

**Facilitation interventions:**
- "Test with humans, not AI" (hard rule)
- Four Gates checks (systematic verification)
- "Resistance is data" (diagnose rejection)

Related: [AI-Augmented Interventions - Test Phase](../../2_Interventions/resources/ai_augmented_interventions.md), [Four Gates Verification](../../4_Skills_and_Competencies/resources/four_gates_verification.md)

---

## Key Principles for AI-Augmented Facilitation

### 1. AI Should Accelerate Human Cognition, Not Substitute for It

**What this means:**
- Use AI for synthesis grunt work → humans own interpretation
- Use AI for expansion/variation → humans own evaluation and selection
- Use AI for documentation → humans own strategic decisions

**What this prevents:**
- Outsourced cognition (capability stays with AI, doesn't transfer to humans)
- Participants becoming spectators rather than active thinkers

**Facilitation practice:**
- Constantly redirect ownership: "AI synthesised this - what does it mean to you?"
- Make human decision-making visible: Document why selections were made

### 2. Verification Is Not Optional

**What this means:**
- Model Four Gates checks visibly every time
- Make verification a shared team behaviour, not facilitator's private practice
- Allocate time for verification in agenda

**What this prevents:**
- Hallucination acceptance
- Echo chamber effect
- Bias amplification

**Facilitation practice:**
- Run verification as group exercise, not silent individual check
- Celebrate catches: "Good spot - this claim isn't grounded"
- Build verification muscle memory through repetition

Related: [Verification Discipline](../../6_Behaviours/resources/verification_discipline.md)

### 3. Failure Is Diagnostic

**What this means:**
- Bad AI output reveals flawed human logic
- Frame failures as learning opportunities about intent articulation
- Don't skip failures, mine them for insight

**What this prevents:**
- Frustration with tools
- Missed learning moments
- Attribution error (blaming AI when problem is human prompt)

**Facilitation practice:**
- "This nonsense is useful - let's diagnose it"
- Facilitate analysis of what went wrong
- Extract transferable learning: "When might this lack of clarity hurt us elsewhere?"

### 4. Process Integrity Over Speed

**What this means:**
- Don't skip empathy because AI can synthesise faster
- Don't skip iteration because first output looks good
- Maintain pedagogical arc (false start, discovery, iteration)

**What this prevents:**
- Process acceleration without process integrity (Mode 6 in failure modes)
- Superficial engagement with innovation practice
- AI becoming excuse to cut corners under time pressure

**Facilitation practice:**
- Hold the gates: AI can accelerate WITHIN phases, not skip phases
- Frame speed correctly: "AI accelerates synthesis so we can iterate MORE"
- Resist organisational pressure to collapse stages

### 5. Co-Creation Over Control

**What this means:**
- Participants write prompts, not just facilitator
- Surface reasoning about constraints and intent
- Build prompt engineering capability as you go

**What this prevents:**
- Passive learning (watching facilitator use tools)
- Missing skill transfer
- Dependency on facilitator as AI operator

**Facilitation practice:**
- Pairs/small groups write prompts collaboratively
- Ask: "Why did you specify that constraint?"
- Make prompt evolution visible

Related: [Prompt Engineering](../../4_Skills_and_Competencies/resources/prompt_engineering.md)

---

## Common Facilitation Challenges & Responses

### Challenge: "The AI output is perfect, let's move on"

**Why this is a problem:** Overly neat outputs are red flags (Tension check failure)

**Facilitation response:**
- "This looks perfect. That's suspicious."
- "Where are the trade-offs? What are we not seeing?"
- "Can someone play devil's advocate with this?"

**Follow-up intervention:** Prompt AI to generate counter-arguments or identify risks

### Challenge: "AI says we should do X"

**Why this is a problem:** AI cannot make strategic decisions for your context

**Facilitation response:**
- "AI synthesised options - which one serves YOUR users best?"
- "What criteria matter most in your context?"
- "You own this decision, not the AI"

**Follow-up intervention:** Make decision rationale visible, document why selection was made

### Challenge: "Can we just use AI for the empathy interviews?"

**Why this is a problem:** Synthetic user substitution (Mode 2 failure)

**Facilitation response:**
- "Hard no. AI cannot substitute for human discovery."
- "AI can help synthesise what humans learned, but can't replace the learning"
- "Real user insight is the foundation - without it, everything downstream is speculation"

**Follow-up intervention:** Budget time/resources for real user access upfront

### Challenge: "This is taking longer than traditional methods"

**Why this is a problem:** Mismatched time expectations, doesn't account for interpretation overhead

**Facilitation response:**
- "We're teaching two things simultaneously - innovation process AND AI-augmented practice"
- "Speed gains come from synthesis and documentation, not generation phases"
- "We're building capability, not just producing outputs"

**Follow-up intervention:** Reset time expectations for future sessions based on actual duration

### Challenge: "The AI failed, let's skip this part"

**Why this is a problem:** Missing diagnostic learning opportunity

**Facilitation response:**
- "The AI failure is showing us something about our prompt logic"
- "Let's diagnose this together - what did we fail to specify?"
- "This is valuable learning about articulating intent clearly"

**Follow-up intervention:** Facilitate analysis, iterate prompt, extract transferable learning

### Challenge: Participants under-specify constraints in prompts

**Why this is a problem:** Generic prompts produce generic outputs (Mode 7 failure)

**Facilitation response:**
- "What information does AI need that we haven't provided?"
- "What constraints matter for your context?"
- "Let's document those constraints explicitly in the prompt"

**Follow-up intervention:** Model constraint specification, make reasoning visible

### Challenge: Over-trust of AI outputs without verification

**Why this is a problem:** Hallucination acceptance, bias amplification

**Facilitation response:**
- "Before we accept this, let's verify it"
- "Can someone trace this claim back to source material?"
- "I'm modelling verification behaviour - watch what I check"

**Follow-up intervention:** Make Four Gates checks routine, build verification muscle memory

---

## Post-Session Documentation

**Capture both process and content:**

**AI outputs AND human decisions:**
- Don't just save AI-generated artifacts
- Document what humans decided and WHY
- Capture decision rationale, interpretation, significance judgements

**What prompts worked:**
- Build prompt library for future sessions
- Document which prompts produced useful outputs
- Note constraint patterns that improved results

**Failure modes encountered:**
- What went wrong and how addressed
- Which interventions prevented predicted failures
- New failure patterns not anticipated

**Time actuals vs. estimates:**
- How long tasks actually took with AI
- Where speed gains occurred
- Where tasks took longer than traditional approaches

**Reflection questions for next iteration:**
- What did AI accelerate effectively?
- Where did AI hinder or distract?
- What verification behaviours emerged (or didn't)?
- Which facilitation interventions worked?

---

## Troubleshooting Guide

### Symptom: Participants jumping to AI immediately, skipping human thinking

**Diagnosis:** Misunderstanding of AI role as replacement rather than amplifier

**Intervention:** "Human work first" sequencing, explicit ordering

**Prevention:** Frame AI role clearly in pre-session setup

---

### Symptom: Long silences while everyone reads AI output

**Diagnosis:** Underestimated time for reading/interpretation

**Intervention:** Budget adequate time, normalize reading time as valuable

**Prevention:** Adjust time allocation in planning (generation is fast, interpretation is slow)

---

### Symptom: Generic, disconnected AI outputs

**Diagnosis:** Prompt quality issue - insufficient constraints

**Intervention:** Prompt co-creation with explicit constraint surfacing

**Prevention:** Require constraint documentation before AI generation

---

### Symptom: AI confirming all assumptions, no tension

**Diagnosis:** Echo chamber effect (Mode 1 failure)

**Intervention:** Deliberate counter-argument generation, bias check

**Prevention:** Frame AI role as mirror not validator, build verification habit

---

### Symptom: Participants asking AI to make decisions

**Diagnosis:** Confusion about what AI can/can't do

**Intervention:** Redirect ownership, clarify interpretation as human work

**Prevention:** Clear framing of AI role in pre-session setup

---

### Symptom: Frustration when AI produces poor output

**Diagnosis:** Failure framed as blocker rather than diagnostic

**Intervention:** Reframe as learning moment, facilitate diagnosis

**Prevention:** Create permission structure for failures in advance

---

## Further Reading

**Core Resources:**
- [What is Facilitation](../What%20is%20Facilitation.md) - Foundational facilitation principles
- [AI-Augmented Interventions](../../2_Interventions/resources/ai_augmented_interventions.md) - Specific methods to deploy
- [AI Tool Failure Modes](../../3_Tools/resources/ai_tool_failure_modes.md) - What you're preventing
- [Four Gates Verification](../../4_Skills_and_Competencies/resources/four_gates_verification.md) - Systematic verification methodology

**Research & Best Practices:**
- Nielsen Norman Group (2026). ["Facilitating AI-Enhanced Workshops: From Ideation to Action"](https://www.nngroup.com/articles/facilitating-ai-workshops/)
- Miro (2026). ["How to Use AI for Workshops: A Facilitator Guide"](https://miro.com/ai/ai-workshop/)
- IDEO U. ["AI x Design Thinking Workshop Series"](https://www.ideou.com/products/ai-design-thinking-certificate)
- Emerge Creatives (2026). ["Designing an Effective Generative AI Workshop: Complete Agenda and Toolkit Guide"](https://www.emerge-creatives.com/post/designing-an-effective-generative-ai-workshop-complete-agenda-and-toolkit-guide)

**Related Elements:**
- [Interventions](../../2_Interventions/What%20are%20Interventions.md) - Methods to deploy
- [Tools](../../3_Tools/What%20are%20Tools.md) - AI tools landscape
- [Skills & Competencies](../../4_Skills_and_Competencies/What%20are%20Skills%20and%20Competencies.md) - Capabilities to build
- [Behaviours](../../6_Behaviours/What%20are%20Behaviours.md) - Verification discipline

---

_Element: Facilitation_  
_Orchestrating AI-augmented innovation sessions_  
_Version: 1.0_  
_Created: 2026-03-21_
