# -*- coding: UTF-8 -*-
def procurar_regex(nomes):
	print 'Digite a expressão regular'
	regex = raw_input()
	nomes_concatenados = ' '.join(nomes)
	resultados = re.findall(regex, nomes_concatenados)
	print(resultados)

def procurar(nomes):
    print 'Digite nome a procurar:'
    nome_a_procurar = raw_input()

    if (nome_a_procurar in nomes):
    	print 'Nome %s está cadastrado' %(nome_a_procurar)
    else:	
    	print 'Nome %s não está cadastrado' %(nome_a_procurar)

def alterar(nomes):
	print 'Qual nome você gostaria de alterar?'
	nome_a_alterar = raw_input()

	if (nome_a_alterar in nomes):
		posicao = nomes.index(nome_a_alterar)
		print 'Digite novo nome:'
		nome_novo = raw_input()
		nomes[posicao] = nome_novo

def remover(nomes):
    print 'Qual nome gostaria de remover?'
    nome = raw_input()
    nomes.remove(nome)

def listar(nomes):
	print 'Listando nomes:'
	for nome in nomes:
		print nome

def cadastrar(nomes):
	print 'Digite o nome: '
	nome = raw_input()
	nomes.append(nome)

def menu():
	nomes = []
	escolhe = ''
	while(escolhe != '0' ):
		print 'Digite: 1 para cadastrar, 2 para listar, 3 para remover, 4 para alterar, 5 para procurar, 6 para expressão regular, 0 para terminar'
		escolhe = raw_input()

		if (escolhe == '1'):
			cadastrar(nomes)

		if(escolhe == '2'):
			listar(nomes)
		
		if(escolhe == '3'):
			remover(nomes)

		if(escolhe == '4'):
			alterar(nomes)

		if(escolhe == '5'):
			procurar(nomes)
		if(escolhe == '6'):
			procurar_regex(nomes)	
menu()
					