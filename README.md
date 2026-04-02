<div align="center" id="top">

<h1 align="center">Projeto v2 Análise de Sistema I 💻 — CoreFlow Estúdio de Pilates</h1>
<h2>Repositório Back-end</h2>

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](#top)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](#top)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](#top)
[![Railway](https://img.shields.io/badge/Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white)](#top)
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)](#top)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](#top)

<h3>
O Estúdio CoreFlow é uma academia de pilates que oferece aulas personalizadas para seus clientes. O objetivo deste projeto é desenvolver um sistema de backend robusto e escalável para gerenciar as operações da academia, incluindo o gerenciamento de alunos, instrutores, aparelhos, modalidades, planos, aulas individuais e agenda. O sistema também deve ser capaz de enviar notificações para os alunos quando seus planos estiverem prestes a expirar.
</h3>

[![My Skills](https://skillicons.dev/icons?i=python,fastapi,docker,git,github,vscode)](https://skillicons.dev)

</div>

---

## Sobre o projeto

O CoreFlow é um sistema de back-end para um estúdio de pilates, com foco na gestão operacional da academia.

O projeto foi pensado para dar suporte ao gerenciamento de alunos, instrutores, aparelhos, modalidades, planos, aulas e agenda, além de servir como base para futuras evoluções da aplicação.

## Stack utilizada

- Python 3.13
- FastAPI
- Uvicorn
- SQLAlchemy
- PostgreSQL 16
- Docker
- Docker Compose

## Ambiente de desenvolvimento

O projeto está configurado para rodar com dois containers:

- `api`: aplicação FastAPI
- `db`: banco de dados PostgreSQL

A API roda em modo de desenvolvimento com `reload`, e a conexão com o banco dentro do Docker é feita usando o host `db`.

## Como rodar com Docker

### 1. Criar o arquivo de ambiente

No PowerShell:

```powershell
Copy-Item .env.exemple .env
```

Se preferir, você também pode criar o `.env` manualmente a partir do arquivo de exemplo.

### 2. Subir os containers

```powershell
docker compose up --build -d
```

### 3. Verificar se os serviços estão rodando

```powershell
docker compose ps
```

### 4. Acessar a aplicação

- API: `http://localhost:8000`
- Health check: `http://localhost:8000/health`
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Comandos úteis

### Ver logs da API

```powershell
docker compose logs -f api
```

### Ver logs do PostgreSQL

```powershell
docker compose logs -f db
```

### Parar os containers

```powershell
docker compose down
```

### Parar e remover volumes

```powershell
docker compose down -v
```

## Variáveis de ambiente

O projeto utiliza as seguintes variáveis no arquivo `.env`:

- `APP_NAME`
- `DATABASE_URL`
- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `SECRET_KEY`

## Estrutura atual do ambiente Docker

- A aplicação usa a porta `8000`
- O PostgreSQL usa a porta `5432`
- Os dados do banco são persistidos no volume `postgres_data`

## Informações do trabalho

**Instituição:** [Centro Universitário do Triângulo — UNITRI](https://unitri.edu.br)  
**Curso:** Análise e Desenvolvimento de Sistemas  
**Disciplina:** Análise de Sistemas I  
**Professor:** [Igor](https://www.linkedin.com/in/gabrielcyrino/)
