# Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade
# dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.

years = float(input('Digite quantos anos voce tem:'))
months = float(input('Digite quantos meses:'))
days = float(input('Digite quantos dias:'))

total = (years * 365) + (months * 30) + days

print(total)
