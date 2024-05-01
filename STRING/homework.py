nombre=str=input("ingrese su nombre:")
apellido=str=input("ingrese apellido:")
nombre_apellido:str=nombre+apellido
print(nombre_apellido)

#3. Programa que muestra el número de teléfono sin prefijo ni extensión:

telefono = input("Introduce un número de teléfono con formato +34-XXXXXXXXX-XX: ")

numero_sin_prefijo_extension = telefono[5:15]
print("Número de teléfono sin prefijo ni extensión:", numero_sin_prefijo_extension)