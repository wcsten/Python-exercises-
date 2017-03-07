# O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do
# distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor
# seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro,
# calcular e escrever o custo final ao consumidor.


f_price = float(input('Preço do custo de Fabrica:'))
dist_porcent = 28
tax = 45

distribuidor = (f_price * dist_porcent) / 100
taxa = (f_price * tax) / 100

total = distribuidor + taxa + f_price

print(total)
