# Telas do Jogo Plantão de Raios-X

screen main_menu():
    tag menu

    # Fundo hospitalar / azul petróleo escuro
    add "#1a252f"

    vbox:
        align (0.5, 0.45)
        spacing 25

        text "🏥 Plantão de Raios-X":
            size 75
            color "#ecf0f1"
            xalign 0.5

        text "Projeto Integrador — Técnico em Radiologia (Senac)":
            size 28
            color "#1abc9c"
            xalign 0.5

        null height 30

        textbutton "▶️ Iniciar Jogo":
            action Start()
            text_size 38
            text_idle_color "#bdc3c7"
            text_hover_color "#3498db"
            xalign 0.5

        textbutton "🚪 Sair":
            action Quit(confirm=True)
            text_size 32
            text_idle_color "#7f8c8d"
            text_hover_color "#e74c3c"
            xalign 0.5

# Tela de confirmação simples para o Sair
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    add "#000000aa"

    frame:
        align (0.5, 0.5)
        padding (50, 40)
        background "#2c3e50"

        vbox:
            spacing 30
            text message:
                xalign 0.5
                color "#ffffff"
                size 30

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
