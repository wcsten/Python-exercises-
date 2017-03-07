# Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos
# brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total
# de eleitores.

population = int(input('Digite o total da população da cidade: '))
null = int(input('Digite o numero de votos nulos: '))
whites = int(input('Digite o numero de votos em branco: '))

valids = (population - null) - whites

percentual_null = null * 100 / population
percentual_whites = whites * 100 / population
percentual_valids = valids * 100 / population

print('nulos {} %'.format(percentual_null))
print('brancos {} %' .format(percentual_whites))
print('validos {} %' .format(percentual_valids))
