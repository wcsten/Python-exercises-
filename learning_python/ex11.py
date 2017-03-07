# Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês,
# mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele
# efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas
# vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do
# vendedor.



pay = float(input('Salario:'))
comissao = float(input('Valor da comissão pra cada carro vendido: '))
carros = int(input('Quantidade de carros vendidos: '))
valor_vendas = float(input('Valor total mensal: '))


valor_comissao = comissao * carros
porcentagem_vendas = 5/100 * valor_vendas

total = pay + valor_comissao + porcentagem_vendas

print(total)
