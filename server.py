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
        
        global list_alt
        list_alt = []

        while True: # Loop infinito
            data = conn.recv(1024) # Recebe dados do cliente e armazena em data (1024 é o tamanho do buffer)
            data = data.decode()
            global alt
            alt = ''

            if (data != "enviar") & (data != 'envio1') & (data != 'envio2') & (data != 'envio3'):
                alt = data
                list_alt.append(alt)
                




                            
            global auxemail
            auxemail = ''
            

            #print(alt)

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
                var = 'destinatario'
                conn.sendall(var.encode()) # Envia a opção para o servidor
                #global auxemail
                
            elif data == 'envio1':
                #global auxemail
                auxemail = "envio1"
                enviar_email()
                var = 'assunto'
                conn.sendall(var.encode()) # Envia a opção para o servidor
            
            elif data == 'envio2':
                #global auxemail
                auxemail = "envio2"
                enviar_email()
                var = 'mensagem'
                conn.sendall(var.encode()) # Envia a opção para o servidor

            elif data == 'envio3':
                #global auxemail
                auxemail = "envio3"
                enviar_email()
                var = 'bumbum'
                conn.sendall(var.encode()) # Envia a opção para o servidor
            
            elif data == 'finalizado':
                auxemail = "finalizado"
                enviar_email()
                


            
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
    #global auxemail
    de = log.usuario # Usuário logado
    print(list_alt)
    

    if (auxemail == "envio1"):
        print('entrou1', list_alt[0])

        global email_envia
        email_envia = list_alt[0] # Destinatario do e-mail
        list_alt.pop(0)
        return email_envia


    if (auxemail == "envio2"):
        print('entrou2', list_alt[0])

        global assunto
        assunto = list_alt[0] # Assunto do e-mail
        list_alt.pop(0)
        return assunto
        
        
    if (auxemail == "envio3"):
        print('entrou3', list_alt[0])

        global mensagem
        mensagem = list_alt[0] # Mensagem do e-mail
        list_alt.pop(0)
        return mensagem
        
    if (auxemail == "finalizado"):
        print('entro no salvamento')
        email.write("----------------\n De:{}\n Para: {}\n Assunto: {}\n Mensagem: {}\n".format(de, email_envia, assunto, mensagem)) # Escreve no arquivo
        print("E-mail enviado")
        email.close() # Fecha o arquivo
        return email

main()
