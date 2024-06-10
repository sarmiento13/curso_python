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

 *ejemplo*

en el archivo lecture.py