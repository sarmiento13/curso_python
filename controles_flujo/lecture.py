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

# crear un programa que me cuente la cantidad de comas y me meustre 
# sus indices
oracion:str=input("escribe una oracion con comas:")
contador:int=0
for n in range(0,len(oracion)):
     if oracion[n]==",":
          contador+=1
          print(f"coma encontrada en el indice {n} ")   
print(f"la cantidad de comas es {contador}")
    
          
         