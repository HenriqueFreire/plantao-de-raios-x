## Módulo UC 1: Preparar Equipamentos e Acessórios para a Realização de Exames Radiológicos Convencionais (108h)
## Baseado nas Diretrizes Pedagógicas do Senac e Física Radiológica
## Integrado com Cenários, Sprites da Dra. Cláudia e Progresso Persistente (⭐⭐⭐)

default uc1_pontos = 0
default uc1_total = 0

label uc1_start:
    scene bg sala_exame with fade
    $ uc1_pontos = 0
    $ uc1_total = 0

    show claudia normal at pos_claudia_normal with dissolve
    narrador "--- MÓDULO PRÁTICO: UC 1 ---"
    narrador "{b}Preparar Equipamentos e Acessórios para a Realização de Exames Radiológicos Convencionais{/b} (108h)"
    
    claudia "Olá, Ravi! Seja muito bem-vindo ao módulo de aprofundamento da {b}UC 1{/b}."
    claudia "Na radiologia, operar o equipamento sem dominar a física e a biossegurança é como dirigir de olhos vendados."
    claudia "Aqui você vai dominar a ampola de raios-X, os fatores de exposição, a terminologia de posicionamento e as normas de proteção."

label uc1_menu_trilhas:
    scene bg sala_exame with dissolve
    show claudia normal at pos_claudia_normal with dissolve

    menu:
        narrador "Escolha a trilha de treino da UC 1 que deseja praticar:"

        "⚡ Trilha 1: Física das Radiações & Tubo de Raios-X":
            jump uc1_trilha_fisica

        "📐 Trilha 2: Terminologia Anatômica, Planos & Acessórios":
            jump uc1_trilha_terminologia

        "🎛️ Trilha 3: Fatores Técnicos, Compensações & Cálculos (kV/mAs)":
            jump uc1_trilha_fatores

        "🧼 Trilha 4: Biossegurança, Higienização, EPIs & Ética":
            jump uc1_trilha_biosseguranca

        "📝 Simulado Completo Integrado da UC 1 (Desafio Geral)":
            jump uc1_simulado_completo

        "📚 Voltar à Seleção de UCs":
            jump iniciar_modo_estudo_uc

        "🏠 Menu Principal":
            jump menu_selecao_modo


# ==============================================================================
# TRILHA 1: FÍSICA DAS RADIAÇÕES & TUBO DE RAIOS-X
# ==============================================================================
label uc1_trilha_fisica:
    scene bg biombo with dissolve
    show claudia normal at pos_claudia_normal with dissolve
    narrador "--- TRILHA 1: FÍSICA DAS RADIAÇÕES & TUBO DE RAIOS-X ---"
    
    claudia "Vamos revisar a física do feixe. Lembre-se: dentro da ampola de vidro a vácuo ocorrem transformações energéticas intensas."
    claudia "O filamento de tungstênio no cátodo é aquecido por uma corrente, liberando elétrons na chamada {b}emissão termoiônica{/b}."
    claudia "Quando aplicamos a alta tensão (kVp), esses elétrons são acelerados violentamente em direção ao ânodo de tungstênio."
    claudia "Cerca de {b}99%%{/b} dessa energia cinética vira calor, e apenas {b}1%%{/b} é convertida em raios-X!"

    # Questão 1: Componentes da Ampola
    $ uc1_total += 1
    narrador "Pergunta 1/4 — Anatomia do Tubo de Raios-X:"
    menu:
        claudia "Qual componente do tubo de raios-X atua como eletrodo negativo, responsável pela emissão de elétrons por efeito termoiônico?"

        "A) Ânodo giratório":
            claudia preocupada "Incorreto! O ânodo é o eletrodo positivo (alvo). O eletrodo negativo é o cátodo."
        
        "B) Cátodo (Filamento de tungstênio)":
            $ uc1_pontos += 1
            claudia sorrindo "Exato! O cátodo é o polo negativo onde o filamento é aquecido para liberar a nuvem de elétrons."
        
        "C) Colimador luminoso":
            claudia preocupada "Incorreto! O colimador fica fora da ampola e serve para delimitar o campo de radiação."
        
        "D) Filtro de alumínio":
            claudia preocupada "Incorreto! O filtro de alumínio serve para absorver fótons de baixa energia do feixe primário."

    # Questão 2: Mecanismos de Produção
    $ uc1_total += 1
    narrador "Pergunta 2/4 — Mecanismos de Produção do Raio-X:"
    menu:
        claudia normal "Na interação dos elétrons projéteis com o alvo de tungstênio, a radiação de freamento ({i}Bremsstrahlung{/i}) ocorre quando:"

        "A) O elétron remove um elétron da camada K do átomo de tungstênio.":
            claudia preocupada "Atenção! Arrancar elétrons de camadas internas gera a {b}Radiação Característica{/b}. A radiação de freamento é a desaceleração pelo campo nuclear."

        "B) O elétron projétil é desacelerado e desviado pela força atrativa do núcleo do átomo de tungstênio.":
            $ uc1_pontos += 1
            claudia sorrindo "Perfeito! Ao frear e desviar perto do núcleo, o elétron perde energia cinética na forma de fótons de raio X (espectro contínuo)."

        "C) Ocorre uma reação de fusão nuclear dentro da ampola.":
            claudia preocupada "Não! Não existe fusão ou fissão nuclear na ampola de diagnóstico."

        "D) O fóton é totalmente absorvido pelo filamento do cátodo.":
            claudia preocupada "Incorreto!"

    # Questão 3: Interação com a Matéria (Fotoelétrico vs Compton)
    $ uc1_total += 1
    narrador "Pergunta 3/4 — Interação do Feixe com o Paciente:"
    menu:
        claudia normal "Qual mecanismo de interação da radiação com o corpo do paciente é responsável pelo contraste radiográfico (absorção total no osso) e qual gera radiação espalhada (névoa e dose ocupacional)?"

        "A) Efeito Compton gera o contraste ósseo; Efeito Fotoelétrico gera o espalhamento.":
            claudia preocupada "Invertido! O {b}Fotoelétrico{/b} é absorção total (dá o branco/contraste do osso) e o {b}Compton{/b} é espalhamento (névoa e radiação secundária)."

        "B) Efeito Fotoelétrico gera absorção total (contraste); Efeito Compton gera radiação espalhada.":
            $ uc1_pontos += 1
            claudia sorrindo "Excelente! O Fotoelétrico garante o contraste das estruturas densas, enquanto o Compton ejeta um elétron externo e espalha o fóton com menor energia."

        "C) Radiação de freamento gera contraste; Termoiônico gera espalhamento.":
            claudia preocupada "Incorreto! Esses são processos de produção no tubo, não de interação com o paciente."

        "D) Apenas o efeito fotoelétrico ocorre no diagnóstico; o efeito Compton só ocorre na radioterapia.":
            claudia preocupada "Incorreto! O efeito Compton é o principal responsável pela radiação secundária e dose ocupacional no diagnóstico."

    # Questão 4: Efeito Anódico na Prática
    $ uc1_total += 1
    narrador "Pergunta 4/4 — Aplicação Prática do Efeito Anódico:"
    menu:
        claudia normal "Devido à geometria do alvo, a intensidade do feixe de raios-X é maior do lado do Cátodo e menor do lado do Ânodo ({i}Efeito Anódico{/i}). Como você deve posicionar o paciente em um exame de fêmur ou coluna?"

        "A) A parte anatômica mais espessa e densa deve ficar voltada para o lado do Cátodo.":
            $ uc1_pontos += 1
            claudia sorrindo "Certíssimo! Como o lado do cátodo emite mais intensidade, colocamos a parte mais grossa (ex: quadril/base da coxa) voltada para o cátodo para uniformizar a densidade da imagem!"

        "B) A parte mais espessa deve ficar voltada para o lado do Ânodo.":
            claudia preocupada "Cuidado! O lado do ânodo sofre autoatenuação (feixe mais fraco). Se colocar a parte grossa no ânodo, a imagem ficará subexposta nessa região."

        "C) O efeito anódico só se aplica a exames odontológicos.":
            claudia preocupada "Incorreto! O efeito anódico é relevante em qualquer estrutura longa de espessura assimétrica (fêmur, coluna torácica, tíbia)."

        "D) A orientação do tubo não afeta a intensidade da radiação.":
            claudia preocupada "Incorreto! A intensidade do feixe pode variar em até 45%% entre a extremidade do cátodo e a do ânodo."

    claudia sorrindo "Concluímos a Trilha 1! Pontuação parcial: [uc1_pontos]/[uc1_total]."
    jump uc1_menu_trilhas


# ==============================================================================
# TRILHA 2: TERMINOLOGIA ANATÔMICA, PLANOS & ACESSÓRIOS
# ==============================================================================
label uc1_trilha_terminologia:
    scene bg sala_exame with dissolve
    show claudia normal at pos_claudia_normal with dissolve
    narrador "--- TRILHA 2: TERMINOLOGIA ANATÔMICA, PLANOS & ACESSÓRIOS ---"

    claudia "Para posicionar com precisão e preparar os acessórios certos, a linguagem técnica deve estar na ponta da língua."

    # Questão 1: Planos Anatômicos
    $ uc1_total += 1
    narrador "Pergunta 1/4 — Planos do Corpo Humano:"
    menu:
        claudia "Qual plano anatômico divide o corpo em metades Direita e Esquerda, e qual divide em Porção Anterior (frente) e Posterior (trás)?"

        "A) Plano Coronal divide em direita/esquerda; Plano Sagital divide em anterior/posterior.":
            claudia preocupada "Invertido! Sagital divide em Direita/Esquerda; Coronal (Frontal) divide em Anterior/Posterior."

        "B) Plano Sagital divide em direita/esquerda; Plano Coronal (Frontal) divide em anterior/posterior.":
            $ uc1_pontos += 1
            claudia sorrindo "Perfeito! E o plano Transversal (Axial) divide o corpo em Superior e Inferior."

        "C) Plano Axial divide em direita/esquerda; Plano Sagital divide em ventral/dorsal.":
            claudia preocupada "Incorreto!"

        "D) Plano Sagital divide em superior/inferior; Plano Transversal em anterior/posterior.":
            claudia preocupada "Incorreto! Quem divide em superior e inferior é o plano transversal (ou axial)."

    # Questão 2: Direção do Feixe (AP vs PA)
    $ uc1_total += 1
    narrador "Pergunta 2/4 — Incidências Fundamentais:"
    menu:
        claudia normal "Em uma incidência Ântero-Posterior (AP), por onde o feixe de radiação entra e sai do paciente?"

        "A) Entra pela face posterior (costas) e sai pela anterior (frente).":
            claudia preocupada "Essa é a incidência Póstero-Anterior (PA), padrão para exames de tórax de rotina!"

        "B) Entra pela face anterior (frente) e sai pela face posterior (costas).":
            $ uc1_pontos += 1
            claudia sorrindo "Muito bem! Em AP o feixe penetra pela frente e sai por trás em direção ao receptor de imagem."

        "C) Entra pelo lado direito e sai pelo esquerdo.":
            claudia preocupada "Essa é uma incidência em Perfil (Lateral)!"

        "D) Entra longitudinalmente pelo ápice do crânio e sai pela pelve.":
            claudia preocupada "Incorreto! Essa seria uma incidência axial / crânio-caudal!"

    # Questão 3: Espessômetro e Goniômetro
    $ uc1_total += 1
    narrador "Pergunta 3/4 — Acessórios de Medição:"
    menu:
        claudia normal "Quais são as funções específicas do {b}Espessômetro{/b} e do {b}Goniômetro{/b} na rotina de preparo da sala?"

        "A) O Espessômetro mede a espessura da estrutura anatômica (em cm); o Goniômetro mede o ângulo de inclinação do raio central.":
            $ uc1_pontos += 1
            claudia sorrindo "Exatamente! O espessômetro é a régua em compasso usada para calcular o kV, e o goniômetro garante a angulação exata (ex: 15° cefálico)."

        "B) O Espessômetro mede o tempo de revelação; o Goniômetro mede a temperatura da sala.":
            claudia preocupada "Incorreto! São instrumentos de física geométrica aplicada ao paciente."

        "C) Ambos servem exclusivamente para cortar filmes radiográficos.":
            claudia preocupada "Incorreto!"

        "D) O Espessômetro mede a dose do dosímetro; o Goniômetro calcula a miliamperagem.":
            claudia preocupada "Incorreto! Dosímetro e miliamperímetro são instrumentos de física e proteção distintos."

    # Questão 4: Écrans e Divisores de Chumbo
    $ uc1_total += 1
    narrador "Pergunta 4/4 — Acessórios do Chassi:"
    menu:
        claudia normal "Qual é a função do {b}écran (tela intensificadora){/b} e do {b}divisor de chumbo{/b} no chassi convencional?"

        "A) O écran absorve a radiação espalhada; o divisor resfria o filme.":
            claudia preocupada "Incorreto! Quem absorve radiação espalhada é a grade antidifusora (Bucky)."

        "B) O écran converte raios-X em luz visível para reduzir drasticamente a dose de radiação no paciente; o divisor permite fazer mais de uma exposição no mesmo chassi.":
            $ uc1_pontos += 1
            claudia sorrindo "Brilhante! Mais de 95%% da exposição do filme convencional vem da luz fluorescente emitida pelos fósforos do écran, poupando o paciente de doses altas!"

        "C) O écran protege o filme contra fungos; o divisor aumenta o kVp.":
            claudia preocupada "Incorreto!"

        "D) O écran filtra o feixe de radiação primária; o divisor altera a miliamperagem do tubo.":
            claudia preocupada "Incorreto! A filtragem é feita por lâminas de alumínio e o controle elétrico fica no console."

    claudia sorrindo "Muito bem! Concluímos a Trilha 2. Pontuação acumulada: [uc1_pontos]/[uc1_total]."
    jump uc1_menu_trilhas


# ==============================================================================
# TRILHA 3: FATORES TÉCNICOS, COMPENSAÇÕES & CÁLCULOS
# ==============================================================================
label uc1_trilha_fatores:
    scene bg biombo with dissolve
    show claudia normal at pos_claudia_normal with dissolve
    narrador "--- TRILHA 3: FATORES TÉCNICOS, COMPENSAÇÕES & CÁLCULOS ---"

    claudia "Agora chegamos ao cálculo prático de console. A fórmula clássica de quilovoltagem é:"
    claudia "{b}kV = (2 × E) + C{/b}"
    claudia "Onde {b}E{/b} é a espessura medida em centímetros pelo espessômetro e {b}C{/b} é a constante do aparelho (geralmente entre 20 a 40)."

    # Questão 1: Cálculo Prático de kV
    $ uc1_total += 1
    narrador "Pergunta 1/4 — Cálculo de kV:"
    menu:
        claudia "Você usou o espessômetro e mediu um joelho com {b}15 cm{/b} de espessura. Sabendo que a constante do aparelho é {b}C = 30{/b}, qual deve ser o kV ajustado no console?"

        "A) 45 kV":
            claudia preocupada "Incorreto! Lembre-se da fórmula: kV = (2 × E) + C -> (2 × 15) + 30 = 30 + 30 = 60 kV."

        "B) 60 kV":
            $ uc1_pontos += 1
            claudia sorrindo "Cálculo perfeito! kV = (2 × 15) + 30 = 30 + 30 = 60 kV."

        "C) 75 kV":
            claudia preocupada "Incorreto! (2 × 15) + 30 resulta em 60 kV."

        "D) 90 kV":
            claudia preocupada "Incorreto! Lembre-se: 2 × 15 = 30; somando a constante 30 temos 60 kV."

    # Questão 2: Regra dos 15%
    $ uc1_total += 1
    narrador "Pergunta 2/4 — Regra dos 15%% de kVp:"
    menu:
        claudia normal "Se você aumentar o kVp em 15%% mantendo o mesmo mAs, qual será o impacto na exposição/densidade do receptor de imagem?"

        "A) A densidade radiográfica cairá pela metade.":
            claudia preocupada "Incorreto! Maior kVp aumenta o poder de penetração, logo mais fótons chegam ao receptor."

        "B) A densidade radiográfica dobrará (equivalente a dobrar o mAs).":
            $ uc1_pontos += 1
            claudia sorrindo "Corretíssimo! Um aumento de 15%% no kVp tem o mesmo efeito óptico de dobrar o mAs (e vice-versa: se aumentar 15%% de kV, pode cortar o mAs pela metade para reduzir o tempo de exposição)."

        "C) A imagem ficará sem contraste e totalmente branca.":
            claudia preocupada "Incorreto!"

        "D) Não haverá nenhuma alteração na exposição do receptor.":
            claudia preocupada "Incorreto! Quilovoltagem é determinante na energia e na taxa de fótons que alcançam o receptor."

    # Questão 3: Lei do Inverso do Quadrado da Distância
    $ uc1_total += 1
    narrador "Pergunta 3/4 — Distância Foco-Receptor (DFoFi):"
    menu:
        claudia normal "Segundo a Lei do Inverso do Quadrado da Distância, se você dobrar a distância foco-filme (ex: de 1 metro para 2 metros), o que deve acontecer com o mAs para manter a mesma exposição da imagem?"

        "A) O mAs deve ser reduzido à metade.":
            claudia preocupada "Cuidado! Mais longe significa que o feixe se espalha numa área 4 vezes maior. Reduzir o mAs deixaria a imagem extremamente escura/subexposta."

        "B) O mAs deve ser quadruplicado (multiplicado por 4).":
            $ uc1_pontos += 1
            claudia sorrindo "Isso mesmo! A intensidade da radiação cai com o quadrado da distância. Dobrando a distância (2x), a intensidade vira 1/4, exigindo 4x mais mAs."

        "C) O mAs permanece inalterado.":
            claudia preocupada "Incorreto!"

        "D) O mAs deve ser dividido por 4.":
            claudia preocupada "Incorreto! Diminuir o mAs com maior distância geraria uma radiografia completamente subexposta."

    # Questão 4: Compensações Clínicas (Idosos, Musculosos e Gesso)
    $ uc1_total += 1
    narrador "Pergunta 4/4 — Compensações Especiais:"
    menu:
        claudia normal "Como você deve compensar a técnica radiológica ao atender: (1) um idoso com osteopenia/osteoporose, e (2) um membro imobilizado com gesso seco?"

        "A) Idoso: aumentar kVp e mAs; Gesso seco: reduzir pela metade.":
            claudia preocupada "Incorreto! O osso osteopênico tem menor densidade (exige menos técnica), enquanto o gesso atua como barreira densa (exige mais técnica)."

        "B) Idoso: reduzir os parâmetros de exposição; Gesso seco: aumentar a técnica (+5 a 7 kV ou +50%% mAs).":
            $ uc1_pontos += 1
            claudia sorrindo "Excelente raciocínio clínico! Em idosos com perda de massa óssea diminuímos os fatores para não queimar a imagem; no gesso adicionamos penetração para atravessar o gesso e ver o traço de fratura."

        "C) Nenhuma alteração é necessária em ambos os casos.":
            claudia preocupada "Incorreto! A individualização dos fatores é dever do técnico responsável."

        "D) Idoso: manter os parâmetros; Gesso seco: dobrar a distância foco-filme sem alterar o console.":
            claudia preocupada "Incorreto! Afastar o tubo sem aumentar a técnica pioraria a subexposição no gesso."

    claudia sorrindo "Ótimo trabalho nos cálculos! Pontuação acumulada: [uc1_pontos]/[uc1_total]."
    jump uc1_menu_trilhas


# ==============================================================================
# TRILHA 4: BIOSSEGURANÇA, HIGIENIZAÇÃO, EPIS & ÉTICA
# ==============================================================================
label uc1_trilha_biosseguranca:
    scene bg sala_exame with dissolve
    show claudia normal at pos_claudia_normal with dissolve
    narrador "--- TRILHA 4: BIOSSEGURANÇA, HIGIENIZAÇÃO, EPIS & ÉTICA ---"

    claudia "A sala de exames é um ambiente hospitalar crítico. Segurança do paciente, do técnico e do acompanhante não são opcionais."

    # Questão 1: Higienização das Mãos
    $ uc1_total += 1
    narrador "Pergunta 1/4 — Procedimento de Lavagem das Mãos:"
    menu:
        claudia "Durante a lavagem de mãos na rotina de biossegurança do setor de radiologia, quais áreas críticas frequentemente negligenciadas exigem fricção rigorosa?"

        "A) Apenas as palmas das mãos em movimentos circulares rápidos (menos de 5 segundos).":
            claudia preocupada "Incorreto! A lavagem rápida da palma não elimina microrganismos das frestas anatômicas."

        "B) Espaços interdigitais (entre os dedos), leito ungueal (sob as unhas), polegares e borda externa da mão.":
            $ uc1_pontos += 1
            claudia sorrindo "Exatamente! Essas são as zonas de maior retenção biológica e reservatório de patógenos."

        "C) Apenas a ponta dos dedos polegar e indicador.":
            claudia preocupada "Incorreto!"

        "D) Apenas o dorso dos punhos sem molhar os dedos.":
            claudia preocupada "Incorreto! As pontas dos dedos e leitos ungueais são as superfícies de maior contato clínico."

    # Questão 2: Retirada de Luvas sem Contaminação
    $ uc1_total += 1
    narrador "Pergunta 2/4 — Descalçamento Seguro de Luvas:"
    menu:
        claudia normal "Ao finalizar o atendimento de um paciente com fluidos corporais ou sujidade, qual é a técnica correta para retirar as luvas de procedimento sem contaminar as mãos?"

        "A) Puxar as pontas dos dedos com a mão nua e lavar com álcool antes de descartar.":
            claudia preocupada "Perigo! Tocar a superfície externa da luva com a mão nua causa contaminação cruzada imediata."

        "B) Pinçar a luva pelo lado externo do punho, puxá-la pelo avesso, e com a mão limpa entrar por baixo da segunda luva retirando-a também pelo avesso.":
            $ uc1_pontos += 1
            claudia sorrindo "Perfeita técnica asséptica! A face contaminada fica sempre encapsulada no interior do avesso, sendo descartada direto na lixeira infectante (saco branco leitoso)."

        "C) Soprar ar no punho da luva até estourar.":
            claudia preocupada "Absolutamente contraindicado!"

        "D) Cortar as luvas com tesoura cirúrgica e descartar no lixo comum.":
            claudia preocupada "Contraindicado! O corte espalha aerossóis e o descarte deve ser em lixo infectante (grupo A)."

    # Questão 3: Para quem fornecer EPIs
    $ uc1_total += 1
    narrador "Pergunta 3/4 — Seleção de EPIs Plumbíferos:"
    menu:
        claudia normal "De acordo com as normas da CNEN e RDC 611 da ANVISA, para quais pessoas o técnico em radiologia deve fornecer ou utilizar Equipamentos de Proteção Individual (avental de chumbo, protetor de tireoide/gônadas)?"

        "A) Apenas para o próprio técnico operador.":
            claudia preocupada "Incorreto! O paciente e qualquer acompanhante presente na sala têm direito estrito à radioproteção."

        "B) Para o Técnico, para o Paciente (protegendo órgãos de alta radiossensibilidade fora do campo) e para o Acompanhante que precise conter o paciente.":
            $ uc1_pontos += 1
            claudia sorrindo "Resposta exemplar! O princípio ALARA e a legislação exigem blindagem de gônadas/tireoide no paciente quando fora da área de interesse, além de paramentação completa do acompanhante."

        "C) Apenas para o médico que assina o laudo.":
            claudia preocupada "Incorreto!"

        "D) Apenas para pacientes pediátricos, sendo dispensável em adultos.":
            claudia preocupada "Incorreto! A radioproteção de gônadas e tireoide fora do feixe primário é direito de todo paciente."

    # Questão 4: Conservação do Avental de Chumbo & Ética
    $ uc1_total += 1
    narrador "Pergunta 4/4 — Manuseio de EPIs e Sigilo Profissional:"
    menu:
        claudia normal "Sobre a conservação dos aventais plumbíferos e o Código de Ética Profissional dos Técnicos em Radiologia, qual afirmação é VERDADEIRA?"

        "A) Aventais de chumbo devem ser dobrados e guardados em gavetas comuns; o técnico pode discutir diagnósticos em redes sociais.":
            claudia preocupada "Gravíssimo erro! Dobrar o avental quebra a lâmina interna de chumbo criando fissuras invisíveis onde vaza radiação, e expor paciente em rede social viola a LGPD e o Código de Ética!"

        "B) Aventais de chumbo NUNCA devem ser dobrados (devem ficar em cabides próprios); o técnico tem dever de manter sigilo profissional e empatia no atendimento.":
            $ uc1_pontos += 1
            claudia sorrindo "Exatamente! Avental amassado perde a blindagem protetora, e o sigilo das informações e imagem do paciente é pilar ético inegociável."

        "C) Aventais podem ser lavados em máquina de lavar com alvejante.":
            claudia preocupada "Incorreto! A higienização é feita apenas com pano umedecido em solução desinfetante neutra."

        "D) O técnico pode divulgar imagens de exames de pacientes caso oculte apenas o nome, sem precisar de consentimento.":
            claudia preocupada "Incorreto! Exposição de exames sem autorização institucional e do paciente viola a LGPD e o Código de Ética."

    claudia sorrindo "Excelente conclusão da Trilha 4! Pontuação acumulada: [uc1_pontos]/[uc1_total]."
    jump uc1_menu_trilhas


# ==============================================================================
# SIMULADO GERAL INTEGRADO DA UC 1
# ==============================================================================
label uc1_simulado_completo:
    scene bg sala_exame with dissolve
    show claudia normal at pos_claudia_normal with dissolve
    narrador "--- SIMULADO INTEGRADO DA UC 1 (AVALIAÇÃO FORMATIVA) ---"
    claudia "Ravi, prepare-se para o desafio integrador da UC 1. São 5 situações práticas reais de plantão com 4 alternativas cada!"

    $ uc1_pontos = 0
    $ uc1_total = 5

    # Caso Simulado 1
    scene bg biombo with dissolve
    show claudia normal at pos_claudia_normal with dissolve
    narrador "Situação 1: Chega um paciente idoso de 78 anos para realizar RX de coluna lombar. O espessômetro indica 22 cm e a constante do aparelho é C = 35."
    menu:
        claudia "Qual deve ser a estimativa básica de kVp antes de aplicar a redução preventiva por osteopenia?"

        "A) 79 kVp":
            $ uc1_pontos += 1
            claudia sorrindo "Correto! kV = (2 × 22) + 35 = 44 + 35 = 79 kVp."

        "B) 57 kVp":
            claudia preocupada "Incorreto! (2 × 22) + 35 = 79 kVp."

        "C) 90 kVp":
            claudia preocupada "Incorreto!"

        "D) 44 kVp":
            claudia preocupada "Incorreto! 44 é apenas 2 × E. Somando a constante C=35, temos 79 kVp."

    # Caso Simulado 2
    scene bg sala_exame with dissolve
    show claudia normal at pos_claudia_normal with dissolve
    narrador "Situação 2: O exame de coluna torácica exige feixe mais intenso na região inferior (mais densa) do que na superior."
    menu:
        claudia "Como você orienta a posição do tubo aproveitando o Efeito Anódico?"

        "A) Cátodo voltado para a região inferior (abdômen/dorso baixo) e Ânodo voltado para a superior.":
            $ uc1_pontos += 1
            claudia sorrindo "Perfeito! A extremidade catódica entrega maior intensidade de radiação."

        "B) Ânodo voltado para a região inferior.":
            claudia preocupada "Incorreto! O ânodo atenua o feixe."

        "C) O tubo deve ser girado 90° na transversal sem relação anatômica.":
            claudia preocupada "Incorreto! Girar sem critério prejudica a colimação e o alinhamento do feixe."

        "D) A posição do tubo é irrelevante em exames de coluna.":
            claudia preocupada "Incorreto! A variação de densidade na coluna torácica é clássica para uso do efeito anódico."

    # Caso Simulado 3
    narrador "Situação 3: Uma mãe vai acompanhar seu filho de 5 anos dentro da sala para conter o braço durante o RX de antebraço."
    menu:
        claudia normal "Qual é a sua conduta ética e regulatória imediata?"

        "A) Paramentar a mãe com avental plumbífero e protetor de tireoide, questionando antes sobre possibilidade de gestação.":
            $ uc1_pontos += 1
            claudia sorrindo "Conduta irrepreensível! Investigar gestação e blindar completamente o acompanhante é protocolo obrigatório."

        "B) Deixar a mãe sem avental porque ela vai ficar a mais de 30 cm do tubo.":
            claudia preocupada "Erro gravíssimo de radioproteção!"

        "C) Solicitar que a mãe saia e pedir para o próprio técnico segurar a criança sem EPI.":
            claudia preocupada "Nunca! O técnico é profissional ocupacionalmente exposto (IOE) e não deve conter pacientes como rotina."

        "D) Colocar apenas protetor de tireoide na mãe, dispensando o avental de tronco.":
            claudia preocupada "Incorreto! O avental plumbífero é obrigatório para proteção de órgãos vitais e gônadas."

    # Caso Simulado 4
    scene bg biombo with dissolve
    show claudia normal at pos_claudia_normal with dissolve
    narrador "Situação 4: Você precisa visualizar uma fratura no carpo com máximo detalhe anatômico de trabéculas ósseas."
    menu:
        claudia "Qual seleção de ponto focal e acessório é indicada?"

        "A) Ponto focal fino e chassi com écran de alta resolução (ou sem grade/contato direto).":
            $ uc1_pontos += 1
            claudia sorrindo "Exato! Ponto focal fino reduz a penumbra geométrica proporcionando nitidez máxima."

        "B) Ponto focal grosso e grade antidifusora pesada.":
            claudia preocupada "Incorreto! Ponto focal grosso gera maior penumbra e é reservado para estruturas de alta carga térmica."

        "C) Ponto focal grosso com aumento de 30 kVp para clarear os ossos.":
            claudia preocupada "Incorreto! Aumentar kV em excesso degrada o contraste e aumenta a radiação espalhada."

        "D) Usar filtro adicional de chumbo sobre o carpo.":
            claudia preocupada "Incorreto! Chumbo sobre a estrutura bloquearia o feixe e impediria a formação da imagem."

    # Caso Simulado 5
    scene bg sala_exame with dissolve
    show claudia normal at pos_claudia_normal with dissolve
    narrador "Situação 5: Ao terminar a rotina de atendimento do turno matutino, qual o procedimento com o console e detectores?"
    menu:
        claudia "Como realizar a biossegurança e desligamento seguro?"

        "A) Borrifar álcool líquido 70%% diretamente sobre o painel eletrônico e dobrar os aventais no banco.":
            claudia preocupada "Nunca borrife líquidos diretamente nos componentes eletrônicos nem dobre aventais de chumbo!"

        "B) Aplicar desinfetante hospitalar compatível com pano umedecido em superfícies de contato, guardar aventais em cabides e registrar ocorrências.":
            $ uc1_pontos += 1
            claudia sorrindo "Padrão ouro de qualidade e biossegurança institucional!"

        "C) Desligar a chave geral sem limpar a sala, deixando a desinfecção para o próximo plantonista.":
            claudia preocupada "Incorreto! A biossegurança da sala deve ser concluída antes da passagem de plantão."

        "D) Lavar o detector digital com água corrente e sabão em pó.":
            claudia preocupada "Gravíssimo! Detectores e chassis são equipamentos eletrônicos sensíveis e nunca devem ser lavados em água corrente."

    # Cálculo e Atribuição de Estrelas Persistentes
    if uc1_pontos == 5:
        $ persistent.uc1_estrelas = max(persistent.uc1_estrelas, 3)
        $ persistent.uc1_concluida = True
        $ medalha = "⭐⭐⭐ (3/3 Estrelas - Excelência Técnica)"
    elif uc1_pontos == 4:
        $ persistent.uc1_estrelas = max(persistent.uc1_estrelas, 2)
        $ persistent.uc1_concluida = True
        $ medalha = "⭐⭐ (2/3 Estrelas - Bom Desempenho)"
    elif uc1_pontos == 3:
        $ persistent.uc1_estrelas = max(persistent.uc1_estrelas, 1)
        $ medalha = "⭐ (1/3 Estrela - Precisa Praticar)"
    else:
        $ medalha = "❌ (Sem Estrelas - Refazer)"

    # Feedback Final
    scene bg sala_exame with fade
    show claudia sorrindo at pos_claudia_sorrindo with dissolve
    narrador "--- RESULTADO DA AVALIAÇÃO DA UC 1 ---"
    narrador "Você acertou {b}[uc1_pontos]{/b} de {b}[uc1_total]{/b} questões no simulado."
    narrador "Conquista Registrada: {b}[medalha]{/b}"

    if uc1_pontos >= 4:
        claudia sorrindo "PARABÉNS, Ravi! Seu desempenho foi {b}DESENVOLVIDO (D){/b} com louvor!"
        claudia sorrindo "Você demonstrou domínio sólido de física das radiações, parâmetros técnicos, biossegurança e proteção radiológica."
    else:
        show claudia preocupada at pos_claudia_preocupada with dissolve
        claudia preocupada "Você obteve {b}NÃO DESENVOLVIDO (ND){/b} temporário. Recomendo revisar as 4 trilhas práticas da UC 1 para consolidar os conceitos fundamentais."

    menu:
        "🔄 Repetir o Simulado Integrado":
            jump uc1_simulado_completo

        "📚 Explorar as Trilhas Temáticas":
            jump uc1_menu_trilhas

        "🏠 Voltar ao Menu Principal":
            jump menu_selecao_modo
