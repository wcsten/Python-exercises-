def cadastrar(nomes):
    print('Digite o nome:')
    nome = input()
    nomes.append(nome)

def procurar(nomes):
    print('Digite o nome que deseja procurar:')
    nome = input()

    if nome in nomes:
        print('O nome {} está cadastrado!' .format(nome))
    else:
        print('O nome {} não está cadastrado!' .format(nome))

def listar(nomes):
    print('Listando nomes: ')
    for nome in nomes:
        print(nome)

def alterar(nomes):
    print('Digite o nome que deseja alterar: ')
    nome_a_alterar = input()

    if nome_a_alterar in nomes:
        posicao = nomes.index(nome_a_alterar)
        print('Digite o nome novo:')
        nome_novo = input()
        nomes[posicao] = nome_novo

def menu():
    nomes = []
    escolhe = ''

    while escolhe != '0':
        print('Digite 1 para cadastrar, Digite 2 para procurar, 3 para listar, 4 atualizar nome, ou 0 para sair.')
        escolhe = input()

        if escolhe == '1':
            cadastrar(nomes)
        elif escolhe == '2':
            procurar(nomes)
        elif escolhe == '3':
            listar(nomes)
        elif escolhe == '4':
            alterar(nomes)
menu()
