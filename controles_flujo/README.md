# controles de flujos 
todos los programas trabajan a travez de intruciones ordenadas.
existen maneras de romper con el flujo normal de los programas creando `bifurcaciones` o creando `repeticion` de intruciones 
## deciciones
### la sentencia if
la sentencia de decicion en python es `if` en su escritura debemos añadir una **exprecion  de comparacion** terminando con `:` al final de la linea 
> ejemplo:

```python
if rue:
    print("es verdad")
```
- ## Estructura if-else
 **Permite ejecutar un bloque de código si se cumple una condición, y otro bloque de código si no se cumple.**
>Ejemplo:
```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
 ```
- ## Estructura if-elif-else
 **Permite evaluar múltiples condiciones y ejecutar diferentes bloques de código según el resultado.**
>Ejemplo:
 ```python
nota = 80
if nota >= 90:
    print("Obtuviste una A")
elif nota >= 80:
    print("Obtuviste una B")
elif nota >= 70:
    print("Obtuviste una C")
else:
    print("Obtuviste una D")
 ```
- ## Bucle for
 **Permite iterar sobre una secuencia (como una lista o una cadena de texto) y ejecutar un bloque de código para cada elemento.**
>Ejemplo:
```python
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
 ```
- ## Bucle while
 **Permite ejecutar un bloque de código mientras se cumpla una condición.**
>Ejemplo:
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
 ```
- ## Sentencia break
 **Se utiliza para salir de un bucle de forma prematura si se cumple una condición.**
>Ejemplo:
```python
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    if numero == 3:
        break
    print(numero)
 ```
- ## Sentencia continue
 **Se utiliza para saltar a la siguiente iteración de un bucle si se cumple una condición.**
>Ejemplo:
```python
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    if numero == 3:
        continue
    print(numero)
```