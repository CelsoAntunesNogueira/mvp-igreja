# mvp-igreja

# Sistema de Gestão para Igrejas - MVP

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4%2B-red?style=for-the-badge&logo=python)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.2%2B-green?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-3-blue?style=for-the-badge&logo=sqlite)

## 📖 Sobre o Projeto

Este projeto é um **MVP (Produto Mínimo Viável)** de um sistema desktop para gestão de igrejas, desenvolvido em Python. A aplicação foi criada para centralizar as operações administrativas essenciais de uma comunidade religiosa, como gestão de membros, controle financeiro e armazenamento de documentos importantes.

O objetivo principal foi criar uma solução robusta, de fácil utilização e escalável, utilizando uma arquitetura modular que separa claramente a interface gráfica (GUI), a lógica de negócios (Controllers) e o acesso a dados (Models).

## ✨ Funcionalidades Principais

O sistema oferece um conjunto de funcionalidades essenciais para a administração de uma igreja:

*   **🔐 Autenticação Segura:** Sistema de login para garantir que apenas usuários autorizados acessem os dados.
*   **⛪ Gestão de Igrejas e Membros:** Funcionalidades completas de **CRUD** (Create, Read, Update, Delete) para cadastrar e gerenciar múltiplas igrejas e seus respectivos membros.
*   **📊 Dashboard Financeiro:** Uma tela visual com gráficos e indicadores (KPIs) para acompanhamento de entradas, saídas e saúde financeira da instituição.
*   **💰 Controle de Transações:** Módulos para registrar dízimos, ofertas e despesas, permitindo um controle de caixa detalhado.
*   **📄 Gestão de Documentos:** Repositório digital para fazer upload, armazenar e gerenciar documentos importantes como Atas de Reunião, relatórios contábeis (RAIS) e prestações de contas.



## 🛠️ Tecnologias e Arquitetura

Este projeto foi construído com as seguintes tecnologias:

*   **Linguagem:** Python 3.10+
*   **Interface Gráfica (GUI):** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) para uma interface moderna e agradável.
*   **Banco de Dados:** SQLite, um banco de dados leve e embarcado, perfeito para aplicações desktop.
*   **ORM (Object-Relational Mapping):** [SQLAlchemy](https://www.sqlalchemy.org/) para uma interação segura e eficiente com o banco de dados.
*   **Segurança:** Biblioteca `bcrypt` para hashing e proteção de senhas.
*   **Geração de Documentos (Planejado):** `reportlab` para criação de relatórios em PDF.
*   **Visualização de Dados:** `matplotlib` para a criação dos gráficos no dashboard financeiro.

A arquitetura do projeto segue o padrão **Model-View-Controller (MVC)** adaptado, separando as responsabilidades:
- **`models.py`:** Define a estrutura das tabelas do banco de dados (Models).
- **`gui/`:** Contém todas as telas da aplicação (Views).
- **`controllers.py`:** Centraliza a lógica de negócio e a comunicação entre a View e o Model (Controllers).
- **`database.py`:** Gerencia a conexão e a sessão com o banco de dados.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para executar o projeto em sua máquina local.

**1. Clone o Repositório:**
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

**2. Crie um Ambiente Virtual (Recomendado):**
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

**3. Instale as Dependências:**
```bash
pip install -r requisitos.txt
```

**4. Execute a Aplicação:**
```bash
python main.py
```
> Na primeira execução, o sistema criará um banco de dados `igreja.db` e um usuário padrão **admin** com a senha **admin**.

## 🔮 Próximos Passos e Evolução

Este MVP é a base para um sistema completo. Os próximos passos planejados incluem:
- [ ] Geração automática de Atas e Estatutos em PDF.
- [ ] Módulo de gestão de pequenos grupos (células).
- [ ] Calendário de eventos da igreja.
- [ ] Sistema de backup e restauração do banco de dados.

---

Feito com ❤️ por [Celso](linkedin.com/in/celsoantunesnogueira).
