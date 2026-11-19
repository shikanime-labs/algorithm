<!-- owner: Automata | zone: technical | purpose: Canonical technical doc index for shikanime-labs/algorithm -->
# Algorithm — technical index

Shikanime Deva's polyglot collection of algorithmic challenge solutions — a sketchbook of algorithms and data structure implementations for study and reference, organized as one self-contained workbench per language.

## Canonical sources

- [Repository README](https://github.com/shikanime-labs/algorithm#readme)
- [Technical wiki](https://github.com/shikanime-labs/algorithm/wiki)

## Subsystems

### Language workbenches

Each `algorithm-<lang>/` directory is a self-contained workbench with its own README, toolchain, and tests.

| Workbench | Language | Toolchain |
| --- | --- | --- |
| `algorithm-cc/` | C++ | CMake presets, clang-format |
| `algorithm-python/` | Python | uv / pdm |
| `algorithm-ocaml/` | OCaml | dune |
| `algorithm-elixir/` | Elixir | mix |
| `algorithm-javascript/` | TypeScript | vitest |

### Challenge organization

Per-language `src/` directories group implementations by source and year — for example `algorithm-cc/src/adventofcode2015/` and `algorithm-cc/src/adventofcode2022/` — one file per puzzle with `_part_two` variants. Puzzle inputs live under `algorithm-cc/share/<source><year>/<puzzle>/input`.

### CI and dev environment

`.github/workflows/test.yaml` runs the language test suites. The devenv shell provides all toolchains; enter it with `direnv allow` or `nix develop`.

### Contribution

Pull requests follow the org default template in [shikanime-labs/.github](https://github.com/shikanime-labs/.github/blob/main/.github/PULL_REQUEST_TEMPLATE.md); the repository carries no local template.

## Documentation rule

In-repo `docs/` is canonical for technical detail. The [wiki](https://github.com/shikanime-labs/algorithm/wiki) is a rendered human index that links here.
