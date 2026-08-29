<!-- owner: shikanime | zone: internal | purpose: explain the per-language layout and flake wiring so changes land in the right dir -->

# Architecture

## Goal

A single repo holds algorithm implementations in several languages so the same
problem can be solved and compared side by side. The design constraint is
**isolation**: each language directory is an independent project with its own
toolchain, dependency file, and test runner, so a change in one language never
breaks another. The flake is glue, not a build system — it only supplies
reproducible shells.

## Per-language layout

```text
algorithm-cc/         # C++: CMake + GoogleTest
algorithm-elixir/     # Elixir: Mix + ExUnit
algorithm-javascript/ # Node: npm + Vitest
algorithm-ocaml/      # OCaml: Dune + inline tests
algorithm-python/     # Python: uv + pytest
```

Each dir owns its own build config and `README.md`. There is no shared `src/`
or `tests/` at the repo root — the root `AGENTS.md` description is stale; the
real code lives under the per-language dirs.

## Flake wiring

`flake.nix` uses `flake-parts` and imports four flake modules:

```text
devenv.flakeModule        # reproducible dev shells
devlib.flakeModule        # shared shikanime dev/treefmt helpers
git-hooks.flakeModule     # pre-commit hooks
treefmt-nix.flakeModule   # formatting
```

Under `perSystem.devenv.shells`, one shell is defined per language
(`algorithm-cc`, `algorithm-elixir`, …). Each shell imports `devlib.devenvModules.*`
for that language and sets an `enterTest` script that installs deps and runs the
test suite. CI invokes these shells rather than ad-hoc commands.

## Adding a language

Add `algorithm-<lang>/` with its own build config and tests, then register a
matching `devenv.shells.algorithm-<lang>` in `flake.nix` importing the relevant
`devlib.devenvModules.<lang>` and an `enterTest` runner.
