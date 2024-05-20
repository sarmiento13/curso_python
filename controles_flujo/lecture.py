# # primer ejemplo if estructurado

# edad:int=(int("escribe tu edad:"))
# if edad>=18:
#     print("eres mayor")
# else:
#     print("eres menor de edad")

# # segundo ejemplo if alamcenado en variable 

# edad_dos:int=(int("escribe tu eddad:"))
# respuesta:str="eres mayor de edad" if edad_dos>=18 else "eres menor de edad"
# print(respuesta)

# # crear un programa que me imprima las cincos vocales
# vocales:str="aeiou"
# for n in range(0,5):
#     print(vocales[n])
# # crear un programa que me  muestre los 8 primeros numeros pares

# for n in range(1,17):
#     if n%2==0:
#           print(n)
# # segunda forma
 
# contador=0
# for n in range(1,17):
#     if n%2==0:
#           contador+=1
#           print(f"{n} es par numero {contador}")
                
# # crear un programa que pida al usuario escribir una oracion 
# # y mostrar por terminal la cantidad de vocales a que tiene 
# # ese horacion 
# # ojo: SOLO LAS a MINUSCULAS
# oracion:str=input("escribe una oracion:")
# contador:int=0
# for n in range(0,len(oracion)):
#      if oracion[n]=="a":
#           contador=contador+1
# print(f"la cantidad de latras a que tengo es {contador}")      

## crear un programa que me cuente la cantidad de comas y me meustre 
# sus indices
# OJO: tiene que pedir al usuario

## primera forma de hacer:  

# oracion:str=input("escribe una oracion con comas:")
# contador:int=0
# for n in range(0,len(oracion)):
#      if oracion[n]==",":
#           contador+=1
#           print(f"coma encontrada en el indice {n} ")   
# # print(f"la cantidad de comas es {contador}")

## segunda  forma de hacer:  

# texto= "hola, como estas,espero que estes bien."
# contador=0
# indices=[] 
# for indice,caracter in enumerate(texto):
#      if caracter==",":
#         contador += 1
#         indices.append(indice)
        
# print("la cantidad de comas en el texto es:",contador)
# print("los indices de las comas en el texto son:",indices)

## tercera forma de hacer:        
 
# oracion:str=input("ingrese una horacion")
# contador:int=0
# for indice,letra in enumerate(oracion):
#     if letra == ",":
#         print(f"su indice es  {indice}")
#         contador+=1
# print(f"la cantidad de comas es {contador}")

## escribe un programa que pregunte al usuario su edad muestre por pantalla todos 
## los años que ha cumplido (desde su edad).

# edad:str=input("ingrese su edad")
# for n in range (1,edad):
#     print(f"su edad hacido cumplido {n} años")

## crear un programa que me pida el nombre de tres personas y guarde una variavle global la ultima
## letra de sus nombres.
## mustrar por pantalla la variable global  con las letras ultimas letras del nombre de cada persona 

# ultima_letra:str=""
# for _ in range (3):
#     nombre:str=input("escribe tu nombre:")
#     ultima_letra+=nombre[-1]
# print(ultima_letra)

## crear un programa que muestre por terminal las siguientes figura:
# a
# ee
# iii
# OOOO
# uuuuu

#for figura in ("a","ee","iii";"ooo","uuuu"):
 #   print(figura)

## ejercicios while

# 01
# condicion=True
# while condicion:
#     print("hola")
#     condicion=False
# # 02
# condicion=True
# while condicion:
#     eval=input("desea continuar[N/S]: ")
#     if eval=="S":
#         print("continuas en el bucle")
#         continue
#     else:
#         print("se termino el programa")
#         break
# 03
# contador=0
# while contador<=5:
#     print(contador)
#     contador+=1
# print(f"valor final{contador}:")

## >metodos de string - array
# nombre="jose"
# nombre:upper() # > la funcion upper convierte el texto en 

# nombre="ALVARES"
# nombre:lower() # > convierte el texto en minuscula

# segundo_nombre="luis"
# print(segundo_nombre.capitalize()) # > convierte la primera letra en mayuscula

## ejercios while
# crear un programa que pida la cantidad de notas que se debe registrar, luego pedira
# las notas e imprimera el promedio

notas:str=(input("ingrese las catidades de notas:"))
promedio=0
while notas==5:
    
    print(f"")

  


