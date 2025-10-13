# QA_AUTOMACAO_DE_TESTES

## 📌 Descrição das Pastas e Instruções de Execução
## 🧪 Projeto api/ — Automação de Testes com Python + Pytest + Request

- Dentro da pasta api está concentrada toda a estrutura de automação de testes de API desenvolvida em Python utilizando Pytest.

### 📂 docs/

- Contém os documentos de apoio e evidências de execução dos testes:

- Relatorio_Incidentes_API.pdf → Relatório consolidado dos testes executados e incidentes encontrados.

- caso_de_teste_get.md / caso_de_teste_post.md → Casos de teste documentados, com critérios de aceite e cenários cobertos para os endpoints GET e POST.

### 📄 README.md

- Arquivo com instruções detalhadas sobre:

- Como configurar o ambiente virtual (.venv)

- Instalar dependências

- Executar testes isolados e em massa com Pytest

- Gerar relatórios de execução

## 🌐 Projeto web/ — Automação de Testes com Cypress

### A pasta web contém toda a automação de testes end-to-end (E2E) desenvolvida com Cypress, organizada de acordo com a estrutura padrão do framework.

### 📂 docs 
- Documentação dos casos de teste frontend


### 📄 README.md

- Arquivo com instruções para:

    - Instalar dependências do projeto

    - Executar testes em modo interativo ou headless

    - Estrutura de pastas e organização dos testes (e2e, fixtures, support, pages)

▶️ Como executar os testes de Front-End

### 📂 cypress

- e2e/ → contém os arquivos de teste end-to-end (pageWeb.cy.js)

- fixtures/ → massas de dados e arquivos JSON usados nos testes

- support/ → comandos customizados e organização por páginas (page/home/homePage.js)


## Estrutura do projeto
```
├── 📁 .github/
│   └── 📁 workflows/
│       └── ⚙️ ci.yml
├── 📁 api/
│   ├── 📁 docs/
│   │   ├── 📕 Relatorio_Incidentes_API.pdf
│   │   ├── 📝 caso _de_teste_post.md
│   │   └── 📝 caso_de_teste_get.md
│   ├── 📁 src/
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 client.py
│   │   └── 🐍 testdata.py
│   ├── 📁 tests/
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 helpers.py
│   │   ├── 🐍 schemas.py
│   │   ├── 🐍 test_api_get.py
│   │   └── 🐍 test_api_post.py
│   ├── 📄 .env.example
│   ├── 📖 README.md
│   ├── 🐍 conftest.py
│   ├── ⚙️ pytest.ini
│   ├── 📄 requirements-dev.txt
│   └── 📄 requirements.txt
├── 📁 web/
│   ├── 📁 cypress/
│   │   ├── 📁 docs/
│   │   │   └── 📝 casos_de_teste_.md
│   │   ├── 📁 e2e/
│   │   │   └── 📄 pageWeb.cy.js
│   │   ├── 📁 fixtures/
│   │   │   └── 📄 example.json
│   │   └── 📁 support/
│   │       ├── 📁 page/
│   │       │   └── 📁 home/
│   │       │       └── 📄 homePage.js
│   │       ├── 📄 commands.js
│   │       └── 📄 e2e.js
│   ├── 📖 README.md
│   ├── 📄 cypress.config.js
│   ├── 📄 package-lock.json
│   └── 📄 package.json
└── 📖 README.md
```