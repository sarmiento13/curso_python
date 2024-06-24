# FUNCIONES
Matematicamente una funcion es una operacion que toma uno o mas valores llamados 
`argumentos` y produce un valor determinado
`resultado`
> [!note]
> todos los lenguajes de programacion tiene funciones incorporadas (`funciones internas`), y funciones creadas por el usuario (`funciones externas`)
en programacion una funcion es un subprograma, es una estructura que nos permite agrupar codigo y sus principales objetivos son:
-`NO REPETIR` fragmentos de codigo
-`REUTILIZAR` el codigo en distintos escenarios
## Estructura de una funcion 
Una funcion viene `definida` por un `nombre`, sus `parametros` y su valor de `retorno`.
una vez creada la funcion podremos solicitar su ejecucion `invocando` la funcion por su `nombre`.
## Defenir una funcion en python
para defenir una funcion en python primero utilizaremos la palabra recervada `def` seguido por el `nombre`de la funcion. A continuacion especificaremos los `parametros` con `()` si es una funcion sin parametros, `(a)` si es un funcion con parametros, si se tuviera mas de un paramatro iran separados por `:`, en la siguiente linea sin olvidar el idntado, comenzara el `cuerpo` de la funcion (micro programa ) que puede pasar 1 o mas sentencias, finalmente devera `retornar` un resultado con la palbra recervada `return`
>[!TIP]
> como retorno tambien se puede utilizar la `funcion interna`,`print ()`, para depuracion de codigo no es recomendable usralo en produccion.
> PRINT dentro de una funcion es una herramienta que se utiliza para comprobar que un funcion aga el trabjo de manera correcta.

*ejemplo:*
```python
def saludo():
    saludo="hola chivo"
    saludo_dos="como estas"
    return saludo+saludo_dos
    return f"{saludo},{saludo_dos}"
    # print(f"{saludo},{saludo_dos}")
print (saludo())
# saludo()
```
## Invocar una funcion
para invocra, (o llamar,ejecutar)una funcion solo tendremos que escribir el nombre de la funcion por ( ) parentesis. 
```python 
def saludo():
    print("hola")
# invocando la funcion 
saludo()

## Retornar un valor
las funciones pueden retornar (o devolver)un valor
```
>[!WARNING]
> No confudir print() con return, el valor retornado por return nos permite usarlo fuera de su contexto, y print() solo mostrara el literal por terminal.

## RETORNANDO MULTIPLES VALORES
El secreto es hacerlo mediante un tipo de datos estructurados
```python
def tupla():
    return 2,3,4
varios()
#retorna(2,3,4)
def lista():
    return ["hola",45]
lista()
#retorna["hola",45]
def dicc():
    return {"nombre":"jose","edad":45}
dicc()
#retorna {"nombre":"jose","edad":45}
```

## parametros  y argumentos 
si una funcion no dispuciera de valores de entrada estaria limitada en su actuacion. es por ello que los `parametros` nos permiten variar los datos que consume una funcion para optener destintos resultados 
**ejemplos**
*crear una funcion que recibe un valor numerico y devuelve su raiz cuadrada *
```python
def aqrt(valor):
    return valor**(1/2)
# NOTA: en este caso, el valor 4 es un argumento de la funcion
aqrt(4)
```

cuando llamamos  a un funcion con `argumento`, los valores de este argumentos se copian en los correspondientes `parametros` dentro de la funcion.
```python
def ejm(a,b,c):
    return a+b+c
ejm(4,5,6)
```

### Argumentios nominales 
en esta aproximacion los argumentos no son copiados en un orden especifico sino que se **asigna por nombre a cada parametro**. Ello nos permite evitar el problema de conocer o recordar cual es el orden de los parametros en la definicion de la funcion. Para utilizarlo, basta con realizar una asignacion de cada argumento en la propia llamada a la funcion.
9**ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f"""
         la cpu es de la familia {familia},
         con {num_core} cores y con una frecuencia de {frecuencia}
    """)
# haciendo uso de argumentos nominales 
build_cpu(num_core=4,ffamilia="intel",frecuencia=2.7)
```

### Argumentos posicionales 
los argumentos no son copiados en un orden especifico, en este caso debemos conocer o recorder cual es el orden de los parametros 
**ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f"""
         la cpu es de la familia {familia},
         con {num_core} cores y con una frecuencia de {frecuencia}
    """)
# haciendo uso de argumentos nominales 
build_cpu("intel",4,2.7)
```
## Parametros por defecto 
Es posible especificar **valores por defecto** en los parametros de una funcion el caso de que no se proporcione un valor al argumento en la llamada ala funcion, el parametro correspondiente tomara el valor defenido por defecto.
**ejemplo**
```python
def  alumno(nombre,app,estado="aprobado"):

alumnos("ruth","castillo")
alumnos("anthony","crucez","desaprobado")
```
# Desempaquetado/Empaquetado de argumentos(tarea)

El **desempaquetado y empaquetado de argumentos** en lenguajes de programación es una técnica que permite pasar múltiples argumentos a una función de manera más flexible y dinámica.
 
### El desempaquetado de argumentos 
  
- se refiere a pasar argumentos a una función como una lista o diccionario.

### El empaquetado de argumentos
- implica pasar argumentos a una función de manera desempaquetada, es decir, expandiendo una lista o diccionario en argumentos individuales.
 
## Partes
 
### 1. Empaquetado de Argumentos:
 
- Permite pasar múltiples argumentos a una función como una estructura única, como una lista o diccionario.
- Ayuda a simplificar la llamada a funciones con múltiples argumentos.
### 2. Desempaquetado de Argumentos:
 
- Permite pasar argumentos a una función desempaquetados, es decir, como argumentos individuales en lugar de una estructura única.
- Proporciona flexibilidad al llamar a funciones con argumentos almacenados en una lista o diccionario.
 
## Funciones
 
**- Empaquetado de Argumentos:**
 
- En Python, se puede realizar el empaquetado de argumentos utilizando el operador ` * ` para listas y  `**`  para diccionarios.
**Ejemplo en Python:**
```python

def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)
```
**- Desempaquetado de Argumentos:**
 
- En Python, se puede realizar el desempaquetado de argumentos utilizando el operador ` * ` para listas y ` **`  para diccionarios.
**Ejemplo en Python:**
```python
 Copiar
def my_function(a, b, c):
    print(a, b, c)

my_list = [1, 2, 3]
my_function(*my_list)
```
 
## Ejemplos
 
### Empaquetado de Argumentos:
 
- Enviar múltiples argumentos a una función como una lista:
```python
 
def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)
```
### Desempaquetado de Argumentos:

- Pasar argumentos desempaquetados a una función desde una lista:
```python
 Copiar
def my_function(a, b, c):
    print(a, b, c)

my_list = [1, 2, 3]
my_function(*my_list)
``` 
 
### En resumen
 **el desempaquetado y empaquetado de argumentos** en lenguajes de programación como Python proporciona una forma conveniente de trabajar con funciones que requieren múltiples argumentos de manera flexible. ¡Es una técnica muy útil en el desarrollo de software! 

# Funciones internas de python (tarea)

- En Python, **las funciones internas** son aquellas que vienen integradas en el lenguaje y están disponibles para su uso sin necesidad de importar módulos externos. Estas funciones internas son ampliamente utilizadas en `Python` y proporcionan funcionalidades útiles para realizar diversas tareas. 
 
### Funciones Internas Comunes en Python:
 
**1.  `print()  ` : Utilizada para imprimir mensajes en la consola.**
 
```python
 Copiar
print("Hola, mundo!")
``` 
**2.    `len()  ` : Devuelve la longitud de un objeto (número de elementos).**
 
```python
 Copiar
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Salida: 5
```
**3.    `type()  ` : Devuelve el tipo de un objeto.**
 
```python
 Copiar
x = 5
print(type(x))  # Salida: <class 'int'>
``` 
**4.    `input()  ` : Permite al usuario ingresar datos desde la consola.**
 
```python
 Copiar
name = input("Ingrese su nombre: ")
```
**5.    `range()  ` : Genera una secuencia de números.**
 
```python
 Copiar
for i in range(5):
    print(i)  # Salida: 0, 1, 2, 3, 4
 ```
**6.    `sum()  ` : Calcula la suma de elementos en una secuencia.**
 
```python
 Copiar
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)  # Salida: 15
``` 
**7.    `min()  `  y   ` max()  ` : Encuentran el valor mínimo y máximo en una secuencia.**
 
```python
 Copiar
numbers = [10, 5, 8, 20]
print(min(numbers))  # Salida: 5
print(max(numbers))  # Salida: 20
```
**8.    `abs()  ` : Devuelve el valor absoluto de un número.**
 
```python
 Copiar
x = -10
print(abs(x))  # Salida: 10
```
 #### averiguar y leer para saber del tema 
 ## TIPOS DE FUNCIONES 
 ### Funciones Anonimas (Funciones lamda)
 una funcion que no tiene nombre 
 ```python
 lamda:"hola" 
#normal
def saludo():
    return "hola"
 ```
 ### Funciones Closure
 una funcion que dentro tiene otra funcion 
`def saludo(nombre):
     print(f"bienvenido {nombre}")
 `
 ### Funciones Callback
```python

```
 ### Programacion Funcional
la programacion funcional no requiere que sepas como se desarrolla y ejecuta el procesamiento de la informacion
**ejemplo**
```python
# programacion iterativa 
lista=[5,7,8,4,1]
def num_minimo(l):
    minimo=l[0]
    for n in l:
        if n < minimo:
            minimo=n
    return minimo 
# programacion funcional
min(lista) 
```
#### Hacer tarea  sobre map(), filter(), reduce()
## MAP()
## FILTER()
## REDUCE()