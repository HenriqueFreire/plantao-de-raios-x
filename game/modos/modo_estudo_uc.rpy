## Modo Estudo: Seleção por Unidade Curricular (UC)
## Suporte a Progresso Persistente com Estrelas (⭐⭐⭐)

default persistent.uc1_estrelas = 0
default persistent.uc1_concluida = False
default persistent.uc2_estrelas = 0
default persistent.uc2_concluida = False
default persistent.uc6_estrelas = 0
default persistent.uc6_concluida = False

label iniciar_modo_estudo_uc:
    scene bg sala_exame with dissolve

    $ uc1_badge = " ⭐" * persistent.uc1_estrelas if persistent.uc1_estrelas > 0 else ""
    $ uc2_badge = " ⭐" * persistent.uc2_estrelas if persistent.uc2_estrelas > 0 else ""
    $ uc6_badge = " ⭐" * persistent.uc6_estrelas if persistent.uc6_estrelas > 0 else ""

    menu:
        narrador "Selecione a Unidade Curricular que você deseja estudar e praticar:"

        "🧪 UC 1 — Física das Radiações, Equipamentos & Biossegurança [uc1_badge]":
            jump uc1_start

        "🦴 UC 2 — Anatomia Radiológica e Posicionamento de Extremidades [uc2_badge]":
            jump menu_uc2

        "🛡️ UC 6 — Proteção Radiológica e Legislação (CNEN / ANVISA) [uc6_badge]":
            jump menu_uc6

        "↩️ Voltar ao Menu Principal":
            jump menu_selecao_modo
