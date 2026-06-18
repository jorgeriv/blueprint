# Decision: Initializer Owns Structure, Skills Own Substance

Status: accepted

Date: 2026-06-18

## Context

The project considered whether the first skill should create the initial folder
structure and templates. A cleaner split emerged from comparing Blueprint with
Spec Kit's installation model.

## Decision

The Blueprint initializer should create the project folder structure and
lightweight placeholder files. Skills should carry the substantive templates and
instructions for creating real document content.

## Rationale

This keeps initialization stable while allowing skills to evolve independently.
It also avoids turning the CLI into a large document generator.

## Consequences

`blueprint init` creates the `definition/` structure and `.blueprint/config.json`.
Skills should detect this initialized structure, preserve user-authored content,
and replace placeholders only when enough context exists.
