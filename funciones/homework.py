## crear una funcion que reciba por argumento n numeros 
# y retorne una lista con los numeros pares 

# def numeros_pares(*args):
#     list_pares = []
#     for m in args:
#         if m % 2 == 0:
#             list_pares.append(m)
#     return list_pares
# print(numeros_pares(8,5,4,7,9,25,4,7,12))

## crear tres funciones para los siguientes caso
# calcular el numero menor 
# calcular el numero mayor
# calcular la suma de todos los numero
# se le pasara por argumento n numero 
### 01
def encontrar_menor(*numeros):
    return min(numeros, default=None)

def encontrar_mayor(*numeros):
    return max(numeros, default=None)

def calcular_suma(*numeros):
    return sum(numeros)

numeros = (5, 8, 3, 12, 6, 9)
menor = encontrar_menor(*numeros)
mayor = encontrar_mayor(*numeros)
suma_total = calcular_suma(*numeros)

print(f"Números: {numeros}")
print(f"Número menor: {menor}")  
print(f"Número mayor: {mayor}")   
print(f"Suma total: {suma_total}")

### 02
def Min(*args):
    menor=args[0]
    for n in args:
        if n<menor:
            menor=n
    return menor
def Max(*args):
    mayor=args[0]
    for n in args:
        if n>mayor:
            mayor=n
    return mayor
def Sum(*args):
    suma=0
    for n in args:
        suma+=n
    return suma

valores=4,7,8,5,2,1
print(Min(*valores))
print(Max(*valores))
print(Sum(*valores))



