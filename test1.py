# Video 6 - if + Operadores de Comparacion

num1 = int(input("ingrese 1er nota: "))
num2 = int(input("ingrese 2da nota:"))
num3 = int(input("ingrese 3er nota:"))

prom = ( num1 + num2 + num3)/3

print("el PROMEDIO es %f"%prom)

if(prom > 6):
    print("Aprobado")
else:
    print("Desaprobado")