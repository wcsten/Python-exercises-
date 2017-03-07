# Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste.
# Calcular e escrever o valor do novo salário.

pay = float(input('Digite o valor do salario mensal atual: '))
reajust = float(input('Digite o percentual de reajuste: '))

total = pay + (reajust / 100 * pay)

print('salario com reajuste {}' .format(total))
