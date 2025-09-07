#Ejercicio1_numerosDel0Al100
num=0 
for num in range (0,101,1):
   print (num) 
#Ejercicio2_digitosNumeros
numero=int(input("Ingrese un numero entero"))
desglose=numero
digitos=0
while desglose>=1:
    digitos= digitos+1
    desglose= desglose/10
print(f"El numero{numero} tiene {digitos} digitos.")
# Ejercicio3_sumaEntreNumeros
num1 = int(input("Ingrese primer valor: "))
num2 = int(input("Ingrese segundo valor: "))
num3 = 0
if num1 > num2:
    num3=num1
    num1=num2
    num2=num3
sumatoria = 0
for i in range(num1 + 1, num2): 
    sumatoria += i
print(f"La sumatoria de los números entre {num1} y {num2} es: {sumatoria}")
#Ejercicio4_SumaEnSecuencia
numero= int(input("Ingrese un numero entero distinto de 0 :"))
sumatoria= 0
while numero != 0:
    sumatoria=sumatoria+numero
    numero=int(input("Ingrese otro numero distinto de 0 :"))
print(f"la sumatoria d elos numero ingresados es de {sumatoria}")
#Ejercicio5_JuegoAzar
import random
azar = random.randint(0,9)
intentos = 0
numero = int(input("Elige un número entre 0 y 9: "))
while numero != azar:
    if numero < 0 or numero > 9:
        print("Debes ingresar un número entre 0 y 9.")
    else:
        intentos += 1
    numero = int(input("Elige un número entre 0 y 9: "))
intentos = intentos + 1  
print("Felicitaciones!! Has ganado.")
print(f"Número de intentos: {intentos}")
#Ejercicio6_NumerosParesDe100A0
for numero in range(100,-1,-2):
    print(numero)
#Ejercicio7_SumatoriaEntre0aXNumero
numero = int(input("Ingrese un valor entero: "))
sumatoria = 0
if numero < 0:
    print("El número ingresado es negativo. Por favor ingrese un número positivo.")
else:
    for i in range(numero + 1):
        sumatoria = sumatoria + i
    print(f"La sumatoria de 0 a {numero} es de {sumatoria}")
#Ejercicio8_NumerosPpareImparesPositivosNegativos
positivo=0
negativo=0
par=0
impar=0
for i in range (1,101,1):
    numero= int(input("Ingrese un valor"))
    if numero >0:
        positivo= positivo+1
    else:
        negativo=negativo+1
    if numero % 2 == 0:
        par=par+1
    else:
        impar=impar+1
print(f"Se ingresaron {positivo} positivos")
print(f"Se ingresaron {negativo} negativos")
print(f"Se ingresaron {par} pares")
print(f"Se ingresaron {impar} impares")
#Ejercicio9_MediaDe100numeros
sumatoria=0
cant_numeros=100
for i in range(100):
    numero=int(input("Ingrese un numero entero: " ))
    sumatoria=sumatoria+numero
print("La media de los valores ingresados es", (sumatoria/cant_numeros))
#Ejercicio10_ValoresInvertidos
numero=int(input("Ingrese un numero entero: "))
invertido = 0
while numero > 0:
    digito = numero % 10            
    invertido = invertido * 10 + digito
    numero = int(numero/10)             
print(f"El número invertido es: {invertido}")
