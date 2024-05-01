# crea un programa que calcule el promedio de tres numeros ingresados por el usuario
numero1:int=int(input("ingrese un numero: "))
numero2:int=int(input("ingrese el segundo numero: "))
numero3:int=int(input("ingrese el tercer numero: "))
promedio=(numero1+numero2+numero3)/3
print(promedio)

# escribe un programa que calcule el area de un circulo pide al usuario que ingrese el radio y muestre el area
radio:float=float(input("ingrese el radio de un circulo: "))
pi:float=3.1416
area_circulo=pi*radio**2
print(area_circulo)

# escribe un programa que determine si un numero ingresado por el usuario esta par o impar
numero_ingresado:int=int(input("ingrese un numero entero: "))
resto=numero_ingresado%2
condicion:bool=resto==0
print(condicion)



#crea un programa que pida al usuario dos numeros y determine si el primero es mayor que el segundo
primer_numero:int=int(input("ingrese el primer numero: "))
segundo_numero:int=int(input("ingrese el segundo numero: "))
comparacion:bool=primer_numero > segundo_numero
print(comparacion)