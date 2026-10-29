## Definições de Personagens e Assets Visuais do Jogo

define ravi = Character("Ravi (Você)", color="#3498db", who_bold=True)
define claudia = Character("Supervisora Cláudia", image="claudia", color="#2ecc71", who_bold=True)
define narrador = Character(None, what_italic=True)

# Pacientes
define benedito = Character("Seu Benedito", color="#e67e22", who_bold=True)
define julia = Character("Júlia", color="#9b59b6", who_bold=True)
define marcos = Character("Marcos", color="#e74c3c", who_bold=True)
define tereza = Character("Dona Tereza", color="#1abc9c", who_bold=True)
define pedro = Character("Pedro", color="#f1c40f", who_bold=True)
define mae_pedro = Character("Mãe do Pedro", color="#d35400", who_bold=True)

## Declaração de Imagens de Cenário (1920x1080)
image bg hospital_externo = "assets/backgrounds/bg_hospital_externo.png"
image bg sala_espera = "assets/backgrounds/bg_sala_espera.png"
image bg sala_exame = "assets/backgrounds/bg_sala_exame.png"
image bg biombo = "assets/backgrounds/bg_biombo.png"

## Posições Personalizadas (ATL Transforms)

# 1. Cláudia Normal
transform pos_claudia_normal:
    xanchor 0.5
    yanchor 1.0
    xpos 1480
    ypos 1080
    zoom 1.25
    xoffset 3
    yoffset 420

# 2. Cláudia Sorrindo
transform pos_claudia_sorrindo:
    xanchor 0.5
    yanchor 1.0
    xpos 1480
    ypos 1080
    zoom 0.82
    xoffset 0
    yoffset 170

# 3. Cláudia Explicando
transform pos_claudia_explicando:
    xanchor 0.5
    yanchor 1.0
    xpos 1480
    ypos 1080
    zoom 1.25
    xoffset 0
    yoffset 420

# 4. Cláudia Preocupada
transform pos_claudia_preocupada:
    xanchor 0.5
    yanchor 1.0
    xpos 1480
    ypos 1080
    zoom 1.25
    xoffset 0
    yoffset 420

# 5. Cláudia Pensativa
transform pos_claudia_pensativa:
    xanchor 0.5
    yanchor 1.0
    xpos 1480
    ypos 1080
    zoom 1.25
    xoffset 0
    yoffset 420

# 6. Cláudia Brava
transform pos_claudia_brava:
    xanchor 0.5
    yanchor 1.0
    xpos 1480
    ypos 1080
    zoom 1.25
    xoffset 0
    yoffset 420

# Aliases de compatibilidade para código existente
transform pos_claudia_expressoes:
    pos_claudia_sorrindo

transform pos_claudia:
    pos_claudia_normal

transform pos_paciente:
    zoom 0.80
    xanchor 0.5
    yanchor 1.0
    xpos 450
    ypos 1080
    xoffset 0
    yoffset 0

## Declaração de Sprites da Dra. Cláudia (Manager)
# Cada sprite usa apenas o arquivo de imagem; o posicionamento é feito pelos transforms acima.
image claudia normal = "assets/sprites/claudia_normal.png"
image claudia sorrindo = "assets/sprites/claudia_sorrindo.png"
image claudia explicando = "assets/sprites/claudia_explicando.png"
image claudia preocupada = "assets/sprites/claudia_preocupada.png"
image claudia pensativa = "assets/sprites/claudia_pensativa.png"
image claudia brava = "assets/sprites/claudia_brava.png"
