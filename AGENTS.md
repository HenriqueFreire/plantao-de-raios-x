# Plantão de Raios-X — Contexto e Diretrizes do Projeto

Este arquivo fornece instruções operacionais essenciais para o Antigravity / assistentes de IA em qualquer sessão de desenvolvimento neste repositório.

---

## 🏥 1. Visão Geral do Projeto
* **Nome:** Plantão de Raios-X
* **Propósito:** Projeto Integrador (PI) do Curso Técnico em Radiologia — Senac Campinas.
* **Tecnologias:** Ren'Py 8 (narrativa e telas) + Python 3 (lógica dos minigames e cálculos).
* **Modos de Jogo:**
  1. **Modo Estudo por UC:** Módulos independentes e quizzes focados em cada Unidade Curricular (UC1, UC2, UC6).
  2. **Modo Estágio:** Plantão supervisionado no Hospital Santa Magnólia acompanhando o estagiário Ravi e a Supervisora Cláudia no atendimento de pacientes.

---

## 💻 2. Ambiente e Comandos de Terminal
* **Gerenciador de Ambiente:** Nix Flake (`flake.nix`).
* **Iniciar o ambiente de desenvolvimento:**
  ```bash
  nix develop
  ```
* **Executar o jogo localmente para teste:**
  ```bash
  renpy .
  ```
* **Verificar sintaxe do Ren'Py sem abrir a janela gráfica:**
  ```bash
  renpy . lint
  ```

---

## 🌿 3. Diretrizes de Git Flow
* **Branch Padrão de Trabalho:** `develop` (a `main` é reservada exclusivamente para entregas e releases estáveis).
* **Criação de Branches:** Sempre criar a partir de `develop`:
  * `feat/<nome>` — Novas funcionalidades, minigames, telas ou casos clínicos.
  * `fix/<nome>` — Correções de bugs ou ajustes em cálculos de dose/regras.
  * `style/<nome>` — Atualização de sprites, radiografias e temas visuais.
  * `docs/<nome>` — Documentação e guias de estudo.
* **Padrão de Commits:** Utilizar o padrão de Conventional Commits em português (ex: `feat(uc1): adicionar calculo de kv`).
* *Consulte [`GIT_FLOW.md`](file:///home/henrique/Modelos/plantao-de-raios-x/GIT_FLOW.md) para o fluxo detalhado.*

---

## 📂 4. Mapa da Estrutura de Código
* `game/script.rpy` — Ponto de entrada e menu de seleção de modos.
* `game/modos/modo_estagio.rpy` — Fluxo do estágio supervisionado com o protagonista Ravi.
* `game/modos/modo_estudo_uc.rpy` — Hub de seleção das UCs.
* `game/ucs/` — Módulos individuais por disciplina (`uc1/`, `uc2/`, `uc6/`).
* `game/minigames/` — Módulos de lógica em Python e telas customizadas de minigames.
* `game/quiz/` — Quizzes e validação de pedidos médicos e posicionamentos.
* `game/personagens.rpy` — Definições de personagens e estilos de diálogos.
* `game/assets/` — Backgrounds, sprites de personagens, imagens de raio X e UI.

---

## 📖 5. Documentos de Referência
* **Regras pedagógicas, casos clínicos e pontuação:** Consulte [`GDD.md`](file:///home/henrique/Modelos/plantao-de-raios-x/GDD.md).
* **Processos de branches e releases:** Consulte [`GIT_FLOW.md`](file:///home/henrique/Modelos/plantao-de-raios-x/GIT_FLOW.md).
* **Instruções gerais:** Consulte [`README.md`](file:///home/henrique/Modelos/plantao-de-raios-x/README.md).
