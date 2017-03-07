# A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais
# de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%.
# Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva
# o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas
# (considere que o mês possua 4 semanas exatas).

horas_mes = int(input('Numero de horas trabalhadas: '))
ganho_hora = float(input('Preço hora: '))

if horas_mes > 180:
    total_bonus = ((horas_mes - 180) * ganho_hora) * 1.5
    hora_salario = horas_mes - 180
    salario_sem_bonus = (horas_mes - hora_salario) * ganho_hora
    total = salario_sem_bonus + total_bonus
    print(total)
else:
    total = horas_mes * ganho_hora
    print(total)
