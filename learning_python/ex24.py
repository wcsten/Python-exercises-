# Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. Sabendo-se que
# ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que
# ultrapassar este valor, calcular e escrever o seu salário total.

salario = float(input('Salario fixo:'))
vendas = float(input('Valor de vendas:'))

if vendas <= 1500:
    salario = salario + ((3 / 100) * vendas)
    print(salario)
else:
    venda_bonus = vendas - 1500
    bonus_cinco = (5 / 100) * venda_bonus
    bonus_tres = (3 / 100) * 1500
    salario = salario + bonus_tres + bonus_cinco
    print(salario)
