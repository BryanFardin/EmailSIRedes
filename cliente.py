import socket
from turtle import clear
import login as log

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((HOST, PORT))

def verificar_email(email):
    tcp.send(email.encode())
    print(tcp.recv(1024).decode())
def enviar_email(email):
    tcp.send(email.encode())
    print(tcp.recv(1024).decode())


def main():
    print("___________________")
    print("Bem vindo ao cliente")
    print("Para verificar e-mail digite 1")
    print("Para enviar e-mail digite 2")
    print("Para sair digite sair")
    print("___________________")


    opcao = input("Digite a opção: ")
    if opcao == "1":
        print("Verificando e-mail")
        verificar_email(email)

    elif opcao == "2":
        print("Enviando e-mail")
        email = input("Digite o e-mail a enviar: ")
        enviar_email(email)
    elif opcao == "sair":
        tcp.close()
        exit()
    else:
        print("Opção inválida")
        main()





#    while True:
#        msg = input("Digite a mensagem: ")
#        if msg == "sair":
#            tcp.send(msg.encode())
#            break
#        tcp.send(msg.encode())
#        msg = tcp.recv(1024)
#        print(msg.decode())
#
#   tcp.close()
main()