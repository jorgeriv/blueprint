# Decision: First Skill Kickstarts The Project North Star

Status: accepted

Date: 2026-06-18

## Context

Blueprint needs a first agent skill that starts the idea-shaping process. The
user may only have a raw project description, not a clear set of goals or
sub-goals.

## Decision

The first skill is `blueprint-kickstart-idea`.

It should help the user describe the project, make provisional assumptions,
verify those assumptions through a focused interview, and document the main goal
and first-pass scope. The result should be a clear north star for later
refinement, even if detailed sub-goals remain undefined.

## Rationale

Later refinement needs a stable guiding idea. If Blueprint begins by asking for
all sub-goals or implementation details, it risks pushing the project into
premature planning. The first skill should instead clarify the main goal and
scope boundary that the rest of the process can orbit.

## Alternatives Considered

- Start with a general documentation skill.
- Start with a decision-recording skill.
- Start with backlog or task generation.

## Consequences

The skill updates the high-level definition files first: overview, origin,
problem, audience, purpose, scope, non-goals, and unresolved questions. More
detailed goal decomposition should be handled by later skills.
