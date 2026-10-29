## ==============================================================================
## FERRAMENTA DE CALIBRAÇÃO VISUAL DE SPRITES (Supervisora Cláudia)
## Cada expressão possui calibração INDIVIDUAL de X-Offset, Y-Offset e Zoom.
## Ajustar uma expressão NÃO altera as outras.
## ==============================================================================

init python:
    # Estrutura de dados com offsets e zoom individuais por pose
    if "calib_poses" not in globals():
        calib_poses = {
            "sorrindo":   {"x": 0, "y": 420, "zoom": 1.25},
            "explicando": {"x": 0, "y": 420, "zoom": 1.25},
            "preocupada": {"x": 0, "y": 420, "zoom": 1.25},
            "pensativa":  {"x": 0, "y": 420, "zoom": 1.25},
            "brava":      {"x": 0, "y": 420, "zoom": 1.25},
        }

    def calib_get_x(pose):
        return calib_poses.get(pose, {}).get("x", 0)

    def calib_get_y(pose):
        return calib_poses.get(pose, {}).get("y", 420)

    def calib_get_zoom(pose):
        return calib_poses.get(pose, {}).get("zoom", 1.25)

    def calib_mod_x(pose, delta):
        if pose in calib_poses:
            calib_poses[pose]["x"] += delta
            renpy.restart_interaction()

    def calib_mod_y(pose, delta):
        if pose in calib_poses:
            calib_poses[pose]["y"] += delta
            renpy.restart_interaction()

    def calib_mod_zoom(pose, delta):
        if pose in calib_poses:
            calib_poses[pose]["zoom"] = round(calib_poses[pose]["zoom"] + delta, 3)
            renpy.restart_interaction()

    def calib_reset_pose(pose):
        if pose in calib_poses:
            calib_poses[pose]["x"] = 0
            calib_poses[pose]["y"] = 420
            calib_poses[pose]["zoom"] = 1.25
            renpy.restart_interaction()

default calib_modo = "sobreposto"            # "sobreposto" ou "lado_a_lado"
default calib_expressao = "sorrindo"         # Expressão ativa sendo calibrada
default calib_normal_x = 3
default calib_normal_y = 420
default calib_normal_zoom = 1.25
default calib_base_xpos = 1480
default calib_base_ypos = 1080
default calib_alpha_normal = 0.6
default calib_alpha_exp = 0.6
default calib_ver_todas_codigo = False

label tela_calibrador:
    scene bg sala_exame with dissolve
    call screen calibrador_screen
    jump menu_selecao_modo

screen calibrador_screen():
    tag menu

    # --------------------------------------------------------------------------
    # 1. VISUALIZAÇÃO DOS SPRITES
    # --------------------------------------------------------------------------

    if calib_modo == "lado_a_lado":
        add "#000000bb"

        text "Visualização de Todas as 6 Poses Lado a Lado (com ajustes individuais)":
            xalign 0.5
            ypos 25
            size 28
            bold True
            color "#1abc9c"

        # Linha horizontal guia de base
        add Solid("#e74c3c", xsize=1900, ysize=3):
            xalign 0.5
            ypos 980

        text "▲ Linha de base dos pés (Y = 1080)":
            xalign 0.5
            ypos 990
            size 18
            color "#e74c3c"

        hbox:
            align (0.5, 0.88)
            spacing 25

            # Normal
            vbox:
                xalign 0.5
                spacing 4
                text "Normal":
                    xalign 0.5 size 20 bold True color "#3498db"
                text "x:[calib_normal_x] y:[calib_normal_y] z:[calib_normal_zoom:.2f]":
                    xalign 0.5 size 13 color "#bdc3c7"
                add "assets/sprites/claudia_normal.png":
                    zoom (calib_normal_zoom * 0.48)
                    xoffset calib_normal_x
                    yoffset (calib_normal_y * 0.48)

            # Sorrindo
            $ s_x = calib_get_x("sorrindo")
            $ s_y = calib_get_y("sorrindo")
            $ s_z = calib_get_zoom("sorrindo")
            vbox:
                xalign 0.5
                spacing 4
                text "Sorrindo":
                    xalign 0.5 size 20 bold True color "#2ecc71"
                text "x:[s_x] y:[s_y] z:[s_z:.2f]":
                    xalign 0.5 size 13 color "#bdc3c7"
                add "assets/sprites/claudia_sorrindo.png":
                    zoom (s_z * 0.48)
                    xoffset s_x
                    yoffset (s_y * 0.48)

            # Explicando
            $ e_x = calib_get_x("explicando")
            $ e_y = calib_get_y("explicando")
            $ e_z = calib_get_zoom("explicando")
            vbox:
                xalign 0.5
                spacing 4
                text "Explicando":
                    xalign 0.5 size 20 bold True color "#f39c12"
                text "x:[e_x] y:[e_y] z:[e_z:.2f]":
                    xalign 0.5 size 13 color "#bdc3c7"
                add "assets/sprites/claudia_explicando.png":
                    zoom (e_z * 0.48)
                    xoffset e_x
                    yoffset (e_y * 0.48)

            # Preocupada
            $ p_x = calib_get_x("preocupada")
            $ p_y = calib_get_y("preocupada")
            $ p_z = calib_get_zoom("preocupada")
            vbox:
                xalign 0.5
                spacing 4
                text "Preocupada":
                    xalign 0.5 size 20 bold True color "#e74c3c"
                text "x:[p_x] y:[p_y] z:[p_z:.2f]":
                    xalign 0.5 size 13 color "#bdc3c7"
                add "assets/sprites/claudia_preocupada.png":
                    zoom (p_z * 0.48)
                    xoffset p_x
                    yoffset (p_y * 0.48)

            # Pensativa
            $ pe_x = calib_get_x("pensativa")
            $ pe_y = calib_get_y("pensativa")
            $ pe_z = calib_get_zoom("pensativa")
            vbox:
                xalign 0.5
                spacing 4
                text "Pensativa":
                    xalign 0.5 size 20 bold True color "#9b59b6"
                text "x:[pe_x] y:[pe_y] z:[pe_z:.2f]":
                    xalign 0.5 size 13 color "#bdc3c7"
                add "assets/sprites/claudia_pensativa.png":
                    zoom (pe_z * 0.48)
                    xoffset pe_x
                    yoffset (pe_y * 0.48)

            # Brava
            $ b_x = calib_get_x("brava")
            $ b_y = calib_get_y("brava")
            $ b_z = calib_get_zoom("brava")
            vbox:
                xalign 0.5
                spacing 4
                text "Brava":
                    xalign 0.5 size 20 bold True color "#e67e22"
                text "x:[b_x] y:[b_y] z:[b_z:.2f]":
                    xalign 0.5 size 13 color "#bdc3c7"
                add "assets/sprites/claudia_brava.png":
                    zoom (b_z * 0.48)
                    xoffset b_x
                    yoffset (b_y * 0.48)

    else:
        # MODO SOBREPOSTO (ONION-SKIN NO CENÁRIO DO JOGO)
        if calib_expressao == "todas":
            for pos_name in ["sorrindo", "explicando", "preocupada", "pensativa", "brava"]:
                $ cur_x = calib_get_x(pos_name)
                $ cur_y = calib_get_y(pos_name)
                $ cur_z = calib_get_zoom(pos_name)
                add ("assets/sprites/claudia_" + pos_name + ".png"):
                    xanchor 0.5
                    yanchor 1.0
                    xpos calib_base_xpos
                    ypos calib_base_ypos
                    zoom cur_z
                    xoffset cur_x
                    yoffset cur_y
                    alpha 0.30
        else:
            $ act_x = calib_get_x(calib_expressao)
            $ act_y = calib_get_y(calib_expressao)
            $ act_z = calib_get_zoom(calib_expressao)
            add ("assets/sprites/claudia_" + calib_expressao + ".png"):
                xanchor 0.5
                yanchor 1.0
                xpos calib_base_xpos
                ypos calib_base_ypos
                zoom act_z
                xoffset act_x
                yoffset act_y
                alpha calib_alpha_exp

        # Cláudia Normal sobreposta
        add "assets/sprites/claudia_normal.png":
            xanchor 0.5
            yanchor 1.0
            xpos calib_base_xpos
            ypos calib_base_ypos
            zoom calib_normal_zoom
            xoffset calib_normal_x
            yoffset calib_normal_y
            alpha calib_alpha_normal

    # --------------------------------------------------------------------------
    # 2. PAINEL DE CONTROLE E AJUSTE (Lado Esquerdo da Tela)
    # --------------------------------------------------------------------------
    frame:
        align (0.02, 0.02)
        xsize 660
        ysize 1030
        background "#111921f0"
        padding (16, 14)

        vbox:
            spacing 8

            text "🛠️ Calibrador de Sprites Individual":
                size 24
                bold True
                color "#1abc9c"

            # Alternar Modo de Visualização
            hbox:
                spacing 10
                text "Modo:" color "#ecf0f1" size 16 yalign 0.5
                textbutton "Sobreposto (Ajuste Fino)":
                    action SetVariable("calib_modo", "sobreposto")
                    text_color ("#1abc9c" if calib_modo == "sobreposto" else "#7f8c8d")
                textbutton "Lado a Lado (Todas)":
                    action SetVariable("calib_modo", "lado_a_lado")
                    text_color ("#1abc9c" if calib_modo == "lado_a_lado" else "#7f8c8d")

            # Seletor de Expressão Ativa
            text "Escolha a pose para calibrar com a Normal:" color "#ecf0f1" size 15 bold True
            grid 3 2:
                spacing 4
                textbutton "Sorrindo":
                    action SetVariable("calib_expressao", "sorrindo")
                    text_color ("#2ecc71" if calib_expressao == "sorrindo" else "#bdc3c7")
                textbutton "Explicando":
                    action SetVariable("calib_expressao", "explicando")
                    text_color ("#f39c12" if calib_expressao == "explicando" else "#bdc3c7")
                textbutton "Preocupada":
                    action SetVariable("calib_expressao", "preocupada")
                    text_color ("#e74c3c" if calib_expressao == "preocupada" else "#bdc3c7")
                textbutton "Pensativa":
                    action SetVariable("calib_expressao", "pensativa")
                    text_color ("#9b59b6" if calib_expressao == "pensativa" else "#bdc3c7")
                textbutton "Brava":
                    action SetVariable("calib_expressao", "brava")
                    text_color ("#e67e22" if calib_expressao == "brava" else "#bdc3c7")
                textbutton "Todas (Fantasma)":
                    action SetVariable("calib_expressao", "todas")
                    text_color ("#1abc9c" if calib_expressao == "todas" else "#bdc3c7")

            if calib_modo == "sobreposto":
                # Controle de Opacidade
                hbox:
                    spacing 6
                    text "Transp: Normal" color "#3498db" size 14 yalign 0.5
                    textbutton "100%":
                        action SetVariable("calib_alpha_normal", 1.0)
                    textbutton "60%":
                        action SetVariable("calib_alpha_normal", 0.6)
                    textbutton "30%":
                        action SetVariable("calib_alpha_normal", 0.3)
                    textbutton "0%":
                        action SetVariable("calib_alpha_normal", 0.0)

                hbox:
                    spacing 6
                    text "Transp: Expressão" color "#2ecc71" size 14 yalign 0.5
                    textbutton "100%":
                        action SetVariable("calib_alpha_exp", 1.0)
                    textbutton "60%":
                        action SetVariable("calib_alpha_exp", 0.6)
                    textbutton "30%":
                        action SetVariable("calib_alpha_exp", 0.3)
                    textbutton "0%":
                        action SetVariable("calib_alpha_exp", 0.0)

            # ------------------------------------------------------------------
            # PAINEL DA EXPRESSÃO ATIVA (AJUSTA SOMENTE ELA)
            # ------------------------------------------------------------------
            $ cur_pose = calib_expressao if calib_expressao != "todas" else "sorrindo"
            $ cur_pose_title = cur_pose.capitalize()
            $ cur_x_val = calib_get_x(cur_pose)
            $ cur_y_val = calib_get_y(cur_pose)
            $ cur_z_val = calib_get_zoom(cur_pose)

            frame:
                background "#1e2b37"
                padding (10, 8)
                xfill True
                vbox:
                    spacing 5
                    text "🟩 Pose Ativa: [cur_pose_title] (Ajuste Individual)":
                        color "#2ecc71"
                        size 17
                        bold True

                    # X-Offset
                    hbox:
                        spacing 6
                        text "X-Offset: [cur_x_val] px" color "#ffffff" size 15 xsize 160 yalign 0.5
                        textbutton "-10":
                            action Function(calib_mod_x, cur_pose, -10)
                        textbutton "-1":
                            action Function(calib_mod_x, cur_pose, -1)
                        textbutton "+1":
                            action Function(calib_mod_x, cur_pose, 1)
                        textbutton "+10":
                            action Function(calib_mod_x, cur_pose, 10)
                        textbutton "0":
                            action Function(calib_mod_x, cur_pose, -cur_x_val)

                    # Y-Offset
                    hbox:
                        spacing 6
                        text "Y-Offset: [cur_y_val] px" color "#ffffff" size 15 xsize 160 yalign 0.5
                        textbutton "-20":
                            action Function(calib_mod_y, cur_pose, -20)
                        textbutton "-5":
                            action Function(calib_mod_y, cur_pose, -5)
                        textbutton "+5":
                            action Function(calib_mod_y, cur_pose, 5)
                        textbutton "+20":
                            action Function(calib_mod_y, cur_pose, 20)
                        textbutton "420":
                            action Function(calib_mod_y, cur_pose, 420 - cur_y_val)

                    # Zoom
                    hbox:
                        spacing 6
                        text "🔍 Zoom: [cur_z_val:.3f]" color "#ffffff" size 15 xsize 160 yalign 0.5
                        textbutton "-0.02":
                            action Function(calib_mod_zoom, cur_pose, -0.02)
                        textbutton "-0.005":
                            action Function(calib_mod_zoom, cur_pose, -0.005)
                        textbutton "+0.005":
                            action Function(calib_mod_zoom, cur_pose, 0.005)
                        textbutton "+0.02":
                            action Function(calib_mod_zoom, cur_pose, 0.02)
                        textbutton "1.25":
                            action Function(calib_reset_pose, cur_pose)

            # ------------------------------------------------------------------
            # PAINEL DA CLÁUDIA NORMAL (REFERÊNCIA)
            # ------------------------------------------------------------------
            frame:
                background "#1e2b37"
                padding (10, 8)
                xfill True
                vbox:
                    spacing 5
                    text "🟦 Cláudia Normal (pos_claudia_normal)":
                        color "#3498db"
                        size 17
                        bold True

                    # X-Offset
                    hbox:
                        spacing 6
                        text "X-Offset: [calib_normal_x] px" color "#ffffff" size 15 xsize 160 yalign 0.5
                        textbutton "-10":
                            action SetVariable("calib_normal_x", calib_normal_x - 10)
                        textbutton "-1":
                            action SetVariable("calib_normal_x", calib_normal_x - 1)
                        textbutton "+1":
                            action SetVariable("calib_normal_x", calib_normal_x + 1)
                        textbutton "+10":
                            action SetVariable("calib_normal_x", calib_normal_x + 10)
                        textbutton "3":
                            action SetVariable("calib_normal_x", 3)

                    # Y-Offset
                    hbox:
                        spacing 6
                        text "Y-Offset: [calib_normal_y] px" color "#ffffff" size 15 xsize 160 yalign 0.5
                        textbutton "-20":
                            action SetVariable("calib_normal_y", calib_normal_y - 20)
                        textbutton "-5":
                            action SetVariable("calib_normal_y", calib_normal_y - 5)
                        textbutton "+5":
                            action SetVariable("calib_normal_y", calib_normal_y + 5)
                        textbutton "+20":
                            action SetVariable("calib_normal_y", calib_normal_y + 20)
                        textbutton "420":
                            action SetVariable("calib_normal_y", 420)

                    # Zoom
                    hbox:
                        spacing 6
                        text "🔍 Zoom: [calib_normal_zoom:.3f]" color "#ffffff" size 15 xsize 160 yalign 0.5
                        textbutton "-0.02":
                            action SetVariable("calib_normal_zoom", calib_normal_zoom - 0.02)
                        textbutton "-0.005":
                            action SetVariable("calib_normal_zoom", calib_normal_zoom - 0.005)
                        textbutton "+0.005":
                            action SetVariable("calib_normal_zoom", calib_normal_zoom + 0.005)
                        textbutton "+0.02":
                            action SetVariable("calib_normal_zoom", calib_normal_zoom + 0.02)
                        textbutton "1.25":
                            action SetVariable("calib_normal_zoom", 1.25)

            # ------------------------------------------------------------------
            # PAINEL GLOBAL (TELA)
            # ------------------------------------------------------------------
            frame:
                background "#1e2b37"
                padding (8, 6)
                xfill True
                vbox:
                    spacing 4
                    text "⚙️ Posição Global na Tela (Base)":
                        color "#f39c12"
                        size 15
                        bold True

                    hbox:
                        spacing 6
                        text "X-Pos: [calib_base_xpos]" color "#ffffff" size 14 xsize 140 yalign 0.5
                        textbutton "-20":
                            action SetVariable("calib_base_xpos", calib_base_xpos - 20)
                        textbutton "-5":
                            action SetVariable("calib_base_xpos", calib_base_xpos - 5)
                        textbutton "+5":
                            action SetVariable("calib_base_xpos", calib_base_xpos + 5)
                        textbutton "+20":
                            action SetVariable("calib_base_xpos", calib_base_xpos + 20)

                    hbox:
                        spacing 6
                        text "Y-Pos: [calib_base_ypos]" color "#ffffff" size 14 xsize 140 yalign 0.5
                        textbutton "-20":
                            action SetVariable("calib_base_ypos", calib_base_ypos - 20)
                        textbutton "-5":
                            action SetVariable("calib_base_ypos", calib_base_ypos - 5)
                        textbutton "+5":
                            action SetVariable("calib_base_ypos", calib_base_ypos + 5)
                        textbutton "+20":
                            action SetVariable("calib_base_ypos", calib_base_ypos + 20)

            # ------------------------------------------------------------------
            # CÓDIGO GERADO PRONTO PARA COPIAR
            # ------------------------------------------------------------------
            frame:
                background "#16222f"
                padding (10, 8)
                xfill True
                vbox:
                    spacing 3
                    hbox:
                        text "📋 Código para personagens.rpy:":
                            size 14
                            color "#bdc3c7"
                            bold True
                            yalign 0.5
                        null width 15
                        textbutton ("Mostrar Todas" if not calib_ver_todas_codigo else "Mostrar Ativa"):
                            action ToggleVariable("calib_ver_todas_codigo")
                            text_size 13
                            text_color "#1abc9c"

                    if not calib_ver_todas_codigo:
                        text "pos_claudia_[cur_pose]:":
                            size 13 bold True color "#2ecc71"
                        text "    zoom [cur_z_val:.2f] | xoffset [cur_x_val] | yoffset [cur_y_val]":
                            size 13 color "#ecf0f1"
                    else:
                        text "normal: x=[calib_normal_x] y=[calib_normal_y] z=[calib_normal_zoom:.2f]":
                            size 12 color "#3498db"
                        for p in ["sorrindo", "explicando", "preocupada", "pensativa", "brava"]:
                            $ px = calib_get_x(p)
                            $ py = calib_get_y(p)
                            $ pz = calib_get_zoom(p)
                            text "[p]: x=[px] y=[py] z=[pz:.2f]":
                                size 12 color "#2ecc71"

            # Botão Voltar
            textbutton "↩️ Voltar ao Menu Principal":
                action Return()
                xalign 0.5
                text_size 20
                text_color "#e74c3c"
