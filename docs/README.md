<!-- owner: shikanime | zone: internal | purpose: docs landing + index for the Algorithm sketchbook repo -->

# Algorithm — Documentation

A multi-language sketchbook of algorithm and data-structure implementations for
study and reference, one directory per language runtime. Each language dir is a
self-contained project (its own deps, build, and tests) wired together by a
single Nix flake that provides reproducible dev shells via `devenv`. The repo
ships no running service.

## Internal ops

- [Architecture](./Architecture.md) — the per-language layout and how the flake
  stitches the dev shells together.
- [Development](./Development.md) — local setup, the build/test/format loop, and
  how to add a language or algorithm.
- [Runbook](./Runbook.md) — how to build, test, and release across languages.
- [Troubleshooting](./Troubleshooting.md) — shell/test failures and CI drift.
- [Reference](./Reference.md) — the flake's `devenv` shells and test entrypoints.

## User-facing docs

The project intro lives in the repo [README](./../README.md). It is the
canonical source for consumers; this `docs/` directory owns internal ops only
and links out rather than duplicating it.
