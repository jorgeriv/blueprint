# Constraints

Status: active

Blueprint should stay lightweight and general-purpose.

Current constraints:

- the initializer should create structure and placeholder files only
- the initializer should install bundled Blueprint skills into the target
  project so the harness is usable immediately
- substantive document templates should live with the skills that use them
- existing user-authored definition content should be preserved by default
- backlog generation should not be treated as the main output
- the framework should work beyond software projects
- the first implementation should remain small enough to evolve through use

Current implementation constraints:

- the CLI is a small Python package
- `blueprint init` supports creating a project directory or initializing the
  current directory
- scaffold files are preserved by default and overwritten only with `--force`
