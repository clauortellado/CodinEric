# Video 8
'''
Tirar 4 veces un dado1Eliminar el Valor menor
y Sumar el Total restante
'''

import random

'''
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
dado4 = random.randint(1,6)
suma = dado1 + dado2 + dado3 + dado4
menor = min(dado1, dado2, dado3, dado4)
Fuerza = suma - menor
#print("dado1: %i - dado2: %i - dado3 %i - dado4: %i"% (dado1, dado2, dado3, dado4))
print("Fuerza: %i"% Fuerza)

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
dado4 = random.randint(1,6)
suma = dado1 + dado2 + dado3 + dado4
menor = min(dado1, dado2, dado3, dado4)
Destreza = suma - menor
#print("dado1: %i - dado2: %i - dado3 %i - dado4: %i"% (dado1, dado2, dado3, dado4))
print("Destreza: %i"% Destreza)

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
dado4 = random.randint(1,6)
suma = dado1 + dado2 + dado3 + dado4
menor = min(dado1, dado2, dado3, dado4)
Constitucion = suma - menor
#print("dado1: %i - dado2: %i - dado3 %i - dado4: %i"% (dado1, dado2, dado3, dado4))
print("Constitucion: %i"% Constitucion)

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
dado4 = random.randint(1,6)
suma = dado1 + dado2 + dado3 + dado4
menor = min(dado1, dado2, dado3, dado4)
Inteligencia = suma - menor
#print("dado1: %i - dado2: %i - dado3 %i - dado4: %i"% (dado1, dado2, dado3, dado4))
print("Inteligencia: %i"% Inteligencia)

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
dado4 = random.randint(1,6)
suma = dado1 + dado2 + dado3 + dado4
menor = min(dado1, dado2, dado3, dado4)
Sabiduria = suma - menor
#print("dado1: %i - dado2: %i - dado3 %i - dado4: %i"% (dado1, dado2, dado3, dado4))
print("Sabiduria: %i"% Sabiduria)

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
dado4 = random.randint(1,6)
suma = dado1 + dado2 + dado3 + dado4
menor = min(dado1, dado2, dado3, dado4)
Carisma = suma - menor
#print("dado1: %i - dado2: %i - dado3 %i - dado4: %i"% (dado1, dado2, dado3, dado4))
print("Carisma: %i"% Carisma)
'''

mis_dados = [4,5,6,2]
print(mis_dados)
mis_dados.sort()
print(mis_dados)
print("option1___________")
dados_min = min(mis_dados)
print(dados_min)
altos = sum(mis_dados)-dados_min
print(altos)
print("option2___________")
dados_altos = mis_dados[1:]
print(dados_altos)
altos = sum(dados_altos)
print(altos)
