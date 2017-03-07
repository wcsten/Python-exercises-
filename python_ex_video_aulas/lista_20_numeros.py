
vetor20 = []
vetor_par = []
vetor_impar = []

for i in range(1, 20):
    num = int(input('Digite {} de 20 numeros: '.format(i)))
    vetor20.append(num)

    if num % 2 == 0:
        vetor_par.append(num)
        print(vetor_par)
    else:
        vetor_impar.append(num)
        print(vetor_impar)
