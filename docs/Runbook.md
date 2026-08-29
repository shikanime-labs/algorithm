<!-- owner: shikanime | zone: internal | purpose: how to build, test, and release across languages without surprises -->

# Runbook

This repo is a study sketchbook, not a deployable service. "Operations" means
keeping every language's dev shell and test suite green so the flake keeps
working as a reproducible environment.

## Running a language

Each language is isolated; run its shell directly:

```bash
direnv exec algorithm-python uv run pytest
direnv exec algorithm-cc  cmake --build out/build/unknown-unknown-gnu
direnv exec algorithm-elixir mix test
direnv exec algorithm-ocaml dune runtest
direnv exec algorithm-javascript npm run test
```

## Testing in CI

CI runs each language's `enterTest` script from `flake.nix` (`test.yaml`). There
is no manual step — a green PR means every `enterTest` passed for every shell.

## Releasing

There is no publish or version tag — the repo is a personal reference collection.
A change is "released" the moment it merges to `main`; downstream flakes that
reference `algorithm` (e.g. via a flake input) pull it in through their lock.

## Branch protection

`main` requires one approving review, linear history, signed commits, and
squash+rebase only. PRs are the merge path; direct pushes are rejected.
