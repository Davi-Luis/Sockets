import socket

screenName = "Davi"
host = "127.0.0.1" #IP do meu próprio computador, localhost
port = 4444

# conecta ao servidor
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((host, port))

# cria os streams para o socket
entrada = clientSocket.makefile("r")
saida = clientSocket.makefile("w")

print("Conectado ao IP " + host + " na porta " + str(port))

# lê da entrada padrão, envia e escreve resposta
while True:
    # leitura
    s = input()

    # envio pelo socket
    saida.write("[" + screenName + "]: " + s + "\n")
    saida.flush()

    # pega resposta
    resposta = entrada.readline()

    if not resposta:
        break

    print(resposta, end="")

# encerra os sockets
print("Closing connection to " + host)

saida.close()
entrada.close()
clientSocket.close()