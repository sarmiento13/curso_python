# STRINS
En Python, **las cadenas de texto (strings)** se utilizan para **representar secuencias de caracteres.** Aquí tienes un resumen de cómo trabajar con cadenas de texto en Python, junto con algunos ejemplos:
 
- ## Declaración de una cadena de texto
 **Para declarar una cadena de texto en Python, se pueden utilizar comillas simples `('')`, comillas dobles `("")` o triple comillas dobles `(""")`.**
>Ejemplo:
 ```python
nombre = "Juan"
mensaje = 'Hola, ¿cómo estás?'
parrafo = """Este es un párrafo
que ocupa varias líneas"""
```
- ## Acceso a caracteres
 **Se puede acceder a caracteres individuales de una cadena utilizando el índice entre corchetes `([])`. Los índices comienzan desde 0 para el primer carácter.**
>Ejemplo:
 ```python
nombre = "Juan"
print(nombre[0])  # Output: J
print(nombre[2])  # Output: a
 ```
 
- ## Longitud de una cadena
**Se puede obtener la longitud de una cadena utilizando la función `len()`.**
>Ejemplo:
 ```python
nombre = "Juan"
longitud = len(nombre)
print(longitud)  # Output: 4
```
- ## Concatenación de cadenas
**Para unir o concatenar dos o más cadenas de texto, se utiliza el operador de suma `(+)`.**
>Ejemplo:
```python
nombre = "Ana"
apellido = "Gómez"
nombre_completo = nombre + " " + apellido
print(nombre_completo)  # Output: Ana Gómez
```
- ## Métodos de cadenas
 **Python proporciona una variedad de métodos integrados para manipular cadenas de texto, como convertir a `mayúsculas, minúsculas, dividir en palabras, reemplazar caracteres`, entre otros.**
>Ejemplo:
```python
mensaje = "Hola, cómo estás?"
print(mensaje.upper())  # Output: HOLA, CÓMO ESTÁS?
print(mensaje.split())  # Output: ['Hola,', 'cómo', 'estás?']
print(mensaje.replace("estás", "te encuentras"))  # Output: Hola, cómo te encuentras?
 ``` 
- ## Formateo de cadenas
 **Python ofrece diferentes formas de formatear cadenas, como el método format`()` y `las f-strings (cadenas formateadas)`.**
>Ejemplo:
 ```python
nombre = "María"
edad = 30
saludo = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)
print(saludo)  # Output: Hola, mi nombre es María y tengo 30 años.
saludo_fstring = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(saludo_fstring)  # Output: Hola, mi nombre es María y tengo 30 años.
```
 