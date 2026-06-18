# Decision: Initializer Installs Blueprint Skills

Status: accepted

Date: 2026-06-18

## Context

Blueprint skills are part of the utility harness. If `blueprint init` only
creates documentation folders, users still need a separate manual step before
agents can use the Blueprint workflow inside the initialized project.

## Decision

`blueprint init` should install all bundled Blueprint skills into the target
project.

Skills are installed under `.agents/skills/` so project-local agents can
discover and use them after initialization.

## Rationale

The harness should arrive ready to use. The initializer owns structure, and it
also makes the relevant agent workflows available in the project. The skills
still own the substantive templates and writing behavior.

## Consequences

The Python package must bundle the repository's `skills/` directory. The CLI
must copy bundled skills during initialization and preserve existing skill files
unless `--force` is used.
