<!-- owner: shikanime | zone: internal | purpose: known failure modes and the first-responder fix for each -->

# Troubleshooting

## A language shell won't enter

**Symptom:** `direnv exec algorithm-<lang> …` fails or the shell is empty.
**Cause:** the matching `devenv.shells.algorithm-<lang>` entry or its
`devlib.devenvModules.<lang>` import is missing/misnamed.
**Fix:** check `flake.nix` for a shell block named exactly `algorithm-<lang>`
importing the right `devlib.devenvModules.<lang>`; run `nix fmt` and confirm the
flake evaluates.

## `enterTest` fails locally but passes in CI

**Cause:** local deps drifted from the lockfile. **Fix:** re-pin inside the
shell — `uv lock` / `npm ci` / `mix deps.get` — and re-run; commit the lockfile
if it changed.

## `nix fmt` rejects a docs page

**Cause:** treefmt's rumdl-check rejects Markdown lines over 80 columns.
**Fix:** wrap the offending lines to ≤80 and re-run `nix fmt` until clean.

## One language red in `test.yaml`

**Cause:** an edit landed in a language dir without a matching test, or the
language's build config changed. **Fix:** reproduce with that shell's
`enterTest` locally, add/fix the test, and confirm before pushing.
