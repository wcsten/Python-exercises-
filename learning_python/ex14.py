# Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso
# contrário escrever NÃO É MAIOR QUE 10!

n = float(input('Digite um numero:'))

if n > 10:
    print('MAIOR QUE 10!')
elif n == 10:
    print('É 10 CARALHO!')
else:
    print('MENOR QUE 10!')
