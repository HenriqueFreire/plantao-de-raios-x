# Game Design Document — Estágio em Radiologia
**Projeto Integrador | Curso Técnico em Radiologia — Senac Campinas**

---

## Visão Geral

**Título:** *Plantão de Raios-X*
**Gênero:** Visual Novel educativa com minigames
**Engine:** Ren'Py (narrativa) + Python puro (minigames integrados)
**Plataforma-alvo:** PC (Windows/Mac/Linux) + Android
**Público:** Estudantes e interessados em Técnico em Radiologia
**Tom:** Misto — contexto clínico sério, personagens simpáticos e situações cotidianas reconhecíveis

---

## Premissa

O jogador assume o papel de **Ravi**, um estagiário recém-chegado ao setor de radiologia do Hospital Santa Magnólia. Sob orientação da técnica sênior **Supervisora Cláudia**, ele enfrenta os desafios reais do dia a dia: higienizar equipamentos, interpretar pedidos médicos, posicionar pacientes e garantir imagens de qualidade tudo isso com empatia, precisão e proteção radiológica.

---

## 3. Personagens Principais

### Ravi (o jogador)
* **Perfil:** Estagiário do 2º semestre do curso Técnico em Radiologia.
* **Personalidade:** Dedicado, curioso, cuidadoso, mas inseguro em algumas situações de emergência.
* **Objetivo:** Cumprir o plantão com excelência, aprender os macetes práticos e conquistar a confiança da equipe.

### Supervisora Cláudia (mentora)
- Técnica sênior experiente, direta mas acolhedora
- Aparece no início de cada turno e após erros críticos
- Frase característica: *"Na radiologia, capricho não é perfeccionismo — é proteção."*

### Pacientes (1 por caso clínico)
Cada paciente tem personalidade própria para tornar a anamnese mais rica:

| # | Nome | Perfil | Exame |
|---|------|--------|-------|
| 1 | Seu Benedito | Idoso simpático, 72 anos, um pouco surdo | Tórax PA e Perfil |
| 2 | Júlia | Jovem ansiosa, 24 anos, suspeita de fratura | Mão AP e Oblíqua |
| 3 | Marcos | Homem agitado, 45 anos, dor lombar intensa | Coluna Lombar AP e Perfil |
| 4 | Dona Tereza | Senhor de 68 anos, pós-operatório de quadril | Quadril AP |
| 5 | Pedro | Criança de 8 anos acompanhada da mãe | Antebraço AP e Perfil |

---

## Fluxo de Cada Caso Clínico

Cada caso segue sempre o mesmo fluxo em 6 etapas. O conteúdo muda conforme o exame:

```
[INÍCIO DO DIA]
      │
      ▼
1. Higienização dos equipamentos   ← minigame: checklist
      │
      ▼
2. Análise do pedido médico        ← quiz: leitura da requisição
      │
      ▼
3. Preparação dos equipamentos     ← minigame: seleção de parâmetros técnicos
      │
      ▼
[CHEGADA DO PACIENTE]
      │
      ▼
4. Recepção e anamnese             ← diálogo com escolhas (visual novel)
      │
      ▼
5. Posicionamento                  ← quiz por etapas com imagens
      │
      ▼
6. Avaliação da imagem             ← análise da radiografia gerada
      │
      ▼
[RESULTADO DO CASO]
Pontuação + feedback por etapa
```

---

## Detalhamento das Etapas e Mecânicas

---

### Etapa 1 — Higienização dos Equipamentos

**Mecânica:** Minigame Python integrado ao Ren'Py via `renpy.call_screen()`.

O jogador vê a sala de exame com os equipamentos listados. Deve marcar o que higienizou antes de o paciente entrar.

**Itens do checklist (variam por caso):**
- Mesa de exame / mesa bucky
- Colimador e tubo de raios-X
- Apoios e acessórios (almofadas, suportes)
- Bucky mural (quando aplicável)
- Superfícies de contato (interruptores, painel)
- EPI do técnico (dosímetro, avental de chumbo)

**Consequências:**
- Todos marcados → +10 pts, Cláudia aprova
- 1 ou 2 esquecidos → -5 pts, aviso educativo
- Mais de 3 esquecidos → cena de repreensão leve + explicação técnica obrigatória

**Código sugerido (Python/Ren'Py):**
```python
# Em um screen Ren'Py ou minigame Python puro
items = [
    {"id": "mesa", "label": "Mesa de exame", "checked": False},
    {"id": "tubo", "label": "Tubo e colimador", "checked": False},
    {"id": "apoios", "label": "Apoios e almofadas", "checked": False},
    {"id": "painel", "label": "Painel de controle", "checked": False},
    {"id": "epi", "label": "EPI do técnico", "checked": False},
]

def calcular_higienizacao(items):
    marcados = sum(1 for i in items if i["checked"])
    total = len(items)
    if marcados == total:
        return "perfeito", +10
    elif marcados >= total - 2:
        return "aceitavel", -5
    else:
        return "reprovado", -15
```

---

### Etapa 2 — Análise do Pedido Médico

**Mecânica:** Quiz visual. Aparece uma imagem de requisição médica (ilustrada/mockup). O jogador responde 3 perguntas de múltipla escolha.

**Perguntas padrão:**
1. Qual região anatômica deve ser radiografada?
2. Qual a incidência solicitada?
3. Há alguma informação clínica importante no pedido?

**Exemplo — Caso 1 (Seu Benedito):**
```
Pedido: "Radiografia de Tórax PA e Perfil — Paciente com tosse persistente há 3 semanas"

Q1: Qual a região?
  A) Abdome   B) Tórax ✓   C) Coluna   D) Crânio

Q2: Quais incidências?
  A) AP e Oblíqua   B) PA e Perfil ✓   C) AP e Perfil   D) PA e AP

Q3: O que a informação clínica sugere investigar?
  A) Fratura   B) Alterações pulmonares ✓   C) Escoliose   D) Nada relevante
```

**Pontuação:** 10 pts por resposta correta. Erros exibem explicação educativa antes de avançar.

---

### Etapa 3 — Preparação dos Equipamentos

**Mecânica:** Minigame Python com sliders/seletores de parâmetros técnicos.

O jogador configura os parâmetros antes de chamar o paciente. Valores fora da faixa adequada geram consequências visuais na imagem final.

**Parâmetros configuráveis:**
- **kV** (kilovoltagem) — controla o contraste
- **mAs** (miliamperagem × tempo) — controla a densidade
- **DFP** (distância foco-filme/detector) — padrão 100cm ou 180cm para tórax
- **Tamanho do cassete/detector** — 18×24, 24×30, 35×43 cm
- **Grade antidifusora** — sim/não (depende da espessura do segmento)

**Tabela de referência para o código (valores corretos por caso):**

| Caso | Exame | kV ideal | mAs ideal | DFP | Cassete |
|------|-------|----------|-----------|-----|---------|
| 1 | Tórax PA/P | 110–125 | 3–5 | 180 cm | 35×43 |
| 2 | Mão AP/Obl | 50–60 | 4–8 | 100 cm | 18×24 |
| 3 | Coluna Lombar | 75–85 | 25–40 | 100 cm | 35×43 |
| 4 | Quadril AP | 70–80 | 20–35 | 100 cm | 35×43 |
| 5 | Antebraço AP/P | 50–60 | 3–6 | 100 cm | 18×24 |

**Consequências dos parâmetros:**
- Corretos → imagem final de qualidade
- kV muito baixo → imagem subexposta (escura)
- kV muito alto → imagem superexposta (clara demais, sem contraste)
- mAs alto → dose desnecessária ao paciente → penalidade de proteção radiológica
- Cassete errado → corte anatômico → repetição obrigatória

---

### Etapa 4 — Recepção e Anamnese

**Mecânica:** Visual novel clássica. Diálogo com o paciente. O jogador escolhe as perguntas a fazer numa lista.

**Perguntas obrigatórias (sempre devem ser feitas):**
- Confirmação do nome e data de nascimento
- Confirmação da região a ser examinada
- Uso de implantes metálicos ou marca-passo
- Histórico de cirurgias recentes
- Para mulheres em idade fértil: possibilidade de gravidez
- Alergia a contrastes (quando aplicável)
- Remoção de adornos metálicos

**Consequências:**
- Todas feitas → +15 pts, paciente se sente bem acolhido
- Esquecer gravidez em paciente feminina → cena de alerta grave + explicação obrigatória sobre proteção gonadal
- Esquecer implante metálico → artefato na imagem final

**Exemplo de diálogo — Seu Benedito:**
```renpy
define benedito = Character("Seu Benedito", color="#e8a87c")
define ravi = Character("Ravi", color="#7cb9e8")

label caso1_anamnese:
    scene sala_espera with fade
    show benedito normal

    benedito "Boa tarde, meu filho! Esse é o raio-x do pulmão?"
    
    menu:
        "Confirmar nome e data de nascimento":
            ravi "Seu nome completo e data de nascimento, por favor?"
            benedito "Benedito Alves da Silva, 14 de março de 1952."
            $ anamnese_score += 5
            jump anamnese_proxima_pergunta
        "Perguntar sobre implantes metálicos":
            ravi "O senhor tem algum implante metálico, marca-passo ou prótese?"
            benedito "Tenho não, graças a Deus. Só esse joelho que dói..."
            $ anamnese_score += 5
            jump anamnese_proxima_pergunta
        "Chamar logo para a sala":
            ravi "Pode vir comigo, senhor."
            $ anamnese_score -= 10
            $ anamnese_incompleta = True
            jump posicionamento_caso1
```

---

### Etapa 5 — Posicionamento

**Mecânica:** Sequência de quiz com imagens. Dividida em sub-etapas que simulam o raciocínio clínico real.

**Sub-etapas do posicionamento:**
1. Posição do paciente (decúbito dorsal, ortostático, sentado...)
2. Região de interesse e centralização do RC
3. Angulação do tubo (perpendicular, angulado X graus...)
4. Colimação (campo de irradiação)
5. Proteção radiológica (avental de chumbo, protetor gonadal...)

**Exemplo — Tórax PA (Seu Benedito):**
```
[Imagem: sala de raio-x com bucky mural]

Sub-etapa 1 — Posição do paciente:
Como você posiciona Seu Benedito?
  A) Deitado na mesa, em decúbito dorsal
  B) Em pé de frente ao bucky mural ✓
  C) Em pé de lado ao bucky mural
  D) Sentado na cadeira de rodas

[Feedback correto]: "Tórax PA: paciente em pé (ortostático), face anterior voltada ao bucky. 
Isso minimiza a magnificação cardíaca e melhora a expansão pulmonar."

Sub-etapa 2 — Centralização do RC:
Onde você centraliza o raio central?
  A) Na incisura jugular
  B) No processo xifoide
  C) Na 6ª vértebra torácica (entre escápulas) ✓
  D) No bordo inferior das escápulas

Sub-etapa 3 — Angulação do tubo:
Qual a angulação correta do tubo?
  A) 15° caudal
  B) Perpendicular ao detector ✓
  C) 10° cranial
  D) 5° lateral

Sub-etapa 4 — Colimação:
O campo deve incluir:
  A) Apenas os pulmões
  B) Da clavícula ao processo xifoide, incluindo toda a largura torácica ✓
  C) Só o lado com queixa
  D) O abdome superior também

Sub-etapa 5 — Proteção radiológica:
O que você faz antes de disparar?
  A) Nada, o exame é simples
  B) Coloca avental de chumbo na cintura pélvica de Seu Benedito ✓
  C) Sai da sala e fecha a porta ✓ (múltipla resposta)
  D) Avisa o corredor ✓ (múltipla resposta)
```

---

### Etapa 6 — Avaliação da Imagem

**Mecânica:** Aparece a "radiografia gerada" pelo jogo (imagem pré-definida baseada nas escolhas do jogador) e o jogador precisa avaliá-la.

**Três tipos de imagem possível:**
- **Imagem adequada** → parâmetros e posicionamento corretos
- **Imagem subexposta/superexposta** → parâmetros técnicos errados
- **Imagem com erro de posicionamento** → rotação, corte, artefato

**Perguntas de avaliação:**
1. A imagem está tecnicamente adequada para diagnóstico?
2. Se não, qual o problema principal?
3. O que você faria? (Aceitar / Repetir / Chamar supervisor)

**Critérios ensinados (aparecem no feedback):**
- Simetria das clavículas (tórax)
- Visibilidade de estruturas específicas
- Ausência de artefatos
- Densidade e contraste adequados
- Campo colimado corretamente

---

## Sistema de Pontuação

| Etapa | Pontos máximos |
|-------|---------------|
| Higienização | 10 pts |
| Análise do pedido | 30 pts |
| Preparação dos equipamentos | 20 pts |
| Anamnese | 20 pts |
| Posicionamento | 40 pts |
| Avaliação da imagem | 20 pts |
| **Total por caso** | **140 pts** |

**Classificação ao final de cada caso:**
- 126–140 pts → ⭐⭐⭐ "Técnico exemplar"
- 98–125 pts → ⭐⭐ "Bom trabalho"
- 70–97 pts → ⭐ "Precisa melhorar"
- Abaixo de 70 → "Repetir o caso"

**Penalidades especiais (subtraem pontos independente da etapa):**
- Esquecer de perguntar sobre gravidez: -20 pts
- Não sair da sala antes de disparar: -15 pts
- Repetir o exame sem necessidade (dose extra): -10 pts
- Aceitar imagem inadequada para diagnóstico: -15 pts

---

## Estrutura de Arquivos do Projeto Ren'Py

```
plantao_raios_x/
│
├── game/
│   ├── script.rpy              # Script principal, menu inicial
│   ├── personagens.rpy         # Definição de personagens e sprites
│   ├── casos/
│   │   ├── caso1_benedito.rpy
│   │   ├── caso2_julia.rpy
│   │   ├── caso3_marcos.rpy
│   │   ├── caso4_tereza.rpy
│   │   └── caso5_pedro.rpy
│   ├── minigames/
│   │   ├── higienizacao.rpy    # Screen + lógica Python do checklist
│   │   ├── parametros.rpy      # Screen + lógica Python dos parâmetros
│   │   └── avaliacao.rpy       # Screen de avaliação da imagem
│   ├── quiz/
│   │   ├── pedido_medico.rpy   # Quiz de leitura da requisição
│   │   └── posicionamento.rpy  # Quiz de posicionamento por etapas
│   ├── ui/
│   │   ├── resultado_caso.rpy  # Tela de pontuação ao final do caso
│   │   └── hud.rpy             # HUD com pontuação em tempo real
│   └── assets/
│       ├── backgrounds/        # Cenários: sala RX, recepção, corredor
│       ├── sprites/            # Personagens: Cláudia, pacientes
│       ├── imagens_rx/         # Radiografias (adequadas e com erros)
│       └── ui/                 # Ícones, botões, frames
│
├── requirements.txt            # Dependências Python (pygame, etc.)
└── README.md
```

---

## Variáveis Globais do Jogo

```python
# Variáveis de controle (declarar em script.rpy com 'default')

default pontuacao_total = 0
default caso_atual = 1

# Por caso:
default higienizacao_score = 0
default pedido_score = 0
default parametros_score = 0
default anamnese_score = 0
default posicionamento_score = 0
default avaliacao_score = 0

# Flags de consequências:
default anamnese_incompleta = False
default gravidez_perguntada = False
default parametros_corretos = False
default imagem_qualidade = "adequada"  # "adequada", "subexposta", "superexposta", "posicionamento_errado"

# Parâmetros escolhidos pelo jogador:
default kv_escolhido = 0
default mas_escolhido = 0
default dfp_escolhido = 100
default cassete_escolhido = ""
```

---

## Prompt para a IA Gerar o Código

Use o seguinte prompt ao pedir para uma IA (como Claude) gerar o código de cada parte:

```
Você é um desenvolvedor de jogos educativos especializado em Ren'Py e Python.

Gere o código Ren'Py para [NOME DA ETAPA] do caso clínico [NÚMERO] do jogo "Plantão de Raios-X".

Contexto do jogo:
- Engine: Ren'Py com minigames em Python via renpy.call_screen()
- Tom: sério e educativo, personagens simpáticos
- O jogador é Ravi, estagiário de radiologia
- A mentora é Supervisora Cláudia
- As variáveis globais estão declaradas conforme o GDD

Caso [NÚMERO] — Paciente: [NOME DO PACIENTE]
Exame: [NOME DO EXAME]
Parâmetros corretos: kV [X], mAs [X], DFP [X]cm, cassete [X]

Siga estritamente o fluxo e as mecânicas descritas no GDD.
Inclua comentários explicando cada bloco de código.
Gere o arquivo completo: caso[N]_[nome].rpy
```

---

## Referências Técnicas

- Bontrager, K. L. *Tratado de Técnica Radiológica e Base Anatômica*. 8ª ed.
- ANVISA — Normas de Proteção Radiológica (CNEN NN 3.01)
- RSNA (Radiological Society of North America) — radiographs.rsna.org
- ACR — American College of Radiology Practice Guidelines

---

*Documento gerado como base para desenvolvimento assistido por IA.*
*Versão 1.0 — Projeto Integrador Senac Campinas*
