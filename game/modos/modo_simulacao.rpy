## Modo Simulação: Plantão com o Ravi no Hospital Santa Magnólia

label iniciar_modo_simulacao:
    scene black with fade

    narrador "Segunda-feira, 07:45 da manhã."
    narrador "Você é {b}Ravi{/b}, estagiário no setor de radiologia do Hospital Santa Magnólia."

    claudia "Bom dia, Ravi! Preparado para o seu primeiro caso do plantão?"
    ravi "Bom dia, Dra. Cláudia! Tudo pronto por aqui."
    claudia "Lembre-se da nossa regra de ouro: {i}Na radiologia, capricho não é perfeccionismo — é proteção.{/i}"
    claudia "Vamos atender os pacientes do dia seguindo o nosso protocolo de 6 etapas."

    # Inicia a sequência de casos clínicos
    jump caso1_inicio

label caso1_inicio:
    narrador "--- CASO CLÍNICO 1: SEU BENEDITO (72 ANOS) ---"
    narrador "Você acabou de receber o pedido médico na recepção..."

    # Placeholder para as etapas completas do caso 1
    narrador "(O fluxo completo do Caso 1 será conectado aqui: Higienização, Pedido, Parâmetros, Anamnese, Posicionamento e Imagem)."

    claudia "Muito bem, Ravi! Vamos revisar os resultados."
    
    menu:
        "Voltar ao Menu Principal":
            jump menu_selecao_modo
        "Finalizar por hoje":
            return
