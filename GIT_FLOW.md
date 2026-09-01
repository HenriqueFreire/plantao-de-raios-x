# 🌿 Diretrizes de Git Flow — Plantão de Raios-X

Este documento define o modelo de ramificação (*branching strategy*), o padrão de commits e o fluxo de trabalho contínuo para o desenvolvimento do jogo **Plantão de Raios-X**.

---

## 🗺️ Modelo de Branches

```mermaid
gitGraph
    commit id: "v1.0.0-alpha (main)"
    branch develop
    checkout develop
    commit id: "Configuracao base"
    
    branch feat/menu-principal-ui
    checkout feat/menu-principal-ui
    commit id: "feat(ui): botoes do menu"
    commit id: "feat(ui): selecao de modos"
    checkout develop
    merge feat/menu-principal-ui id: "Merge em develop"
    
    branch feat/uc1-higienizacao
    checkout feat/uc1-higienizacao
    commit id: "feat(uc1): checklist sala"
    commit id: "feat(uc1): calculo kv/mas"
    checkout develop
    merge feat/uc1-higienizacao id: "Merge em develop"
    
    branch fix/ajuste-dose
    checkout fix/ajuste-dose
    commit id: "fix: limite maximo mas"
    checkout develop
    merge fix/ajuste-dose id: "Merge em develop"
    
    checkout main
    merge develop id: "Release v1.1.0 (main)" tag: "v1.1.0"
```

---

## 📌 Papel de Cada Branch

| Branch | Propósito | Regra de Merge |
| :--- | :--- | :--- |
| **`main`** | **Produção e Entregas Oficiais:** Contém apenas versões testadas, polidas e prontas para avaliação/apresentação na banca do Senac. | **Nunca** comitar diretamente. Recebe merges apenas da `develop`. |
| **`develop`** | **Integração Contínua:** Branch principal do dia a dia onde todas as novas funcionalidades e correções são unificadas e validadas. | Recebe merges das branches de `feat/*`, `fix/*`, `style/*` e `docs/*`. |
| **`feat/*`** | **Novas Funcionalidades:** Criação de telas, minigames, casos clínicos ou sistemas de pontuação. | Criada a partir da `develop` e mesclada de volta na `develop`. |
| **`fix/*`** | **Correção de Bugs:** Ajuste de cálculos de dose, erros de fluxo de diálogo ou inconsistências visuais. | Criada a partir da `develop` e mesclada na `develop`. |
| **`style/*`** | **Melhorias Visuais e Assets:** Sprites, novas radiografias, tipografia e temas de interface. | Criada a partir da `develop` e mesclada na `develop`. |
| **`docs/*`** | **Documentação:** Atualizações no GDD, README e guias do curso. | Criada a partir da `develop` e mesclada na `develop`. |

---

## 🚀 Ciclo de Trabalho Passo a Passo

### 1. Iniciar uma Nova Tarefa
Antes de iniciar qualquer código, certifique-se de estar na `develop` atualizada:
```bash
git checkout develop
git pull origin develop  # (quando houver repositório remoto configurado)
git checkout -b feat/nome-da-funcionalidade
```

*Exemplos de nomes de branch:*
* `feat/menu-principal-ui`
* `feat/uc1-higienizacao-kv`
* `feat/caso1-benedito`
* `fix/calculo-mAs-torax`
* `style/sprites-pacientes`

---

### 2. Padrão de Mensagens de Commit (Conventional Commits)
Use mensagens em português claras e padronizadas:

* `feat(...)`: Nova funcionalidade
  * Exemplo: `git commit -m "feat(uc1): adicionar minigame de checklist de higienizacao"`
* `fix(...)`: Correção de bug
  * Exemplo: `git commit -m "fix(anamnese): corrigir validacao da pergunta sobre gravidez"`
* `style(...)`: Mudanças puramente visuais / assets
  * Exemplo: `git commit -m "style(ui): adicionar novos botoes com estilo hospitalar"`
* `docs(...)`: Documentação
  * Exemplo: `git commit -m "docs(gdd): detalhar caso clinico da Julia"`
* `refactor(...)`: Refatoração sem alterar o comportamento
  * Exemplo: `git commit -m "refactor(minigames): modularizar funcoes python"`

---

### 3. Testar Localmente
Antes de mesclar sua branch, teste o jogo no ambiente Nix:
```bash
renpy .
```

---

### 4. Integrar na Branch `develop`
Após validar que a funcionalidade está completa e sem erros:
```bash
# 1. Voltar para a develop
git checkout develop

# 2. Mesclar a branch finalizada
git merge feat/nome-da-funcionalidade

# 3. Deletar a branch local temporária
git branch -d feat/nome-da-funcionalidade
```

---

### 5. Fechar um Marco/Release na `main`
Quando um conjunto completo de funcionalidades estiver pronto para ser apresentado (ex: finalização de uma UC ou de um caso clínico completo):
```bash
git checkout main
git merge develop
git tag -a v1.0.0 -m "Release: Versao com Caso 1 completo e Modo UCs"
```

---

## 🛡️ Checklist de Boas Práticas
- [ ] **Não subir arquivos temporários:** O arquivo `.gitignore` já ignora arquivos compilados `.rpyc` e pastas de `cache/` e `saves/`.
- [ ] **Commits atômicos:** Faça commits pequenos e frequentes conforme cada etapa for concluída.
- [ ] **Manter a `main` sagrada:** Só leve para a `main` o que puder ser jogado do início ao fim sem quebras.
