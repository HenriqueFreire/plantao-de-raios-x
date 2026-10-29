## Script Principal - Plantão de Raios-X

# Variáveis globais do sistema de pontuação e estado
default pontuacao_total = 0
default caso_atual = 1
default modo_escolhido = ""

label start:
    scene black with dissolve

    narrador "Bem-vindo ao {b}Plantão de Raios-X{/b}!"
    narrador "Um simulador e jogo educativo desenvolvido para o curso Técnico em Radiologia do Senac."

    jump menu_selecao_modo

label menu_selecao_modo:
    scene black with dissolve

    menu:
        narrador "Escolha como deseja jogar hoje:"

        "📚 Modo Estudo — Escolher por Unidade Curricular (UC)":
            $ modo_escolhido = "estudo_uc"
            jump iniciar_modo_estudo_uc

        "🏥 Modo Estágio — Iniciar Plantão Supervisionado com o Ravi":
            $ modo_escolhido = "estagio"
            jump iniciar_modo_estagio

        "🛠️ Calibrador Visual de Sprites (Ajustar Posições)":
            jump tela_calibrador

        "ℹ️ Sobre o Projeto Integrador":
            jump tela_sobre

        "🚪 Sair":
            return

label tela_sobre:
    narrador "{b}Plantão de Raios-X — Projeto Integrador{/b}\nCurso Técnico em Radiologia — Senac Campinas."
    narrador "Objetivo: Simular o atendimento radiológico humanizado e a tomada de decisões técnicas com base nas normas da CNEN e ANVISA."
    narrador "Desenvolvido com Ren'Py e Python."
    jump menu_selecao_modo
