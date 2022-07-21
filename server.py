import socket # Importa o módulo socket
import login as log # Importa o módulo login
import verificar_email as ve # Importa o módulo verificar_email


HOST = "127.0.0.1"  # Endereço IP do servidor
PORT = 65432  # Porta do servidor (IPv4)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket e o binda ao endereço
tcp.bind((HOST, PORT)) # bind ao endereço e inicia o servidor
tcp.listen(1) # Aceita conexões de um cliente
print("listado na porta ", PORT) # Mostra a porta que o servidor está escutando

def close():  # Função para fechar a conexão
    tcp.close() # Fecha a conexão
    print("Servidor encerrado")

def main(): # Função principal
    while True: # Loop infinito
        conn, addr = tcp.accept() # Aceita conexão do cliente
        print("Conectado a: ", addr) # Mostra o endereço do cliente
        
        while True: # Loop infinito
            data = conn.recv(1024) # Recebe dados do cliente e armazena em data (1024 é o tamanho do buffer)
            data = data.decode()

            if data == "1":
                print("Verificando e-mail")
                conn.sendall(ve.verificar_email().encode()) # Envia a opção para o servidor

            elif data == "2": # Se a opção for 2 entra no if e envia o e-mail
                print("Enviando e-mail")
                #ve.enviar_email()

            
            if not data: # Se o dado recebido for nulo entra no i
                break # Sai do loop
            #conn.sendall(data) # Envia o dado recebido do cliente para o cliente
        tcp.close() # Fecha a conexão
        print("Conecxão encerrada")

main()