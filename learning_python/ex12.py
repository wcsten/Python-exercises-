# Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor
# correspondente em graus Celsius (baseado na fórmula abaixo):
# C
# ----------
# 5
# =
# F - 32
# -----------
# 9

f = float(input('Digite a temperatura em Fahrenheit: '))

c  = (f - 32) / 1.8

print(c)
