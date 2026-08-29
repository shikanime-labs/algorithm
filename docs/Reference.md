<!-- owner: shikanime | zone: internal | purpose: the flake devenv shells and test entrypoints for consumers/CI -->

# Reference

## Dev shells (`devenv.shells.*`)

Defined in `flake.nix` under `perSystem.devenv.shells`. Each maps to one
language directory and imports its `devlib.devenvModules.<lang>`.

| Shell | Language | Test entrypoint (`enterTest`) |
| ----------------- | -------- | ------------------------------------ |
| `algorithm-cc` | C++ | `cmake --preset … && ctest` |
| `algorithm-elixir`| Elixir | `mix deps.get && mix test` |
| `algorithm-javascript` | Node | `npm ci && npm run test` |
| `algorithm-ocaml` | OCaml | `dune runtest` |
| `algorithm-python`| Python | `uv run pytest` |

## Flake modules imported

| Module | Role |
| ----------------------- | ----------------------------- |
| `devenv.flakeModule` | reproducible dev shells |
| `devlib.flakeModule` | shared shikanime dev helpers |
| `git-hooks.flakeModule` | pre-commit hooks |
| `treefmt-nix.flakeModule` | formatting |
| `flake-parts.lib.mkFlake` | per-system outputs |

## Key concepts

- **Per-language isolation** — each `algorithm-<lang>/` is independent; never
  share build artifacts across dirs.
- **`enterTest` is CI truth** — what CI runs is exactly the `enterTest` script;
  change behavior there, not in a workflow step.
- **flake inputs** — `automata`, `devlib`, `devenv`, `nixpkgs-unstable`,
  `treefmt-nix`, `git-hooks`, `flake-parts`, `hercules-ci/flake-parts`.
