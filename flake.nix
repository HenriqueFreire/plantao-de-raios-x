{
  description = "Ambiente de desenvolvimento para o jogo Plantão de Raios-X (Ren'Py + Python)";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
        config = {
          allowUnfree = true;
          permittedInsecurePackages = [
            "python3.12-ecdsa-0.19.1"
          ];
        };
      };
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = [
          pkgs.python3
          pkgs.renpy
          pkgs.git
        ];

        shellHook = ''
          echo "🏥 Bem-vindo ao repositório do Plantão de Raios-X!"
          echo "📦 Git branch: $(git branch --show-current 2>/dev/null || echo 'main')"
          echo "🎮 Ren'Py: $(renpy --version 2>/dev/null | head -n 1 || echo 'Disponível')"
          echo "🐍 Python: $(python3 --version 2>/dev/null || echo 'Disponível')"
        '';
      };
    };
}
