---
name: blueprint-kickstart-idea
description: Kickstart a Blueprint project from a raw idea into a clear north star. Use when the user wants to describe a new project, clarify the initial idea, identify the main goal, define first-pass scope and non-goals, verify assumptions through an interview, and update an initialized Blueprint Project Definition Pack before detailed sub-goals, decisions, plans, or backlog work.
---

# Blueprint Kickstart Idea

Use this skill to turn a raw project idea into the first stable project north
star: the main goal, purpose, initial audience, first-pass scope, non-goals, and
open questions. Keep the idea well defined even when sub-goals remain unknown.

## Preconditions

Work inside an initialized Blueprint project. Confirm that `.blueprint/config.json`
and `definition/` exist before writing files.

If the project is not initialized, tell the user to run `blueprint init --here`
or `blueprint init <project-name>` first. Do not create the scaffold manually.

## Operating Loop

1. Receive the raw idea in whatever form the user gives it.
2. Restate the idea in clear project language.
3. Make provisional assumptions and label them as assumptions.
4. Ask targeted questions that verify or correct those assumptions.
5. Use the user's answers to define the north star.
6. Update only the relevant Project Definition Pack files.
7. End with what is now clear, what remains open, and the next refinement step.

## Interview Style

Be an active interviewer, not a passive note-taker.

- Make intelligent guesses from the raw idea.
- Ask 3-7 questions per round.
- Prefer questions that test a specific assumption.
- Avoid generic discovery questionnaires.
- Do not ask for detailed sub-goals yet unless the user naturally provides them.
- Keep implementation, technology, and backlog discussion out of scope unless the
  user explicitly asks.

Good question pattern:

```text
I am assuming this is mainly for independent creators, not teams. Is that right?
```

Avoid:

```text
What are all the requirements?
```

## Distillation Rules

Separate these categories as the conversation develops:

- Raw idea: what the user said before interpretation.
- Assumptions: plausible inferences that need confirmation.
- Confirmed understanding: what the user has explicitly accepted or corrected.
- North star: the main goal that should guide later refinement.
- Scope: what belongs in the project at this stage.
- Non-goals: what the project should not become.
- Open questions: unresolved issues to preserve for later.

Do not treat assumptions as decisions. When the user confirms or corrects an
assumption, update the documentation in stable language.

## Files To Update

Use the templates in `assets/templates/` as starting points when replacing
placeholder files or creating the first substantive version of a file.

Primary files for this skill:

- `definition/overview.md`
- `definition/context/origin.md`
- `definition/context/problem.md`
- `definition/context/audience.md`
- `definition/shape/purpose.md`
- `definition/shape/scope.md`
- `definition/shape/non-goals.md`
- `definition/unresolved/questions.md`

Optional files:

- `definition/context/constraints.md`, if constraints emerge.
- `definition/unresolved/tensions.md`, if the interview exposes tradeoffs.
- `definition/unresolved/possible-directions.md`, if the user brainstorms
  possible paths that are not yet commitments.

## Writing Rules

Preserve user-authored content unless it is clearly placeholder text.

When a file has `Status: placeholder`, replace it with a substantive first pass.
When a file already has real content, edit incrementally and keep useful
existing context.

Write in a calm, durable project-definition style. Avoid chatty transcript
language. Mention uncertainty explicitly instead of smoothing it away.

The north star should be short enough to guide later work:

```text
The project should help <audience> achieve <primary outcome> by <core approach>,
while avoiding <important boundary>.
```

## Completion Criteria

This skill is complete when the Project Definition Pack has a clear first-pass
answer to:

- What is the project?
- Who is it for?
- What main goal should guide the rest of the refinement?
- What is in scope for now?
- What is out of scope for now?
- What remains unresolved?

If these cannot be answered yet, ask another targeted interview round instead of
pretending the project is defined.
