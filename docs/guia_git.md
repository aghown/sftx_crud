# 📘 Guia de Boas Práticas com Git

Este documento foi criado para ajudar a equipe a trabalhar de forma organizada no repositório **sftx_crud**.  
Aqui você encontra os principais comandos e recomendações para evitar problemas.

---

## 🚀 Fluxo Básico de Trabalho

1. **Atualizar repositório antes de começar a programar**
   ```bash
   git pull origin main
   # Isso garante que você está com o código mais recente.

2. **Criar/modificar arquivos no projeto**
    (ex: editar src/main.py, docs/guia_git.md, etc.)

3. **Adicionar arquivos para commit**
    ```bash
    git add nome_do_arquivo
    # ou para adicionar tudo:
    git add .

4. **Fazer commit com mensagem clara**
    ```bash
    git commit -m "feat: adiciona função de cadastro"


5. **Enviar alterações para o GitHub**
    ```bash
    git push origin main

## ✍️ Convenção de Commits

Use prefixos para organizar os commits:

feat: → nova funcionalidade
Ex: feat: adiciona menu inicial

fix: → correção de erro
Ex: fix: corrige cálculo de saldo

docs: → mudanças na documentação
Ex: docs: cria guia_git.md

style: → mudanças de formatação (espaços, indentação, etc)

refactor: → melhorias no código (sem mudar o resultado)

test: → testes adicionados ou alterados

chore: → tarefas de manutenção (ex: criar pastas, atualizar dependências)

## 🔒 Commits Seguros

Antes de dar commit, sempre rode:

    git status


Isso mostra o que foi alterado e evita que arquivos errados sejam enviados.

Se precisar cancelar algo que não queria adicionar:

    git restore nome_do_arquivo

## 🌱 Dicas Extras

Sempre rode **git pull origin main** antes de começar o dia.

Não suba arquivos desnecessários (ex: .vscode/, __pycache__/).

Se for trabalhar em algo grande, crie uma branch:

    git checkout -b nome-da-branch

E depois junte no main.