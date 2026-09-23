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
            print("Conexão com o cliente na porta", port, "encerrada.")
            break 

        if s.split()[1] == "echo": #se a primeira palavra da string (após o screename, por isso [1]) for echo
            screenName = s.split()[0]
            msg = " ".join(s.split()[2:])
            saida.write(screenName + " " + msg + "\n")#devolve a mensagem. com \n que veio do cliente, mas tinha sido perdido no split
            saida.flush()

        elif s.split()[1] == "quit": #se a primeira palavra da string for quit
            print("Fechando a conexão com o cliente na porta ", port, ".")
            saida.close()
            entrada.close()
            clientSocket.close()
            break
        else:
            saida.write("Comando não reconhecido\n")
            saida.flush()

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("127.0.0.1", port))
serverSocket.listen()
serverSocket.settimeout(1) #para permitir o encerramento do servidor por keyboardinterrupt

print("Servidor iniciado na porta " + str(port)+ ". Aguardando conexão do cliente.")

try:
    while True:
        try:
            # espera até alguma requisição de conexão
            clientSocket, address = serverSocket.accept()

            #cria uma thread que irá executar a função thread_atende_cliente
            thread = threading.Thread(
                target=thread_atende_cliente,
                args=(clientSocket, address[1]), #parâmetros a serem passados para a função
                daemon = True 
            )
            thread.start()

        except socket.timeout:
            continue

except KeyboardInterrupt:
    print("\nServidor encerrado.")

