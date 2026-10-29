# Telas e Interface do Jogo Plantão de Raios-X
# Suporte a Menus, Diálogos, Escolhas, Save/Load e Quick Menu

## 1. Menu Inicial
screen main_menu():
    tag menu
    add "assets/backgrounds/bg_sala_exame.jpg"
    add "#00000088" # Overlay escuro para destacar o texto

    vbox:
        align (0.5, 0.45)
        spacing 25

        text "🏥 Plantão de Raios-X":
            size 75
            color "#ecf0f1"
            outlines [(3, "#111921", 0, 0)]
            xalign 0.5

        text "Projeto Integrador — Técnico em Radiologia (Senac Campinas)":
            size 26
            color "#1abc9c"
            outlines [(2, "#111921", 0, 0)]
            xalign 0.5

        null height 25

        textbutton "▶️ Iniciar Jogo":
            action Start()
            text_size 36
            text_idle_color "#ecf0f1"
            text_hover_color "#3498db"
            xalign 0.5

        textbutton "📂 Carregar Jogo":
            action ShowMenu("load")
            text_size 32
            text_idle_color "#bdc3c7"
            text_hover_color "#2ecc71"
            xalign 0.5

        textbutton "🚪 Sair":
            action Quit(confirm=True)
            text_size 28
            text_idle_color "#7f8c8d"
            text_hover_color "#e74c3c"
            xalign 0.5

## 2. Tela de Diálogos e Falas (Say Screen)
screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        align (0.5, 0.96)
        xsize 1550
        ysize 210
        background "#111921e6"
        padding (45, 20)

        vbox:
            spacing 8
            if who is not None:
                text who id "who":
                    size 28
                    bold True
            text what id "what":
                size 24
                color "#ffffff"

    use quick_menu

## 3. Quick Menu (Barra Rápida de Ações)
screen quick_menu():
    zorder 100
    hbox:
        align (0.5, 0.99)
        spacing 25

        textbutton "↩️ Voltar":
            action Rollback()
            text_size 16
            text_idle_color "#95a5a6"
            text_hover_color "#3498db"

        textbutton "💾 Salvar":
            action ShowMenu("save")
            text_size 16
            text_idle_color "#95a5a6"
            text_hover_color "#2ecc71"

        textbutton "📂 Carregar":
            action ShowMenu("load")
            text_size 16
            text_idle_color "#95a5a6"
            text_hover_color "#2ecc71"

        textbutton "⚡ Q.Save":
            action QuickSave()
            text_size 16
            text_idle_color "#95a5a6"
            text_hover_color "#f39c12"

        textbutton "⚡ Q.Load":
            action QuickLoad()
            text_size 16
            text_idle_color "#95a5a6"
            text_hover_color "#f39c12"

        textbutton "🏠 Menu":
            action MainMenu()
            text_size 16
            text_idle_color "#95a5a6"
            text_hover_color "#e74c3c"

## 4. Tela de Escolhas / Menus de Decisão (Choice Screen)
screen choice(items):
    style_prefix "choice"

    vbox:
        align (0.5, 0.5)
        spacing 16

        for i in items:
            if i.action:
                button:
                    action i.action
                    xalign 0.5
                    xsize 1150
                    background "#2c3e50"
                    hover_background "#16a085"
                    padding (25, 14)
                    text i.caption:
                        xalign 0.5
                        text_align 0.5
                        size 24
                        color "#ecf0f1"
                        hover_color "#ffffff"
            else:
                text i.caption:
                    xalign 0.5
                    text_align 0.5
                    size 30
                    bold True
                    color "#1abc9c"
                null height 10

## 5. Telas de Save e Load
screen save():
    tag menu
    use file_slots(_("💾 Salvar Jogo"))

screen load():
    tag menu
    use file_slots(_("📂 Carregar Jogo"))

screen file_slots(title):
    add "assets/backgrounds/bg_sala_exame.jpg"
    add "#000000cc"

    vbox:
        align (0.5, 0.05)
        spacing 15

        text title:
            size 42
            color "#1abc9c"
            bold True
            xalign 0.5

        null height 10

        grid 3 2:
            xalign 0.5
            spacing 25

            for i in range(1, 7):
                $ slot = i
                button:
                    action FileAction(slot)
                    xsize 380
                    ysize 220
                    background "#2c3e50"
                    hover_background "#34495e"
                    padding (15, 15)

                    vbox:
                        spacing 6
                        xalign 0.5

                        text "Slot [slot]":
                            size 20
                            bold True
                            color "#ecf0f1"
                            xalign 0.5

                        add FileScreenshot(slot) xalign 0.5

                        $ file_time = FileTime(slot, format=_("%d/%m/%Y %H:%M"), empty=_("Slot Vazio"))
                        text "[file_time]":
                            size 16
                            color "#bdc3c7"
                            xalign 0.5

        null height 20

        textbutton "↩️ Voltar":
            action Return()
            text_size 28
            text_idle_color "#bdc3c7"
            text_hover_color "#e74c3c"
            xalign 0.5

## 6. Tela de Confirmação (Sair, etc.)
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
