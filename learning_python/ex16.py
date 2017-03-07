# As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem
# compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e
# escreva o custo total da compra.

apple = int(input('Digite quantas maçãs deseja comprar:'))

if apple >= 12:
    total = apple * 1.00
else:
    total = apple * 1.30

print(total)
