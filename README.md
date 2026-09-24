# Sockets


Implementação de um sistema cliente-servidor em Python, desenvolvido para a disciplina de Redes de Computadores.

## Como executar

Primeiro, abra um terminal e inicie o servidor:

```bash
python EchoServer.py
```

Em outro terminal, execute o cliente:

```bash
python EchoClient.py
```

É possível executar vários clientes simultaneamente. O servidor cria uma thread para cada cliente conectado, permitindo que eles sejam atendidos de forma independente.

## Funcionamento

O cliente envia comandos:

* `echo <mensagem>` → o servidor devolve a mensagem enviada.
* `quit` → encerra a conexão com aquele cliente, sem encerrar o servidor.
* Outros comandos → o servidor responde `Comando não reconhecido`.

O servidor também detecta quando um cliente encerra a conexão diretamente, utilizando `Ctrl+C`. O servidor pode ser encerrado com `Ctrl+C`.


