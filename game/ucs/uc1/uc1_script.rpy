## Módulo UC 1: Preparar Equipamentos e Acessórios para Exames Convencionais
# Foco: Biossegurança, Higienização da Sala e Fatores de Exposição (kV / mAs)

label uc1_start:
    scene black with fade

    narrador "--- MÓDULO PRÁTICO: UC 1 ---"
    narrador "{b}Preparar Equipamentos e Acessórios para a Realização de Exames Radiológicos Convencionais{/b} (108h)"
    
    claudia "Olá! Seja bem-vindo ao módulo de treino da {b}UC 1{/b}."
    claudia "Aqui você vai praticar a rotina inicial de biossegurança, checklist de equipamentos e a calibração dos fatores de exposição (kV e mAs)."
    
    # Início direto da atividade prática da UC1
    narrador "Iniciando a preparação da sala de exames..."

    # Próxima etapa da UC1 será inserida aqui
    narrador "(O minigame de higienização e a calculadora de kV/mAs serão executados aqui em sequência)."

    claudia "Parabéns por concluir o treino da UC 1!"

    menu:
        "🔄 Repetir o Treino da UC 1":
            jump uc1_start
        "📚 Voltar à Seleção de UCs":
            jump iniciar_modo_estudo_uc
        "🏠 Menu Principal":
            jump menu_selecao_modo
