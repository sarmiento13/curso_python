# lista="hola"
# lista_texto=list(lista)
# lista2=[e for e in lista]

# texto_largo="hola como esta bienvenido al salon"
# nueva_lista=texto_largo.split(" ")
# print(" ".join(nueva_lista))

# # DATOS PRIMITIVO
# nombre="abel"
# otro_nombre=nombre
# print(id(nombre))
# print(id(otro_nombre))

# # DATOS ESTRUCTURADOS
# lista_original=(1,2,3,4)
# copia_lista=lista_original

# lista_original[-1]=15
# print(copia_lista)


# crear un programa que reciba una lista desordenada y muestre por terminal la lista ordenada y la lista previa a ser ordena.
# lista=[3,4,5,1,2,6,8,9,7]
# copia_lista=lista.copy()
# copia_lista.sort()
# print(lista)
# print(copia_lista)
# con diccionario
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
alumnos[0]={"nombre":"mafer","edad":15}
alumnos[1]["sexo"]="por defenir"
print(alumnos)