# # # return devuelve valores que podre hacer uso 
# # # crea una funcion que retorno el numero 10 y muestra terminal si es par
# # # siempre que el valor retorne mi funcion se utilize en mas sentencia u operaciones hacer uso de return
# # def dies():
# #     return 10
# # if dies()%2==0:
# #     print("es par")
# # else:
# #     print ("es impar")

# # # prin solo muestra por terminal 

# # # crear una funcion que me muestre el producto de dos numeros 
# # def producto(a,b):
# #     return a*b

# # # crear una funcion que me retorne una lista de tres numeros
# # def  lista_numeros():
# #     return [3,2,6]

# # # print usaremos cada ves que nuestro funcion retorne un mensaje 

# # # crear una funcion que por parametro reciva un nombre y retorne un mensaje de bienvenida con el nombre 
# # def mensaje(nombre):
# #     print(f"hola, {nombre}, bienvenido al chongo")
# # # mensaje("jose")

# # # crear un funcion que reciba por parametro una lista de numeros y me devuelva el numero menor, mostrar por terminal
# # # el valor retornado por la funcion 
# # lista=[4,3,6,78,7]
# # def Min(l):
# #     minimo=l[0]
# #     for n in l:
# #         if n < minimo:
# #             minimo=n
# #     return minimo
# # print(Min(lista))

# # Crear una funcion que reciva como parametro el nombre y la edad de una persona mi funcion devera retornar un diccion 
# # con los datos, luego muestrar por terminal el valor de retorno de mi funcion
# nombre="luis"
# edad=12
# def persona(nom,edad):
#     return dict(
#         nombre=nom,
#         edad=edad
#     )
# print(persona(nombre.edad))

##  empaquetado y desempaqueta de argumento nominales 
# def alumnos(**kwargs):
#     kwargs["nombre"]="abel"
#     print(kwargs)
# alumnos(nombres="miguel",apellidos="largo",edad=30)

## ejemplos de lambda
# saludo=lambda:"hola"
# print(saludo())

# crear un programa anonimo que recibe como parametro una lista de 5 numeros y retorne dos listas 
# una con los numeros pares y otra con numeros impares 
list=[1,2,3,4,5]
pares=lambda l:[n for n in list if n%2==0]
impares=lambda l:[n for n in list if n%2!=0]
print(pares(list))
print(impares(list))

int (input())

def mensaje(m):
    print(m)

def pedir_nombre():
    nombre=input("ingresa tu nombre")
    return nombre
mensaje(pedir_nombre())