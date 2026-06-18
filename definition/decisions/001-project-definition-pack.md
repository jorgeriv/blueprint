# Decision: Project Definition Pack Is The Main Output

Status: accepted

Date: 2026-06-18

## Context

Blueprint was initially described as turning ideas into project context, goals,
decisions, and an actionable backlog. During discussion, the backlog framing
felt too implementation-shaped for the messy beginning of a project.

## Decision

Blueprint should produce a Project Definition Pack as its primary output.

The Project Definition Pack should capture context, purpose, scope, decisions,
open questions, tensions, and possible directions. Backlog generation may exist
later, but only as a downstream export after the project is clear enough.

## Rationale

Early project work needs clarity before tasks. A durable definition gives future
humans and agents enough context to act without re-litigating the whole idea.

## Alternatives Considered

- Make backlog generation the primary output.
- Keep a single definition document instead of a structured folder.

## Consequences

The initializer should create definition folders and placeholders, not backlog
files. Skills should focus on interviews, assumptions, decisions, and context
distillation before implementation planning.
