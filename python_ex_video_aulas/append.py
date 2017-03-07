"""
Faça um programa que leia um vetor de 5 númeors inteiros e mostre-os.
"""
vetor = []
for i in range(1, 6):
    num = int(input("Digite um numero {} de 5:".format(i)))
    vetor.append(num)
for i in vetor:
    print(i)
