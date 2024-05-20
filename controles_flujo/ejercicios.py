# # escribir un programa que pregunte al usuario su edad y 
# # muestre por pantalla si es mayor de edad o no.

# edad_usuario:int=int(input("ingrese sue edad"))
# if edad_usuario >=18:print("es mayor de edad")
# else:
#      print("no es mayor de edad")

# # escribir un programa que almacena la cadena de caracteres
# # contraseña en una variable, pregunte al usuario por la contraseña 
# # e imprime por pantalla si la contraseña intruducida por el usuario
# # coincide con la guardada en la varible sin tener en cuenta mayuscula 
# # y minusculas 

# contraseña:str="barrientos"
# password:str=input("ingrese su contraseña")
# if contraseña==password:
#     print("la contraseña coincide")
# else:
#     print("la contraseña no coincide")

# # escriba un programa que pida al usuario un numero entero posetivo y 
# # muestre por panatalla la cuenta atras desde ese numero hasta cero 
# # separados por comas

# numero=int(input(" ingrese un numero entero pocetivo "))
# if  numero <0:
#     print("ingrese su numero entero pocetivo.")
# else: 
#     cuenta_regresiva=""
#     for i in range(numero, -1,-1):
#         cuenta_regresiva+=str(i)
#         if i >0:
#             cuenta_regresiva += ","
#     print(cuenta_regresiva)

## crear un programa que me muestre la tabla de multiplicar de 1 hasta 5

# for i in range (1,6):
#     for j in range(1,13):
#         print(f"{i}x{j}={i*j}")

## crear un programa que que pida un numero y que muestre la tabla de multiplicar de ese numero

numero:int=int(input("ingrese numero:"))
for i in range(1,13):
    print(f"{numero}x{i}={i*numero}")
