# Overview

Status: active

Blueprint is a general-purpose idea-shaping framework for turning raw project
ideas into durable project definition.

Its primary output is a Project Definition Pack: a structured set of documents
that captures context, purpose, scope, decisions, unresolved questions, and
possible directions. Blueprint starts before implementation planning, when the
idea is still partly conversation and partly intuition.

Blueprint has two layers:

- an initializer that creates the project definition structure and placeholder
  files
- agent skills that guide interviews, test assumptions, record decisions, and
  turn conversation into substantive project documentation

The first skill is `blueprint-kickstart-idea`. It turns a raw project idea into
the initial north star: main goal, audience, first-pass scope, non-goals, and
open questions.

The project intentionally treats backlog creation as downstream. The first job
is to clarify what the project is, why it should exist, and what has been
decided.
