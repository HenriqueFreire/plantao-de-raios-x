# Telas e Interface do Jogo Plantão de Raios-X

## 1. Menu Inicial
screen main_menu():
    tag menu
    add "#1a252f" # Fundo escuro elegante

    vbox:
        align (0.5, 0.45)
        spacing 25

        text "🏥 Plantão de Raios-X":
            size 75
            color "#ecf0f1"
            xalign 0.5

        text "Projeto Integrador — Técnico em Radiologia (Senac Campinas)":
            size 26
            color "#1abc9c"
            xalign 0.5

        null height 35

        textbutton "▶️ Iniciar Jogo":
            action Start()
            text_size 36
            text_idle_color "#bdc3c7"
            text_hover_color "#3498db"
            xalign 0.5

        textbutton "🚪 Sair":
            action Quit(confirm=True)
            text_size 30
            text_idle_color "#7f8c8d"
            text_hover_color "#e74c3c"
            xalign 0.5

## 2. Tela de Diálogos e Falas (Say Screen)
screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        align (0.5, 0.95)
        xsize 1500
        ysize 220
        background "#111921dd"
        padding (40, 25)

        vbox:
            spacing 10
            if who is not None:
                text who id "who":
                    size 28
                    bold True
            text what id "what":
                size 24
                color "#ffffff"

## 3. Tela de Escolhas / Menus de Decisão (Choice Screen)
screen choice(items):
    style_prefix "choice"

    vbox:
        align (0.5, 0.5)
        spacing 18

        for i in items:
            if i.action:
                button:
                    action i.action
                    xalign 0.5
                    xsize 1100
                    background "#2c3e50"
                    hover_background "#34495e"
                    padding (25, 14)
                    text i.caption:
                        xalign 0.5
                        text_align 0.5
                        size 24
                        color "#ecf0f1"
                        hover_color "#1abc9c"
            else:
                # Legenda/Título da pergunta do menu (quando não é botão)
                text i.caption:
                    xalign 0.5
                    text_align 0.5
                    size 30
                    bold True
                    color "#1abc9c"
                    bottom_margin 25

## 4. Tela de Confirmação (Sair, etc.)
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    add "#000000bb"

    frame:
        align (0.5, 0.5)
        padding (50, 40)
        background "#2c3e50"

        vbox:
            spacing 30
            text message:
                xalign 0.5
                color "#ffffff"
                size 28

            hbox:
                spacing 80
                xalign 0.5
                textbutton "Sim":
                    action yes_action
                    text_color "#2ecc71"
                    text_size 28
                textbutton "Não":
                    action no_action
                    text_color "#e74c3c"
                    text_size 28
