#Ejercicio1EdadUsuario
edad= int (input("Por favor ingrese su edad:"))
if edad >= 18:
    print("Es mayor de edad")
#Ejercicio2NotaUsuario
nota = int (input("Por favor ingrese su nota:"))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
#Ejercicio3NumerosPares
numero = int (input("Por favor ingrese un numero par:"))
if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar por favor ingrese un numero par")
#Ejercicio4CategoriaPorEdad
edad=int(input("Por favor ingrese su edad:"))
if edad <12:
    print("Ninio")
elif edad >=12 and edad <18:
    print("Adolescente")
elif edad >=18 and edad <30:
    print("Adulto joven")
else:
    print("Adulto")
#Ejercicio5Contrasenia
contrasenia =len( input("Por favor ingres una clave de 8 a 14 caracteres"))
if contrasenia<8 or contrasenia >14:
    print("Porfavor ingrse una clave de 8 a 14 caracteres")
else:
    print("Clave correcta")
#Ejercicio6ModaMediaMediana
import random
numeros_aleatorios = [random.randint(1, 100)for i in range(25)]
from statistics import mode , median , mean
moda=mode (numeros_aleatorios)
mediana=median(numeros_aleatorios)
media=mean(numeros_aleatorios)
if  moda > mediana and mediana > media:
    print("Sesgo negativo")
elif moda <mediana and mediana < media:
    print("Sesgo positivo")
else:
    print("Sin sesgo")
#Ejercicio7FraseUsuario!
frase = input("Por favor, ingrese una frase:")
ultima_letra = frase [-1]
print (ultima_letra)
if ultima_letra == "a" or ultima_letra =="e" or ultima_letra =="i" or ultima_letra =="o" or ultima_letra =="u":
    print(f"{frase}!!")
else:
    print(frase)
#Ejercicio8NombreUsuario
nombre = input("Ingrese su nombre:")
mayuscula = int(input("Ingrese 1 si quiere todo su nombre en mayuscula" \
" 2 si quiere todo su nombre en minuscula o " \
"3 si solo quiere la primer letra en mayuscula"))
if mayuscula == 1:
    print (nombre.upper())
elif mayuscula == 2:
    print (nombre.lower())
elif mayuscula == 3:
    print (nombre.title())
else:
    print ("Opcion seleccionada incorrecta")
#Ejercicio9MagnitudTerremoto
magnitud= int(input("Por favor ingrese la magnitud del terremoto seg'un escala de Richter"))
if magnitud< 3:
    print("Muy leve")
elif magnitud>=3 or magnitud <4:
    print("Leve")
elif magnitud>=4 or magnitud<5:
    print("Moderado")
elif magnitud>= 5 or magnitud<6:
    print("Fuerte")
elif magnitud>=6 or magnitud<7:
    print("Muy Fuerte")
else:
    print("Extremo")
#Ejercicio10EstacionesDelAnio
hemisferio= input("Ingrese hemisferio en el que se encuentra: Norte o Sur").lower()
mes= input("Ingrese fecha del anio en el que se encuentra en formato dd/mm")

if hemisferio == "sur":
    if mes >= "21/12" or mes<= "20/03":
        print("Verano")
    elif mes>= "21/03" or mes<= "20/06":
        print("Otonio")
    elif mes>= "21/06" or mes <= "20/09":
        print("Invierno")
    elif mes>= "21/09" or mes <= "20/12":
        print("Primavera")
elif hemisferio == "norte":
    if mes >= "21/12" or mes<= "20/03":
        print("Invierno")
    elif mes>= "21/03" or mes<= "20/06":
        print("Primavera")
    elif mes>= "21/06" or mes <= "20/09":
        print("Verano")
    elif mes>= "21/09" or mes <= "20/12":
        print("Otonio")
else:
    print("Error, por favor ingrese hemisferio (norte o sur) y fecha (dd/mm)")#Ejercicio10EstacionesDelAnio
hemisferio= input("Ingrese hemisferio en el que se encuentra: Norte o Sur").lower()
mes= input("Ingrese fecha del anio en el que se encuentra en formato dd/mm")

if hemisferio == "sur":
    if mes >= "21/12" or mes<= "20/03":
        print("Verano")
    elif mes>= "21/03" or mes<= "20/06":
        print("Otonio")
    elif mes>= "21/06" or mes <= "20/09":
        print("Invierno")
    elif mes>= "21/09" or mes <= "20/12":
        print("Primavera")
elif hemisferio == "norte":
    if mes >= "21/12" or mes<= "20/03":
        print("Invierno")
    elif mes>= "21/03" or mes<= "20/06":
        print("Primavera")
    elif mes>= "21/06" or mes <= "20/09":
        print("Verano")
    elif mes>= "21/09" or mes <= "20/12":
        print("Otonio")
else:
    print("Error, por favor ingrese hemisferio (norte o sur) y fecha (dd/mm)")