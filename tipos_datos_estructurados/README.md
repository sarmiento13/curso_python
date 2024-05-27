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