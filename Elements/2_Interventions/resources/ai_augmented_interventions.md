# AI-Augmented Interventions

## Introduction

AI-augmented interventions are structured methods that scaffold effective AI use within the innovation process. They prevent common AI failure modes (echo chamber effect, premature convergence, outsourced cognition) whilst capturing acceleration benefits.

These interventions extend the core principle: **Interventions are HOW you're instructed to use tools, not the tools themselves.** When tools are AI systems, the interventions must address AI-specific patterns and failure modes.

Related: [What are Interventions](../What%20are%20Interventions.md), [AI Tools Landscape](../../3_Tools/resources/ai_tools_landscape.md), [AI Tool Failure Modes](../../3_Tools/resources/ai_tool_failure_modes.md)

---

## Discovery Phase (Empathise)

### Purpose
Understand people affected by the challenge through empathy research, then synthesise findings whilst maintaining grounding in real human data.

### AI Role in This Phase
- Synthesis assistant: Identify patterns across interview notes, qualitative observations
- Research support: Background context about user domain before conducting interviews

### Pattern Interrupts

**"AI synthesises, humans interpret"**
- After using AI to extract patterns from interview notes, participants must select which patterns matter and why
- Prevents: Outsourcing interpretation to AI
- Application: Post-synthesis verification moment

**"Verify against source"**
- Always check AI synthesis against original quotes/observations
- Prevents: Hallucination acceptance, drift from actual user data
- Application: For every AI-identified pattern, trace back to specific source quotes

**"What did AI miss?"**
- Deliberate search for patterns AI didn't surface
- Prevents: Over-reliance on AI synthesis, missing contradictions or edge cases
- Application: After reviewing AI output, manually scan source data for gaps

### Structured Methods

**Assisted Synthesis Protocol**

Structure:
1. Humans extract key observations manually from interviews/research (5-7 observations per source)
2. Paste observations into NotebookLM or Claude with specific synthesis prompt
3. AI identifies patterns and contradictions across observations
4. Humans interpret significance: Which patterns matter for OUR context/users? What does this mean for problem framing?
5. Humans select actual insights to carry forward

Tools: NotebookLM (source-grounded), Claude (large context for lengthy data)

Why it works: Humans do the difficult cognitive work (observation selection, interpretation, significance judgement), AI accelerates pattern recognition grunt work

Failure mode prevented: Outsourced cognition (Mode 4 in [AI Tool Failure Modes](../../3_Tools/resources/ai_tool_failure_modes.md))

**Source-Grounded Analysis**

Structure:
1. Upload interview transcripts, observation notes as sources to NotebookLM
2. Use specific prompts: "Identify the top 3-5 moments where users expressed emotional friction with [specific process/tool]"
3. For each AI-identified moment, click through to source material to verify context
4. Flag any AI claims that can't be traced to specific quotes

Tools: NotebookLM (built for source grounding), Perplexity (cited research)

Why it works: RAG-based tools reduce hallucination risk by tying outputs to uploaded sources

Failure mode prevented: Hallucination acceptance (Mode 5), Synthetic user substitution (Mode 2)

### Technology Adoption Specific

**Current State Workflow Mapping with AI Documentation**
- Use AI to structure messy process documentation into clear workflow diagrams
- Human observation of actual workflow → AI generates process map → Human verifies accuracy against reality

**Pain Point Synthesis**
- Collect pain points from multiple stakeholders → AI clusters themes → Human prioritises based on organisational strategy

---

## Define Phase (Frame)

### Purpose
Synthesise discovery findings into clear, actionable problem statement that guides subsequent work.

### AI Role in This Phase
- Reframing assistant: Generate multiple problem statement variations
- Assumption identifier: Surface hidden assumptions in problem framing
- Perspective shifter: Reframe problems from different stakeholder viewpoints

### Pattern Interrupts

**"Alignment check"**
- Did AI answer your actual question or drift to adjacent easier problem?
- Prevents: AI solving wrong problem convincingly
- Application: After every AI problem reframing, compare output to original intent

**"Whose problem is this?"**
- When AI suggests problem framing, verify it reflects user needs not AI's interpretation
- Prevents: Elegant but misaligned problem statements
- Application: Trace problem framing back to specific discovery insights

**"Remove the solution from that problem statement"**
- Standard intervention, now applied to AI-generated problem frames
- AI often embeds solutions in problem statements
- Application: Review AI outputs for solution-masquerading-as-problem

### Structured Methods

**Prompt Co-Creation for Problem Framing**

Structure:
1. Pairs collaborate to write problem framing prompt (not facilitator writing for group)
2. Surface reasoning: "Why did we specify that constraint? What happens if we remove it?"
3. Generate multiple How Might We statements using AI
4. Group evaluates which framing most generative/aligned with strategy
5. Iterate prompt if outputs miss mark, examine why

Tools: ChatGPT, Claude, NotebookLM

Why it works: Making prompt writing collaborative builds ownership, surfaces assumptions, teaches intent articulation

Failure mode prevented: Prompt quality as incidental (Mode 7), Outsourced cognition (Mode 4)

**Problem Statement Iteration Protocol**

Structure:
1. Write initial problem statement manually
2. Prompt AI: "Generate 5 alternative framings of this problem, each emphasizing different aspects or stakeholder perspectives"
3. Review variations, identify which aspects resonate
4. Refine original statement or select strongest AI variation
5. Test refined statement: "Does this reflect our discovery insights? Is it generative? Clear?"

Tools: ChatGPT, Claude

Why it works: AI variations spark thinking, humans maintain decision ownership

Failure mode prevented: First-acceptable-answer acceptance, narrow problem framing

### Cross-Check: Four Gates Verification

**Gate 1 - Alignment:** Does AI-generated problem framing address the challenge we identified in discovery, or has it drifted to something adjacent?

**Gate 2 - Tension:** Does the problem statement reveal inherent trade-offs and complexities, or is it suspiciously clean?

Related: [Four Gates Verification](../../4_Skills_and_Competencies/resources/four_gates_verification.md)

---

## Ideate Phase (Generate)

### Purpose
Generate wide range of potential solutions through divergent thinking, expanding beyond obvious first ideas.

### AI Role in This Phase
- Expansion engine: Generate variations on human-generated core concepts
- Constraint-based generation: Produce ideas within specified boundaries
- Analogous inspiration: Find how other domains solved similar problems

### Pattern Interrupts

**"Human ideas first"**
- Generate initial ideas without AI (10-15 minutes traditional brainstorming)
- Then use AI to expand/diversify
- Prevents: Skipping human creative thinking, defaulting to AI from start
- Application: Strict sequencing - no AI until human ideas documented

**"Narrow strategically"**
- Use AI to filter ideas against criteria BEFORE presenting to full group
- Prevents: Overwhelming participants with 100 AI-generated ideas
- Application: Facilitator or small team uses AI to curate expanded set to manageable number (15-20)

**"Tension check"**
- Are AI-generated ideas showing trade-offs or only benefits?
- Prevents: Overly optimistic solutions that ignore constraints
- Application: Review AI ideation output for realism - flag ideas that appear consequence-free

### Structured Methods

**Expanded Ideation Protocol**

Structure:
1. Traditional brainstorming: Generate 10-15 human ideas (divergent phase)
2. Select best 3-5 concepts as seeds
3. Feed to AI with constraint prompt: "Generate 10 variations on each of these concepts that maintain [specific user needs] and [technical constraints]"
4. Facilitator/small group narrows AI output using evaluation criteria
5. Present curated expanded set (original human ideas + selected AI variations) to full group
6. Group evaluates and selects concepts for prototyping

Tools: ChatGPT, Claude, Perplexity (for analogous inspiration)

Why it works: Combines human creative core with AI expansive capability, prevents overwhelming divergence

Failure mode prevented: Premature convergence (generating only first ideas), AI replacing human creativity

**Constraint-Based Generation**

Structure:
1. Define clear constraints: User needs, technical limits, resource boundaries, strategic priorities
2. Document constraints explicitly in prompt
3. Generate ideas within guardrails: "Generate solutions that address [user need] whilst respecting [constraint A] and [constraint B]"
4. Evaluate outputs for constraint adherence
5. Iterate prompt if AI ignores constraints

Tools: ChatGPT, Claude

Why it works: Constraints enable focused creativity, prevent generic solutions

Failure mode prevented: Unconstrained generation producing disconnected ideas

### Technology Adoption Specific

**Implementation Pathway Options with AI**
- Human-identified adoption barriers → AI generates multiple implementation approaches addressing each barrier → Human evaluation of feasibility

**Hybrid Solution Exploration**
- Prompt AI to generate solutions blending new/existing technology rather than wholesale replacement

---

## Prototype Phase (Build)

### Purpose
Make thinking tangible and testable through rapid prototyping, treating prototypes as questions not answers.

### AI Role in This Phase
- Rendering engine: Generate low-resolution structural artifacts from prompts
- Documentation assistant: Produce specifications, process maps from rough notes
- Rapid visualisation: Convert descriptions into diagrams, wireframes, mind maps

### Pattern Interrupts

**"Prompt iteration IS the prototyping"**
- Refining prompts to get better outputs is the core activity when using generative tools
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

### Structured Methods

**Holodeck Configuration Protocol**

Structure:
1. Prepare Source Documents: Style guides, component libraries, requirements docs uploaded to NotebookLM or provided as context
2. Collaborative prompt writing: Pairs write prompt specifying desired output structure and assembly logic
3. Surface reasoning: "Why did we specify this constraint? What happens if we loosen it?"
4. Generate artifact: AI produces mind map, process flow, infographic, or wireframe
5. Evaluate output: Does it reflect our logic? Are gaps visible? Does structure make sense?
6. Iterate prompt based on evaluation, regenerate, compare versions

Tools: NotebookLM (for structured documents → visual artifacts), ChatGPT/Claude (for description → diagram), v0/Bolt.new (for wireframe → functional prototype)

Why it works: Explicit constraint provision + iterative refinement makes "language as material" visible, builds prompt engineering capability

Failure mode prevented: Prompt quality as incidental (Mode 7), Premature convergence (Mode 3)

**Iterative Refinement Protocol**

Structure:
1. Generate initial prototype from prompt
2. Evaluate against requirements: What works? What's missing? What's wrong?
3. Diagnose prompt logic: Which constraints were unclear? What did we fail to specify?
4. Refine prompt based on diagnosis
5. Regenerate, compare versions
6. Document: What prompt changes produced what output changes?

Tools: NotebookLM, v0, Bolt.new, Claude (Code generation)

Why it works: Explicit iteration loop makes learning visible, builds understanding of how constraint specificity affects output

Failure mode prevented: Accepting first output, missing learning opportunity

### Fidelity Discipline

Match AI tool fidelity to phase certainty:
- **Early Prototype:** NotebookLM mind maps, Claude-generated ASCII diagrams, paper + photo
- **Mid Prototype:** v0 wireframes, Figma AI with constraints, structured mockups  
- **Late Prototype:** Bolt.new/Lovable functional tests, Cursor/Windsurf implementation

Related: [Tool Selection Framework](../../3_Tools/resources/tool_selection_framework.md)

---

## Test Phase (Validate)

### Purpose
Put prototypes in front of real users, gather feedback, learn systematically. Testing is investigation, not validation.

### AI Role in This Phase
- Feedback synthesis: Identify themes and contradictions across test sessions
- Documentation assistant: Structure messy test notes into organised insights
- Iteration planning: Map feedback to potential design changes

### Pattern Interrupts

**"Test with humans, not AI"**
- AI cannot substitute for genuine user feedback
- Prevents: Synthetic testing, asking AI "would users like this?"
- Application: Hard rule - AI synthesises human feedback, doesn't replace collecting it

**"AI as documentation assistant"**
- Use AI to synthesise feedback themes, not to validate whether ideas are good
- Prevents: Echo chamber effect, confirmation bias
- Application: Frame AI role explicitly: "AI identifies patterns in feedback, we interpret significance"

**"Resistance is data"**
- When users reject AI-generated solutions, diagnose why
- Is prompt logic broken? Wrong problem? Poor execution?
- Application: User rejection triggers investigation, not defensiveness

### Structured Methods

**Feedback Synthesis Protocol**

Structure:
1. Collect human feedback through structured testing (think-aloud, observation, interviews)
2. Document verbatim: What users said, what they did, what surprised them
3. Upload feedback notes to NotebookLM or paste into Claude
4. Prompt AI: "Identify the top 3-5 themes across this feedback, noting contradictions and edge cases"
5. For each AI-identified theme, verify against source feedback (trace to specific quotes)
6. Humans interpret significance: Which themes matter most? What do they reveal about our solution/problem framing?
7. Plan iterations based on interpretation

Tools: NotebookLM (source-grounded synthesis), Claude (large context)

Why it works: AI handles pattern recognition grunt work, humans maintain interpretive ownership and strategic decision-making

Failure mode prevented: Outsourced cognition (Mode 4), Hallucination (Mode 5)

**Verification Protocol for Synthesised Insights**

Structure:
1. For each AI-synthesised insight, ask: "Can we trace this back to specific user feedback?"
2. If yes: Document which test sessions, which users, what they said
3. If no: Flag as speculative, exclude from iteration planning
4. Check for contradictory feedback AI may have smoothed over
5. Identify edge cases or outlier responses AI may have dismissed

Tools: NotebookLM (enables source-linking), manual review of test notes

Why it works: Maintains grounding in real user data, prevents AI from generating plausible-but-unsupported insights

Failure mode prevented: Hallucination acceptance (Mode 5), Echo chamber effect (Mode 1)

### Cross-Check: Four Gates Verification

**Gate 1 - Alignment:** Did AI synthesise the feedback we actually received, or has it drifted to more convenient themes?

**Gate 2 - Tension:** Does the feedback synthesis show contradictions and conflicts, or has AI smoothed everything into false consensus?

**Gate 3 - Source Grounding:** Can every synthesised theme be traced back to specific user quotes from test sessions?

**Gate 4 - Bias Amplification:** Is AI surfacing feedback that challenges our assumptions, or only highlighting what confirms our hypothesis?

Related: [Four Gates Verification](../../4_Skills_and_Competencies/resources/four_gates_verification.md), [Verification Discipline](../../6_Behaviours/resources/verification_discipline.md)

---

## Cross-Stage Interventions

These apply across multiple stages or at transition points.

### Four Gates Verification (Apply After Each AI Interaction)

**Gate 1 - Alignment Check**
- Question: Did AI answer your actual question or drift to adjacent easier problem?
- Method: Compare AI output to original prompt intent
- Red flag: Output feels complete but addresses different problem than asked
- Application timing: Immediately after AI generation, before accepting output

**Gate 2 - Tension Check**
- Question: Are trade-offs visible or is this too neat?
- Method: Scan output for counterarguments, limitations, conflicting requirements
- Red flag: Solution appears perfect with no downsides or complexities
- Application timing: During evaluation of AI-generated ideas or synthesis

**Gate 3 - Source Grounding Check**
- Question: Can you trace claims back to source material?
- Method: For synthesis tasks, verify AI conclusions reference actual data
- Red flag: Insights that sound plausible but can't be linked to specific source quotes
- Application timing: Any time AI synthesises research, feedback, or documentation

**Gate 4 - Bias Amplification Check**
- Question: Is AI reflecting your assumptions back?
- Method: Check if output challenges any of your initial framing
- Red flag: AI output perfectly validates what you already believed
- Application timing: When using AI for critique, problem framing, or evaluation

Source: Four Gates Verification Methodology (Szczepanski, 2026)

Related: [Four Gates Verification](../../4_Skills_and_Competencies/resources/four_gates_verification.md)

### AI Failure as Diagnostic Intervention

**"When AI output is poor, diagnose YOUR thinking"**
- Frame bad outputs as mirror showing flawed logic or unclear constraints
- Don't blame AI - investigate what was underspecified in prompt
- Application: Facilitator reframe: "This nonsense is useful - what did we fail to specify?"

**"Permission to fail productively"**
- Normalise bad AI outputs as useful learning data about prompt clarity and problem framing
- Celebrate diagnostic failures
- Application: When AI generates garbage, stop and analyse why before moving on

### Prompt Co-Creation Intervention

**Structure:**
- Pairs or small groups collaborate to write prompts (not facilitator writing for everyone)
- Surface reasoning: "Why this constraint? What if we change this phrase?"
- Make iteration visible: Document prompt evolution, what changed and why
- Builds ownership and teaches intent articulation

**Application across stages:**
- Define: Collaborative problem framing prompts
- Ideate: Collaborative ideation expansion prompts
- Prototype: Collaborative specification prompts
- Test: Collaborative synthesis prompts

Related: [Prompt Engineering](../../4_Skills_and_Competencies/resources/prompt_engineering.md)

---

## Integration with Traditional Interventions

AI-augmented interventions complement, not replace, traditional interventions:

**Discovery:**
- Traditional: "Dig deeper" (ask why five times)
- AI-augmented: "Verify against source" (check AI synthesis against original quotes)
- Work together: Both ensure depth and grounding

**Define:**
- Traditional: "Remove solution from problem statement"
- AI-augmented: "Alignment check" (did AI answer your question?)
- Work together: Both prevent drift and solution-jumping

**Ideate:**
- Traditional: "Don't explain, don't evaluate" (deferred judgement)
- AI-augmented: "Human ideas first" (then AI expansion)
- Work together: Both preserve divergent thinking

**Prototype:**
- Traditional: "Build it in 7 minutes" (time constraint forces simplicity)
- AI-augmented: "Prompt iteration IS prototyping" (language as material)
- Work together: Both emphasise rapid iteration over perfection

**Test:**
- Traditional: "Don't defend your prototype" (observe behaviour)
- AI-augmented: "Test with humans, not AI" (no synthetic validation)
- Work together: Both maintain focus on real user feedback

---

## Facilitation Notes

**When to introduce AI-augmented interventions:**
- Not in first exposure to innovation process (cognitive overload)
- After participants understand traditional Design Thinking cycle
- When participants have access to AI tools and basic familiarity
- In contexts where AI is already part of work practice

**How to scaffold:**
1. Run traditional intervention first (e.g., manual synthesis)
2. Introduce AI-augmented version (assisted synthesis)
3. Compare: What did AI accelerate? What did humans still need to own?
4. Build explicit skill: Prompt writing, verification, interpretation

**Common facilitation challenges:**
- Participants want to skip to AI immediately → enforce "human work first" sequencing
- Over-trust of AI outputs → model verification behaviour visibly
- Under-specification of constraints → make prompt co-creation collaborative and visible
- Treating AI failures as blockers → reframe as diagnostic moments

Related: [AI-Augmented Facilitation](../../9_Facilitation/resources/ai_augmented_facilitation.md)

---

## Further Reading

**Core Resources:**
- [What are Interventions](../What%20are%20Interventions.md) - Foundational concepts
- [INTERVENTIONS_TAXONOMY](./INTERVENTIONS_TAXONOMY.md) - Traditional intervention methods by stage
- [AI Tool Failure Modes](../../3_Tools/resources/ai_tool_failure_modes.md) - What these interventions prevent
- [Four Gates Verification](../../4_Skills_and_Competencies/resources/four_gates_verification.md) - Systematic verification methodology

**Research & Best Practices:**
- [Facilitating AI-Enhanced Workshops (Nielsen Norman Group)](https://www.nngroup.com/articles/facilitating-ai-workshops/)
- [How to Use AI for Workshops (Miro)](https://miro.com/ai/ai-workshop/)
- [AI x Design Thinking Workshop Series (IDEO U)](https://www.ideou.com/products/ai-design-thinking-certificate)
- Four Gates Verification Methodology - Szczepanski, J. (2026). "The Four Gates – A Verification Methodology for AI Outputs." Medium.

**Related Elements:**
- [Tools](../../3_Tools/What%20are%20Tools.md) - AI tools landscape
- [Skills & Competencies](../../4_Skills_and_Competencies/What%20are%20Skills%20and%20Competencies.md) - Prompt engineering as skill
- [Behaviours](../../6_Behaviours/What%20are%20Behaviours.md) - Verification discipline
- [Facilitation](../../9_Facilitation/What%20is%20Facilitation.md) - Orchestrating AI-augmented sessions

---

_Element: Interventions_  
_AI-augmented pattern interrupts and structured methods_  
_Version: 1.0_  
_Created: 2026-03-21_
