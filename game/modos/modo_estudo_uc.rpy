## Modo Estudo: Seleção por Unidade Curricular (UC)

label iniciar_modo_estudo_uc:
    scene black with dissolve

    menu:
        narrador "Selecione a Unidade Curricular que você deseja estudar:"

        "🧪 UC 1 — Higienização, Biossegurança e Parâmetros Técnicos (kV/mAs)":
            jump uc1_start

        "🦴 UC 2 — Anatomia Radiológica e Posicionamento de Extremidades":
            jump menu_uc2

        "🛡️ UC 6 — Proteção Radiológica e Legislação (CNEN / ANVISA)":
            jump menu_uc6

        "↩️ Voltar ao Menu Principal":
            jump menu_selecao_modo
