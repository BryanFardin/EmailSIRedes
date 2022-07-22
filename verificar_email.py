import login as log

def verificar_email(): # Função para verificar e-mail
    with open ("caixa de entrada/email.txt", "r") as email: # Abre o arquivo
        linha = email.readlines() # Le o arquivo
        cont = 0 # Contador
        usuario = log.usuario # Usuário logado
        if data == "contador":
            for i in linha:

                if 'Para: '+usuario+'\n' in i: # Verifica se o usuário tem e-mail
                    cont += 1
            texto = f"""
            Você tem {cont} e-mails

            ----------------

            Deseja visualizar um e-mail? (s/n)
            """
            return texto
        
        if data == "s": # Se o usuário desejar visualizar um e-mail
            texto = """
            Digite o número do e-mail que deseja visualizar
            """
            return texto

            for i in range(len(linha)):
                if 'Para: '+usuario+'\n' in linha[i]: # mostra pro usuario seus e-mail
                    for j in linha:
                        if j == linha[numero]:
                            print(j) # Mostra a pessoa que enviou o e-mail
                            print(linha[numero+1]) # Mostra para quem é o e-mail
                            print(linha[numero+2]) # Mostra o assunto do e-mail
                            print(linha[numero+3]) # Mostra a mensagem do e-mail                         
                    if linha == '':
                        break
            
            

def enviar_email(): # Função para enviar e-mail
    email = open("caixa de entrada/email.txt", "a") # Abre o arquivo
    de = log.usuario # Usuário logado
    email_envia = input("para quem você deseja enviar: ") # Usuário que recebe o e-mail
    assunto = input("assunto: ") # Assunto do e-mail
    mensagem = input("mensagem: ") # Mensagem do e-mail
    email.write("----------------\n De:{}\n Para: {}\n Assunto: {}\n Mensagem: {}\n".format(de, email_envia, assunto, mensagem)) # Escreve no arquivo
    print("E-mail enviado")
    email.close() # Fecha o arquivo
    return email # Retorna o arquivo


