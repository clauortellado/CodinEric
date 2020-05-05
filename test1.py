# Video 6 - if + Operadores de Comparacion

'''
num1 = int(input("ingrese 1er nota: "))
num2 = int(input("ingrese 2da nota:"))
num3 = int(input("ingrese 3er nota:"))

prom = ( num1 + num2 + num3)/3

print("el PROMEDIO es %.2f"%prom)

if(prom > 6):
    print("Aprobado")
else:
    print("Desaprobado")
'''
# Video 7 - while

num = int(input("ingresar nota: "))

total = 0
cant = 0
while(num != 0):
    if (num > 0 and num < 11):
    total = total + num
    cant = cant + 1
    num = int(input("ingresar nota: "))
else:
    num = int(input("ingresar nota entre 1 y 10 - 0 para salir "))

print("suma notas: %.2f - cant notas: %i"% (total,cant))
print("cant notas: %i"%cant)
prom = total/cant
print("promedio: %.2f"%prom)
