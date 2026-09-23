import socket
import threading
port = 4444

def thread_atende_cliente(clientSocket, port):
    print("Conectado a um cliente na porta", port)

    # cria os streams para o socket
    entrada = clientSocket.makefile("r")
    saida = clientSocket.makefile("w")

    # espera a leitura dos dados
    while True:
        s = entrada.readline()

        if s == "": #se s for uma string vazia, a conexão com o cliente foi encerrada
            break 

        # envia a mesma mensagem de volta
        saida.write(s)
        saida.flush()

    # fecha a conexão
    print("Fechando a conexão com o cliente na porta ", port, ".")
    saida.close()
    entrada.close()
    clientSocket.close()

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("127.0.0.1", port))
serverSocket.listen()

print("Servidor iniciado na porta " + str(port)+ ". Aguardando conexão do cliente.")

while True:
    # espera até alguma requisição de conexão
    clientSocket, address = serverSocket.accept()

    #cria uma thread que irá executar a função thread_atende_cliente
    thread = threading.Thread( 
    target= thread_atende_cliente,
    args=(clientSocket, address[1]) #parâmetro a ser passado para a função
    )
    thread.start()

