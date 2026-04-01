# Requisitos Funcionais

Este documento reúne alguns dos requisitos funcionais levantados até o momento para o sistema CorewFlow Pilates API. Novos requisitos poderão ser adicionados conforme a equipe de Produto e UX avançar no levantamento, refinamento e detalhamento das necessidades do sistema.

## RF01 — Cadastro de alunos

O sistema deve permitir cadastrar alunos com seus dados principais e vínculo com modalidade e plano escolhidos.

## RF02 — Cadastro de instrutores

O sistema deve permitir cadastrar e gerenciar instrutores, considerando que pode existir mais de um instrutor no futuro, embora inicialmente haja apenas um por horário.

## RF03 — Cadastro de aparelhos

O sistema deve manter os 4 aparelhos da academia: Reformer, Cadillac, Chair e Ladder Barrel.

## RF04 — Gerenciamento da agenda

O sistema deve permitir gerenciar a agenda de aulas entre 7:00 e 19:00, em sessões com duração de 1 hora.

## RF05 — Controle de capacidade por horário

O sistema deve limitar cada horário a no máximo 4 alunos treinando simultaneamente.

## RF06 — Associação de instrutor ao aluno/aula

O sistema deve registrar qual instrutor atenderá cada aluno em cada agendamento ou sessão.

## RF07 — Controle de modalidade semanal

O sistema deve permitir matrícula nas modalidades de 1x, 2x ou 3x por semana e controlar o limite de agendamentos conforme a modalidade contratada.

## RF08 — Controle de planos

O sistema deve permitir matrícula nos planos mensal, bimestral, trimestral, semestral e anual.

## RF09 — Aula extra avulsa

O sistema deve permitir agendar aula extra mediante taxa individual quando o aluno desejar treinar mais de 3 vezes por semana.

## RF10 — Regra de rotação de aparelhos

O sistema deve controlar o revezamento dos aparelhos e impedir que o aluno utilize o mesmo aparelho em duas semanas consecutivas.

## RF11 — Aviso de vencimento de plano

O sistema deve alertar quando o plano de um aluno estiver próximo do encerramento para apoiar o processo de renovação.

## RF12 — Login no sistema

O sistema deve possuir autenticação de usuários para acesso às funcionalidades.
