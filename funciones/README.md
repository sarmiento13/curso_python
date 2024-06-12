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
## Desempaquetado/Empaquetado de argumentos(tarea)

## Funciones internas de python (tarea)