#4. Programa que divide a los alumnos en grupos A y B:

nombre = input("Por favor, introduce tu nombre: ")
sexo = input("Introduce tu sexo (M para mujer, H para hombre): ")

if (sexo == 'M' and nombre[0].upper() < 'M') or (sexo == 'H' and nombre[0].upper() > 'N'):
    print("Perteneces al grupo A.")
else:
    print("Perteneces al grupo B.")
#5  Escribir un programa para una empresa que tien salas de juegos para todas las edades y quiere cacular de forma automatica el precio que debe cobrar a sus clientes por entrar.
# el programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada .
# si el cliente es menor de 4 años puede entrar gratis , si tiene entre 4 y 18 años debe pagar S/5 y si es mayor de 18 años , S/ 10.
edad=int(input("por favor ingrese su edad: "))
if edad <4:
    print("puede ingresar sin pagar")
if edad >=4 and edad <18:
    print("usted tiene que pagar un monto de S/ 5")
if edad >18:
    print("usted tiene que pagar por su edad un monto de S/10")