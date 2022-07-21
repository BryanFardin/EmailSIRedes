registro = open('registros.txt', 'r') # Abre o arquivo
def login(): # Função para logar
    usuario = str(input('Digite seu nome: '))
    return usuario

def registrar(): # Função para registrar
    senha = str(input('Digite uma Senha: '))
    registro = open('registros.txt', 'a')
    registro.write('----------------\nUsuario: {}\nSenha: {}\n'.format(usuario, senha)) # Escreve no arquivo os usuários e senhas
    registro.close()
def extrair(): # Função para extrair os usuários
    registro = open('registros.txt', 'r') # Abre o arquivo
    registro = list(registro) # Converte o arquivo em uma lista
    
    count = 1
    nomes = []
    senhas = []
    aux = []

    for item in registro: # Separa os usuários e senhas
        item = item.strip('\n')
        if count == 1:
            aux.append(item)
            aux.pop()
            count = 3
            
        elif count == 2: # Separa os usuários
            senhas.append(item)
            count = 1
            
        elif count == 3: # Separa as senhas
            nomes.append(item)
            count = 2

    zipado = zip(nomes, senhas) # Faz um zip dos usuários e senhas
    users = dict(zipado) # Faz um dicionário com os usuários e senhas
    return users # Retorna o dicionário

def verificar(): # Função para verificar se o usuário existe
    users = extrair() # Chama a função extrair
    if users.get('Usuario: '+usuario) == ('Senha: '+senha): # Verifica se o usuário e senha existem
        return True # Se existir, retorna True
    else:
        return False # Se não existir, retorna False

usuario = login() # Chama a função login

if 'Usuario: '+usuario+'\n' in registro: # Verifica se o usuário existe
    senha = str(input('Digite uma Senha: ')) # Senha do usuário
    verificar() # Chama a função verificar
    if verificar() == True: # Se o usuário existir
        print('Logado com Sucesso')
    else:   # Se o usuário não existir
        print('Senha Invalida!')
        exit() # Sai do programa
else: # Se o usuário não existir
    print('Opa!, vi que este usuario não possui cadastro, deseja se cadastarar?')
    print('Digite:\n 1 -> SIM\n 0 -> NAO ')
    opção = int(input()) # Opção do usuário
    if opção == 0:
        print('Por Favor Digite um Usuario Valido!')
        login()
    if opção == 1:
        registrar()       # Chama a função registrar