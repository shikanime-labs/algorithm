<!-- owner: shikanime | zone: internal | purpose: the local build/test/format loop and how to extend the set -->

# Development

## Prerequisites

- A recent Nix with flakes enabled.
- `direnv` (each language dir ships `.envrc`); `direnv allow` to load the shell.
- This is a `jj` repo. Branch off `main`; never commit to `main` directly.

## Build and check loop

```bash
nix fmt                        # treefmt: Nix + per-language fmt + md lint (80)
direnv exec algorithm-python uv run pytest
direnv exec algorithm-cc  cmake --preset unknown-unknown-gnu -B out/build/...
```

The canonical test entrypoints are the `enterTest` scripts in `flake.nix`; run
them via `devenv` or CI. `nix fmt` must be clean before a PR is reviewable.

## CI

`.github/workflows/` runs `test.yaml` (per-language suites), `check.yaml`
(format/eval), `land.yaml` (merge), `release.yaml`, `triage.yaml`, `update.yaml`
(renovate/flake bumps), and `cleanup.yaml`. Each language's `enterTest` is the
source of truth for what CI runs.

## Commit style

Plain capitalized title, no conventional-commit prefix. Body uses labels:

```text
Design: <why the algorithm/approach changed>
Related: <full URL to issue/PR>
Closes: <full URL>
```

Keep Markdown wrapped at 80 columns and run `nix fmt` before shipping.

## Adding an algorithm

1. Pick the language dir; add the implementation and a test next to it.
1. Follow that dir's existing test style (GoogleTest, ExUnit, Vitest, Dune
   inline tests, pytest).
1. Confirm `enterTest` for that shell passes locally.
1. `nix fmt` and open a PR against `main`.
