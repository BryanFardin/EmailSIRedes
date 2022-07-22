import socket
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
            global alt            
            alt = data
            

            print(alt)

            if data == "verificar":
                print("Verificando e-mail")
                alt = "contador"
                conn.sendall(verificar_email().encode()) # Envia a opção para o servidor
                if data == "contador":
                    conn.sendall(verificar_email().encode()) # Envia a opção para o servidor
            if data == "s":
                conn.sendall(verificar_email().encode()) # Envia a opção para o servidor
            if data.isdigit():
                global numero
                numero = int(alt)
                conn.sendall(verificar_email().encode())


            elif data == "enviar": # Se a opção for 2 entra no if e envia o e-mail
                print("Enviando e-mail")
                #conn.sendall(enviar_email().encode()) # Envia a opção para o servidor
                global altaux

                altaux = "email_envia"
                
                if altaux == "email_envia":
                    conn.sendall(enviar_email().encode()) # Usuário que recebe o e-mail
                    altaux = "assunto"

                if altaux == "assunto":
                    conn.sendall(enviar_email().encode()) # Usuário que recebe o e-mail
                    altaux = "mensagem"

                if altaux == "mensagem":
                    conn.sendall(enviar_email().encode()) # Usuário que recebe o e-mail
                    altaux = "finalizado"
                



            
            if not data: # Se o dado recebido for nulo entra no i
                break # Sai do loop
            #conn.sendall(data) # Envia o dado recebido do cliente para o cliente

            
        tcp.close() # Fecha a conexão
        print("Conexão encerrada")

def verificar_email(): # Função para verificar e-mail
                with open ("caixa de entrada/email.txt", "r") as email: # Abre o arquivo
                    linha = email.readlines() # Le o arquivo
                    cont = 0 # Contador
                    contaux = 0 # Contador Auxiliar
                    aux = []
                    usuario = log.usuario # Usuário logado

                    if alt == "contador":
                        for i in linha:
                            contaux += 1

                            if 'Para: '+usuario+'\n' in i: # Verifica se o usuário tem e-mail
                                aux.append(contaux)
                                cont += 1

                        texto = f"Você tem {cont} e-mails\n----------------\nDeseja visualizar um e-mail? (s/n)"
                        return texto
                    
                    if alt == "s": # Se o usuário desejar visualizar um e-mail
                        texto = "Digite o número do e-mail que deseja visualizar"
                        return texto
                    if alt.isdigit():
                        for i in linha:
                            contaux += 1

                            if 'Para: '+usuario+'\n' in i: # Verifica a pos dos emails
                                aux.append(contaux)
                        
                        n = aux[numero-1]

                        de = linha[n-2] # Mostra a pessoa que enviou o e-mail
                        para = linha[n-1] # Mostra para quem é o e-mail
                        assunto = linha[n] # Mostra o assunto do e-mail
                        msg = linha[n+1] # Mostra a mensagem do e-mail                         
                        texto = f"{de}\n{para}\n{assunto}\n{msg}"
                        return texto
                        if linha == '':
                            pass

                        
def enviar_email(): # Função para enviar e-mail
    email = open("caixa de entrada/email.txt", "a") # Abre o arquivo
    global de
    de = log.usuario # Usuário logado
    
    if altaux == "email_envia":
        global email_envia
        email_envia = alt # Destinatario do e-mail
        texto = "Para quem você deseja enviar: "
        return texto


    if altaux == "assunto":
        global assunto
        assunto = alt # Assunto do e-mail
        texto = "Escreva o Assunto: "
        return texto
    
    
    if altaux == "mensagem":
        global mensagem
        mensagem = alt # Mensagem do e-mail
        texto = "Escreva a mensagem: "
        return texto
    
    if altaux == "finalizado":
        email.write("----------------\n De:{}\n Para: {}\n Assunto: {}\n Mensagem: {}\n".format(de, email_envia, assunto, mensagem)) # Escreve no arquivo
        print("E-mail enviado")
        email.close() # Fecha o arquivo
        texto = "E-mail enviado"
        return texto

main()
