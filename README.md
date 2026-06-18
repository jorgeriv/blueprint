# Blueprint

Blueprint is a general-purpose idea-shaping harness for turning early thoughts
into durable project definition: context, purpose, scope, decisions, and open
questions.

It is meant to support the messy beginning of a project: when the idea is still
part conversation, part intuition, part scattered notes, and not yet ready for
implementation. Blueprint gives humans and AI agents a shared structure for
discussing the idea, refining it, and preserving the reasoning that matters.

## Purpose

Blueprint helps move from raw idea to clear project definition.

It should help a person:

- describe a general idea
- clarify the desired outcome
- identify goals and sub-goals
- brainstorm possible directions
- capture open questions
- separate decisions from possibilities
- describe the project context in increasing detail
- decide when the project is defined clearly enough for future work

The framework should work for software projects, creative projects, business
ideas, personal projects, research efforts, operational changes, or any other
project that benefits from structured thinking before execution.

## Core Idea

Most project planning tools assume the project is already clear enough to manage.
Blueprint starts earlier.

It treats early conversation as a valuable design material. The goal is not to
dump chat transcripts into a folder. The goal is to distill useful context from
discussion into durable artifacts that can guide future work.

The main output is a Project Definition Pack, not a backlog. A backlog may be a
later export once the project is ready for implementation, but Blueprint's first
job is to explain what the project is and why it should exist.

Blueprint has two layers:

1. The initializer owns structure. It creates the project definition folders and
   lightweight placeholder files.
2. Skills own substance. They guide interviews, test assumptions, record
   decisions, and use skill-specific templates to turn conversation into useful
   project context.

## Installation

Blueprint includes a small CLI inspired by Spec Kit's initialization flow.

```sh
blueprint init my-project
blueprint init .
blueprint init --here
```

The initializer creates the project structure and placeholders. Existing files
are preserved by default; use `--force` to overwrite scaffold files.

Initialization also installs bundled Blueprint skills into `.agents/skills/` so
project-local agents can use the Blueprint workflow immediately.

## Project Structure

After initialization, a Blueprint project starts with:

```text
definition/
  overview.md
  context/
    origin.md
    problem.md
    audience.md
    constraints.md
  shape/
    purpose.md
    principles.md
    scope.md
    non-goals.md
  decisions/
  unresolved/
    questions.md
    tensions.md
    possible-directions.md
.blueprint/
  config.json
.agents/
  skills/
    blueprint-kickstart-idea/
```

Possible artifact roles:

- `overview.md` gives a concise, current summary of the project.
- `context/` captures where the idea came from, who it is for, what problem it
  addresses, and what constraints matter.
- `shape/` describes the project's purpose, principles, scope, and non-goals.
- `decisions/` records stable choices that should guide future work.
- `unresolved/` preserves open questions, tensions, and possible directions
  without treating them as commitments.
- `.blueprint/config.json` records Blueprint initialization metadata.
- `.agents/skills/` contains the Blueprint skills installed for the project.

## Skills

Blueprint skills live in `skills/`.

The first skill is `blueprint-kickstart-idea`. It helps an agent gather a raw
project idea, make assumptions, verify them through a focused interview, and
document the main goal and first-pass scope. This creates the project north star
that should guide later, more detailed refinement.

When Blueprint is initialized in another project, bundled skills are copied into
that project's `.agents/skills/` directory.

## Possible Workflow

1. Capture the raw idea.
2. Interview the user about intent, audience, constraints, and success.
3. Extract goals and sub-goals.
4. Explore concepts without committing too early.
5. Record decisions once they become stable.
6. Update the Project Definition Pack with the current understanding.
7. Revisit and refine as the project becomes clearer.

## Status

Blueprint is currently an early implementation. The initializer exists, while the
agent skills that create substantive document content are still being designed.
