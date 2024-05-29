#01 crear una lista de 5 alumnos cada alumno almacenaremos su nombre 
# apellidos edad 

# insertar al final de la lista los datos de antoni 

# eliminar de la lista si existe los datos de abel 

# buscar y mostrar el alumnos en la posicion 4 de la lista 

lista_alumnos=[
    {
        "nombre":"miguel",
        "apellidos":"quispe",
        "edad":18
    },{
        "nombre":"maria",
        "apellidos":"santaria",
        "edadad":13
    },{
        "nombre":"luis",
        "apellidos":"huamani",
        "edad":29
    },{
        "nombre":"mari luz",
        "apellidos":"lume",
        "edad":15
    },{
        "nombre":"mari luz",
        "apellidos":"lume",
        "edad":15   
    }
]
lista_nueva=[
    {
         "nombre":"antony",
          "apellidos":"roman",
          "edad":25 
    }
]
lista_alumnos.append(lista_nueva)
print(lista_alumnos)


