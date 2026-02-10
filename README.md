# ⚖️ Lexos

> **Plataforma Inteligente de Gestão Processual e CRM Jurídico**

![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![React](https://img.shields.io/badge/React-18-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 🎯 Sobre o Projeto

O **Lexos** é uma solução SaaS (*Software as a Service*) desenvolvida para modernizar a rotina de escritórios de advocacia. O sistema resolve o problema da fragmentação de dados judiciais, centralizando o acompanhamento de processos e a gestão de clientes em uma interface única.

### 🚀 Diferenciais Técnicos
O sistema utiliza uma arquitetura híbrida de **captura de dados**:
1.  **Integração Oficial:** Conexão com a API DataJud (CNJ) para metadados em tempo real.
2.  **Crawler Inteligente:** Fallback para tribunais específicos que requerem raspagem de dados complementares.
3.  **Automação:** Rotinas em background (Background Jobs) para verificação periódica de novas movimentações.

## 🛠️ Tech Stack

O projeto foi construído seguindo os princípios de **Clean Architecture** e **SOLID**.

* **Backend:** Python (FastAPI), SQLAlchemy, Pydantic.
* **Frontend:** React.js, TypeScript, Tailwind CSS.
* **Banco de Dados:** PostgreSQL.
* **Infraestrutura:** Docker, Docker Compose.
* **Automação:** Celery/Redis (para filas de processamento assíncrono).

## 🧩 Funcionalidades Principais

- [x] **Gestão de Clientes (CRM):** Cadastro completo com vínculo processual.
- [x] **Rastreio Automático:** Monitoramento de processos pelo número CNJ unificado.
- [x] **Dashboard Analítico:** Visão geral de processos ativos, arquivados e prazos.
- [ ] **Notificações:** Alertas via E-mail/WhatsApp sobre novas movimentações (Roadmap).

## ⚙️ Como Executar Localmente

### Pré-requisitos
* Docker e Docker Compose instalados.

### Instalação

1. Clone o repositório:
```bash
git clone [https://github.com/DiogoRamos1986/lexos.git](https://github.com/DiogoRamos1986/lexos.git)
cd lexos

