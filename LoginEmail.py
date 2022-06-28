registro = open('registros.txt', 'r')
def login():
    usuario = str(input('Digite seu nome: '))
    return usuario

def registrar():
    senha = str(input('Digite uma Senha: '))
    registro = open('registros.txt', 'a')
    registro.write('----------------\nUsuario: {}\nSenha: {}\n'.format(usuario, senha))
    registro.close()

def extrair():
    registro = open('registros.txt', 'r')
    registro = list(registro)
    
    count = 1
    nomes = []
    senhas = []
    aux = []

    for item in registro:
        item = item.strip('\n')
        if count == 1:
            aux.append(item)
            aux.pop()
            count = 3
            
        elif count == 2:
            senhas.append(item)
            count = 1
            
        elif count == 3:
            nomes.append(item)
            count = 2

    zipado = zip(nomes, senhas)
    users = dict(zipado)
    return users

def verificar():
    users = extrair()
    if users.get('Usuario: '+usuario) == ('Senha: '+senha):
        return True
    else:
        return False

usuario = login()

if 'Usuario: '+usuario+'\n' in registro:
    senha = str(input('Digite uma Senha: '))
    verificar()
    if verificar() == True:
        print('Logado com Sucesso')
    else:
        print('Senha Invalida!')
        exit()
else:
    print('Opa!, vi que este usuario não possui cadastro, deseja se cadastarar?')
    print('Digite:\n 1 -> SIM\n 0 -> NAO ')
    opção = int(input())
    if opção == 0:
        print('Por Favor Digite um Usuario Valido!')
        login()
    if opção == 1:
        registrar()      
#with open('{}.txt'.format(usuario), 'w') as usuario:
    #usuario.write(str(input('Corpo Email:')))
