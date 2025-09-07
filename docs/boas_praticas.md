# Boas Práticas em Python

Este guia foi criado para ajudar o time a manter um código **limpo, organizado e fácil de entender**, mesmo para quem está começando. Seguir boas práticas evita confusão e facilita a colaboração.

---

## Organização do Código

* **Mantenha o código legível**: use nomes de variáveis e funções que expliquem o que elas fazem.
  ✅ Exemplo: `saldo_total` em vez de `st`.

* **Nomes de funções claros**: use verbo + substantivo para indicar a ação e o objeto.
  ✅ Exemplos: `criar_usuario()`, `entrar_usuario()`, `recuperar_senha()`.
  ❌ Ruim: `funcao_novo_usuario()`, `novaSenha()`.

  * Evite nomes longos demais; prefira clareza em poucas palavras.
  * Se muitas funções relacionadas, considere agrupar em um arquivo/módulo. Ex.: `usuarios.py` → `criar()`, `entrar()`, `recuperar_senha()`.

* **Separe responsabilidades**: cada função deve fazer **uma coisa bem definida**.

* **Evite repetir código**: se você percebeu que escreveu a mesma coisa em vários lugares, crie uma função.

* **Comentários**: comente apenas quando o código não for óbvio. O ideal é que o código seja claro por si mesmo.

---

## Estrutura de Pastas

* `src/` : tudo que é código-fonte.
* `main.py`: ponto de entrada do programa (onde o loop principal fica).
* `menu.py`: tudo relacionado ao menu do sistema.
* `tests/`: testes automatizados.
* `docs/`: documentação (boas práticas, guia de git etc).

> Nunca deixe pastas vazias no repositório. Se precisar criar, adicione um arquivo `README.md` ou `.gitkeep` dentro.

---

## Estilo de Código

* **Indentação**: use 4 espaços por nível.
* **Linhas curtas**: máximo 79 caracteres por linha.
* **Imports organizados**: primeiro bibliotecas padrão, depois bibliotecas externas e por fim os módulos do projeto.
* **Strings**: mantenha o padrão de aspas `"` em todo o projeto.

Exemplo:

```python
# Correto
from datetime import datetime
import sys

from transacoes.deposito import depositar

saldo = 0

# Errado: bagunçado e sem padrão
import sys, datetime
from transacoes import *
```

---

## Quando atualizar o README?

* Adicione ou atualize o `README.md` apenas quando:

  * O objetivo do projeto mudar.
  * Novas instruções de instalação/execução forem necessárias.
  * Houver mudanças importantes nas funcionalidades.

> Não é necessário atualizar o README para cada pequeno ajuste no código.

---

## Zen do Python (Resumo)

O "Zen do Python" é uma coleção de princípios que guiam a escrita de código na linguagem.
Você pode ver a versão completa no terminal com `import this`.

* **Belo é melhor que feio.** → Prefira código limpo e legível.
* **Explícito é melhor que implícito.** → Evite "gambiarras mágicas".
* **Simples é melhor que complexo.** → Se algo pode ser feito de forma clara, faça.
* **Legibilidade conta.** → Código é mais lido do que escrito.
* **Erros nunca devem passar silenciosamente.** → Trate exceções.
* **Devemos ter uma — e preferencialmente só uma — maneira óbvia de fazer algo.**

👉 Esses princípios servem como guia geral para manter o código organizado e compreensível.
