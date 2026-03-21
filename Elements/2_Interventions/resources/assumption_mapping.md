# Assumption Mapping: Making the Implicit Testable

## Why It Matters
Every solution contains hidden assumptions - beliefs treated as facts because they've never been questioned. "Users prefer mobile interfaces." "Our existing customers will want this feature." "The technology is mature enough." These assumptions become baked into thinking so completely that teams don't recognise they're making them.

The danger isn't that assumptions exist - they're necessary for moving forward under uncertainty. The danger is treating them as validated when they're speculative. Assumption mapping forces teams to extract implicit assumptions, make them explicit, assess their risk, and test them before committing substantial resources to solutions that depend on unvalidated beliefs.

It's a deceptively simple intervention with profound impact: writing down what must be true for a solution to succeed transforms wishful thinking into testable hypotheses.

## Key Takeaways

**Assumptions Live in Four Categories:**

**Desirability:** Do people actually want this? Will they use it? Does it solve a problem they care about?
Examples: "Users find the current process painful enough to adopt a new one." "The target audience has the need we've identified." "People will change their behaviour to use this."

**Feasibility:** Can we actually build this? Do we have the capability? Is the technology ready?
Examples: "The API integration is possible within our technical constraints." "Our team has the skills to implement this." "Third-party dependencies will remain stable."

**Viability:** Does this work as a business? Can we sustain it? Will economics work?
Examples: "Users will pay enough to cover costs." "We can deliver at target price point." "Market is large enough to justify investment."

**Adaptability:** Will the organisation adopt this? Can we implement at scale? Will it survive contact with reality?
Examples: "Leadership will support rollout." "Existing processes can accommodate this change." "Staff will adopt new tools/workflows."

**The Riskiest Assumption Framework:**

Not all assumptions are equal. Some are relatively safe (validated by existing evidence, low-impact if wrong). Others are critical (high uncertainty, catastrophic if wrong). The goal isn't testing everything - it's identifying and testing the riskiest assumptions first.

Risk = Uncertainty × Impact

High uncertainty + high impact = test immediately
Low uncertainty + low impact = safe to proceed
High uncertainty + low impact = test if cheap to do so
Low uncertainty + high impact = gather evidence to validate

## Practical Application Tips

**Run Assumption Mapping at Define/Ideate Boundary:**
Best time is after defining the problem but before committing to specific solutions. Once a concept emerges, immediately map what must be true for it to succeed.

**Use This Simple Process:**

1. **Generate:** "For this solution to succeed, what must be true?" Everyone writes assumptions individually (silent work, 5 minutes). This produces more and better assumptions than group discussion.

2. **Cluster:** Group similar assumptions. Look for patterns. Often 20-30 individual assumptions consolidate to 5-8 core beliefs.

3. **Assess Risk:** For each assumption, rate uncertainty (how confident are we this is true?) and impact (how catastrophic if we're wrong?). Plot on 2x2 matrix.

4. **Prioritise Testing:** Top-right quadrant (high uncertainty, high impact) = test immediately. These are project-killers if wrong.

5. **Design Tests:** For each critical assumption, ask: "What's the cheapest, fastest experiment that would validate or invalidate this?"

**Make Assumptions Visible and Persistent:**
Don't let assumption mapping be a one-time exercise. Keep the map visible throughout project. As assumptions are tested, mark them validated (green), invalidated (red), or still uncertain (yellow). This creates living documentation of what's known vs believed.

**Frame as Hypotheses:**
Convert assumptions to testable hypotheses: "We assume X" becomes "We believe X. To test this, we will Y. Success looks like Z."

Example: 
- Assumption: "Users find current check-in process frustrating"
- Hypothesis: "We believe users find check-in frustrating. To test: observe 10 users during check-in, interview after. Success: 7+ report frustration, identify specific pain points."

**Test Cheapest First, Not Everything:**
The goal isn't comprehensive testing - it's risk reduction. Test the assumptions that, if wrong, kill the project. Ignore low-impact assumptions even if uncertain.

**Celebrate Invalidation:**
When testing disproves an assumption, that's success (acquired valuable knowledge) not failure. If the team had proceeded without testing, they'd have invested far more in a doomed direction. Explicitly celebrate: "We learned this won't work for £5k instead of £50k."

**Use as Stage-Gate Criteria:**
Before progressing from prototype to pilot, ask: "Which critical assumptions have we validated? Which remain untested?" Don't allow progression until highest-risk assumptions are addressed.

**Common Pattern: Feasibility Over-Focus:**
Teams naturally obsess over feasibility assumptions ("Can we build it?") because they're technical and feel tractable. They under-invest in desirability ("Will anyone want it?"). Force deliberate attention to all four categories.

**Link to Problem Statement:**
Check assumptions against your problem framing. If you've assumed your way into a different problem than you defined, that's a red flag. Example: Defined problem was "users need faster checkout" but assumptions reveal you're solving "we need more payment options." Which problem are you actually addressing?
