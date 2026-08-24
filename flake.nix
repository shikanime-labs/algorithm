{
  inputs = {
    devenv.url = "github:cachix/devenv";
    devlib.url = "github:shikanime-studio/devlib";
    flake-parts.url = "github:hercules-ci/flake-parts";
    git-hooks.url = "github:cachix/git-hooks.nix";
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    treefmt-nix.url = "github:numtide/treefmt-nix";
  };

  nixConfig = {
    extra-substituters = [
      "https://cachix.cachix.org"
      "https://devenv.cachix.org"
      "https://shikanime.cachix.org"
    ];
    extra-trusted-public-keys = [
      "cachix.cachix.org-1:eWNHQldwUO7G2VkjpnjDbWwy4KQ/HNxht7H4SSoMckM="
      "devenv.cachix.org-1:w1cLUi8dv3hnoSPGAuibQv+f9TZLr6cv/Hm9XgU50cw="
      "shikanime.cachix.org-1:OrpjVTH6RzYf2R97IqcTWdLRejF6+XbpFNNZJxKG8Ts="
    ];
  };

  outputs =
    inputs@{
      devenv,
      devlib,
      flake-parts,
      git-hooks,
      treefmt-nix,
      ...
    }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      imports = [
        devenv.flakeModule
        devlib.flakeModule
        git-hooks.flakeModule
        treefmt-nix.flakeModule
      ];
      perSystem =
        {
          lib,
          pkgs,
          ...
        }:
        {
          devenv = {
            modules = [
              devlib.devenvModules.nix
              devlib.devenvModules.shell
              devlib.devenvModules.shikanime
              {
                treefmt.config.settings.formatter."dyff-json".excludes = [
                  "algorithm-javascript/package-lock.json"
                ];
                # treefmt --check walks gitignored generated artifacts and reformats
                # them, failing devenv test. settings.excludes is the real option
                # (settings.global.excludes is stripped by the treefmt-nix schema).
                # gitignore-style trailing-slash globs exclude the whole directory
                # recursively (the '**' form is not honoured by this treefmt version).
                treefmt.config.settings.excludes = [
                  ".devenv/"
                  ".direnv/"
                  ".rumdl_cache/"
                  ".pre-commit-config.yaml"
                ];
              }
            ];
            shells = {
              algorithm-cc = {
                enterTest = ''
                  cd algorithm-cc
                  ${lib.getExe pkgs.cmake} \
                    --preset unknown-unknown-gnu \
                    -B out/build/unknown-unknown-gnu
                  ${lib.getExe pkgs.cmake} \
                    --build out/build/unknown-unknown-gnu
                  ${pkgs.cmake}/bin/ctest \
                    --preset unknown-unknown-gnu \
                    --test-dir out/build/unknown-unknown-gnu
                '';
                gitignore.templates = [
                  "tt:c"
                  "tt:c++"
                ];
                packages = [
                  pkgs.ninja
                  pkgs.gcc
                  pkgs.openssl
                  pkgs.binutils
                  pkgs.cmake
                  pkgs.gtest
                ];
                treefmt.config.programs = {
                  clang-format.enable = true;
                  cmake-format.enable = true;
                };
              };

              algorithm-elixir = {
                imports = [
                  devlib.devenvModules.elixir
                ];
                enterTest = ''
                  cd algorithm-elixir
                  ${pkgs.elixir}/bin/mix deps.get
                  ${pkgs.elixir}/bin/mix test
                '';
              };
              algorithm-javascript = {
                imports = [
                  devlib.devenvModules.javascript
                ];
                enterTest = ''
                  cd algorithm-javascript
                  ${pkgs.nodejs}/bin/npm ci
                  ${pkgs.nodejs}/bin/npm run test
                '';
              };
              algorithm-ocaml = {
                imports = [
                  devlib.devenvModules.ocaml
                ];
                enterTest = ''
                  cd algorithm-ocaml
                  ${lib.getExe pkgs.dune_3} runtest
                '';
              };
              algorithm-python = {
                imports = [
                  devlib.devenvModules.python
                ];
                languages.python.directory = "algorithm-python";
                enterTest = ''
                  cd algorithm-python
                  ${lib.getExe pkgs.uv} run pytest
                '';
              };
            };
          };
        };
      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "aarch64-darwin"
      ];
    };
}
