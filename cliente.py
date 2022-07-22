import socket # Importa o módulo socket
import login as log # Importa o módulo login

HOST = "127.0.0.1"  # Endereco IP do Servidor
PORT = 65432      # Porta do Servidor

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket
tcp.connect((HOST, PORT)) # Conecta ao servidor


def main(): # Função principal
    while True: # Loop infinito
        print("___________________")
        print("Bem vindo ao cliente")
        print("Para verificar e-mail digite 1")
        print("Para enviar e-mail digite 2")
        print("Para sair digite sair")
        print("___________________")


        opcao = input("Digite a opção: ")   # Recebe a opção do usuário
        if opcao == "1":
            opcao = "verificar"
            tcp.sendall(opcao.encode())
            print("Verificando e-mail")
            
            #alt = "contador"
            #tcp.sendall(alt.encode()) # Envia a opção para o servidor

            data = tcp.recv(1024) # Recebe dados do cliente e armazena em data (1024 é o tamanho do buffer)
            data = data.decode()
            print(data)
            
            alt = input()
            tcp.sendall(alt.encode())

            data = tcp.recv(1024) # Recebe dados do cliente e armazena em data (1024 é o tamanho do buffer)
            data = data.decode()
            print(data)

            numero = input()
            tcp.sendall(numero.encode())

            data = tcp.recv(1024) # Recebe dados do cliente e armazena em data (1024 é o tamanho do buffer)
            data = data.decode()
            print(data)



        elif opcao == "2": # Se a opção for 2 entra no if e envia o e-mail
            print("Enviando e-mail")
            opcao = "enviar"
            tcp.sendall(opcao.encode()) # Envia a opção para o servidor
            
            data = tcp.recv(1024) # Recebe dados do cliente e armazena em data (1024 é o tamanho do buffer)
            data = data.decode()
            print(data)
        
            if data == "Para quem você deseja enviar: ":
                email_envia = input(data)
                tcp.sendall(email_envia.encode())

            data = tcp.recv(1024) # Recebe dados do cliente e armazena em data (1024 é o tamanho do buffer)
            data = data.decode()
            print(data)

            if data == "Escreva o Assunto: ":
                assunto = input(data)
                tcp.sendall(assunto.encode())
            
            data = tcp.recv(1024) # Recebe dados do cliente e armazena em data (1024 é o tamanho do buffer)
            data = data.decode()
            print(data)

            if data == "Escreva a mensagem: ":
                mensagem = input(data)
                tcp.sendall(mensagem.encode())

            data = tcp.recv(1024) # Recebe dados do cliente e armazena em data (1024 é o tamanho do buffer)
            data = data.decode()
            print(data)



        elif opcao == "sair": # Se a opção for sair entra no if e sai do programa
            tcp.close()
            exit()
        else:
            print("Opção inválida") # Se a opção for inválida entra no if e mostra a mensagem de erro
            main() # Chama a função principal


main() # Chama a função principal