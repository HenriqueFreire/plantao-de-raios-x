# Game Design Document (GDD) — Plantão de Raios-X
**Projeto Integrador | Curso Técnico em Radiologia — Senac Campinas**

---

## 1. Visão Geral
* **Título:** *Plantão de Raios-X*
* **Gênero:** Visual Novel educativa + Simulador interativo em Python
* **Engine:** Ren'Py 8 + Python 3
* **Plataforma-alvo:** PC (Linux / Windows) e Android
* **Público-alvo:** Estudantes, docentes e profissionais da área de Radiologia

---

## 2. Estrutura de Modos de Jogo

### Modo 1: Estudo por Unidade Curricular (UC)
Permite ao estudante praticar conteúdos pontuais das UCs do Senac através de minigames e quizzes rápidos:
* **UC1 (Bases Operacionais & Biossegurança):**
  * Minigame de higienização de sala e paramentação de EPIs.
  * Cálculo de fatores de exposição ($kV = 2 \times \text{espessura} + C$).
* **UC2 (Anatomia & Posicionamento de Extremidades):**
  * Quiz de identificação anatômica (MMSS e MMII).
  * Posicionamento, incidências (AP, PA, Perfil, Oblíqua) e centralização do Raio Central (RC).
* **UC6 (Proteção Radiológica & Legislação):**
  * Normas CNEN NN 3.01 e ANVISA RDC 611.
  * Limites de dose e regras de radioproteção (ALARA, tempo, distância e blindagem).

### Modo 2: Modo Estágio (Plantão com o Ravi)
Fluxo narrativo completo no Hospital Santa Magnólia, onde o estagiário Ravi vivencia o seu estágio supervisionado atendendo pacientes consecutivos em 6 etapas clínicas:
1. **Higienização dos Equipamentos:** Preparação e desinfecção da sala.
2. **Análise do Pedido Médico:** Leitura crítica e conferência dos dados do exame.
3. **Seleção de Parâmetros Técnicos:** Ajuste de kV, mAs, DFP e tamanho do chassi/detector.
4. **Recepção e Anamnese:** Diálogo humanizado, confirmação de identidade e contraindicações (ex: gravidez, implantes).
5. **Posicionamento do Paciente:** Instruções ao paciente, colimação e proteção com avental de chumbo.
6. **Avaliação da Imagem Radiográfica:** Análise do resultado, detecção de artefatos e decisão de repetição ou liberação.

---

## 3. Personagens Principais
* **Ravi (Protagonista):** Estagiário do 2º semestre do curso técnico, dedicado e empático.
* **Dra. Cláudia (Mentora):** Técnica e preceptora sênior experiente que orienta e avalia o jogador.
* **Pacientes:**
  1. *Seu Benedito (72 anos):* Tórax PA e Perfil (tosse persistente).
  2. *Júlia (24 anos):* Mão AP e Oblíqua (queda de bicicleta).
  3. *Marcos (45 anos):* Coluna Lombar AP e Perfil (dor lombar aguda).
  4. *Dona Tereza (68 anos):* Quadril AP (avaliação pós-cirúrgica).
  5. *Pedro (8 anos acompanhado da mãe):* Antebraço AP e Perfil (fratura pediátrica).

---

## 4. Sistema de Pontuação e Avaliação

| Etapa | Pontos Máximos |
| :--- | :---: |
| Higienização | 10 pts |
| Análise do Pedido Médico | 30 pts |
| Preparação dos Parâmetros | 20 pts |
| Anamnese & Atendimento | 20 pts |
| Posicionamento Radiográfico | 40 pts |
| Avaliação da Imagem | 20 pts |
| **Total por Caso Clínico** | **140 pts** |

**Classificação por Estrelas:**
* 126 a 140 pts: ⭐⭐⭐ Técnico Exemplar
* 98 a 125 pts: ⭐⭐ Bom Trabalho
* 70 a 97 pts: ⭐ Precisa Praticar Mais
* Menor que 70 pts: ❌ Repetir o Caso
