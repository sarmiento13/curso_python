# TIPOS DE DATOS ESTRUCTURADOS (TDA - tipos de datos abstractos)
```python
# lista - sus valores o elementos se pueden actualizar, eliminar 
lista=["abel",20,5,2,.5;false,["texto",.2]]
# tupla - sus valores o elementosno pueden cer modificados o eliminados.
tupla=("abel",20,5,2,.5;false,[])

# diccionarios u objetos
# los diccionarios almacenan los datos con clve :valor
diccionario={"nombre":"antonio";"edad":15,"sexo":False}
```
-[!TIP]
- **obcervacion:** que los tipos de datos estructurados pueden alamcenaren su interior otros tipos de datos estructurados.
  
```python
lista_alumnos=[
{
    "nombre":"abel",
    "edad":20
    "amigos":["no tiene"]
},{
    "nombre":"ruth",
    "edadad":13,
    "amigos":["flor","rocio"]
},{
    "nombre":"jose ma"
    "edad":80
},{
    "nombre":"ronny
    "edad":15
}
]
```

## metodos
### 1. convertir texto a lista
```python
# Metodo list
texto="hola"
list(texto)
#["h","o","l", "a"]

# metodo split
texto="hola como estas, alumnitos lindo"
texto.split(",")
```
## metodo join
``` python
texto_largo="hola como esta bienvenido al salon"
nueva_lista=texto_largo.split(" ")
print(" ".join(nueva_lista))
```

### 2 agregar elemntos al final de una lista
```python
# metodo append - es el metodo que me permite agregar elementos al final de una lista 
lista=["hola"]
lista.append("mundo")
print(lista)
#["hola","mundo"]

# metodo insert - es metodo que me permite agrega elemento en cualquiera ubicacion de mi lista 
lista_nombres=["edith","ruth","luz"]
lista_nombres.insert(0, "antony")
```

### 3 Elimar elementos de una lista
```python
# METODO POP - es el metodo que elimina el ultimo elemento de una lista es el contrario de append.
lista_nombres=["edith","ruth","luz"]
lista_nombres.pop()

#  primera manera - metodo remove - este metodo elemina el por el nombre el elemento que coninicida dentro de ,mi lista 
lista_nombres=["edith","ruth","luz"]
lista_nombres.remove("ruth")

# segundo opcion - metodo pop - al pasarle po pametro un indice este lo eliminar de la lista.
lista_nombres=["edith","ruth","luz"]
lista_nombres.pop(0)
```

### 4. buscar un elemnto en una lista 
```python
lista_nombres=["edith","ruth","luz"]
indice=lista_nombres.index("ruth")
print(lista_nombres[indice])

pertenencia="edith" in lista_nombres #true False 
```
### 5.COMPARACION DE LISTAS
podemos hacer uso de las operadores de comparcion para comparar listas 
**Ejm:**
```python
compara=[1,2,3]>[1,2,4]
# 1 no por que son iguales en ambas listas
# 2 no por que son iguales en ambas listas
# 3 evalua que es menor a 4 
# entoces la primera lista es menor que la segunda lista 
print(compara)
# salida:
```
### 6. CUIDADO CON LAS COPIAS 


### 7. FE DE ERRATAS (ACTUALIZAR LISTAS)

```python
lista=[1,3,4,5,6]
lista[0]=2
print(lista)
# [2,3,4,5,6]
# modificando lista con diccionario
alumnos=[
    {
        "nombre":"abel",
        "edad":15
    },
    {
        "nombre":"anthony",
        "edad":29
    }
]
alumnos[0]["edad"]=30
alumnos[0]={"nombre":"mafer","edad":15+}
alumnos[1]["sexo"]="por defenir"
print(alumnos)
```
### 8. listas y diccionarios por compresion
es una tecnica pythonica que nos permite crear listas y diccionarios en una sola linea conbinado bucles y decisiones.
>[!NOTE]
> *VLC* value loop condicion
```python
# LISTA POR COMPRENSION
texto="1,4,8,9,6"
nueva_lista=[]
# "n" toma todos los valores de texto
for n in texto .split(","):
    # append agrega algo en la lista
    nueva_lista.append(int(n))
# aplicando la tecnica vlc "valor bucle y condicion"
texto="1,4,8,9,6"
nueva_lista=[int(n) for n in texto.split(",")if int(n)%2==0]
print(nueva_lista)
# DICCIONARIO POR COMPRENSION
lista_amigos=["abel","anthony","edith","ruth"]
diccionario={}
for _,v in enumerate(lista_amigos):
    diccionario[v]=len(v)
print(diccionario)
# aplicando el vlc
lista_amigos=["abel","anthony","edith","ruth"]
diccionario={amigo:len(amigo)for amigo in lista_amigos}
print(diccionario)
```
