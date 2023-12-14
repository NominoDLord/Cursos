########################################################################################################################
##                                                                                                                    ##
##                                                                                                                    ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####         ##
##       ###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##       ##
##       ##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##       ##
##       ##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####         ##
##                                                                                                                    ##
##                                                                                                                    ##
########################################################################################################################

╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                       G U I A    D E    P R O G R A M A C I Ó N                                      ║
║                             ------------------------------------------------------------                             ║
║                                 E S T R U C T U R A    D E    U N    P R O G R A M A                                 ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                         Í      N      D      I      C      E                                         │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

########################################################################################################################
## Para buscar algún tema en concreto dentro de esta documentación, podemos hacer uso del buscador de Notepad++       ##
## [Ctrl] + [F] y escribiendo el nombre en el buscador la palabra clave.                                              ##
########################################################################################################################

'''
      CONTENIDO -- ---- ------- ------- ------ ------ ----- ---- --- -- -

    - CAPÍTULO [01] CÓDIGO "SECUNDARIO" DEL PROGRAMA (avanzado)

    - PARTE 01 ---- DESCRIPCIÓN DEL PROGRAMA
    - PARTE 02 ---- IMPORTAR LAS BIBLIOTECAS
    - PARTE 03 ---- DEFINIR LAS VARIABLES
    - PARTE 04 ---- CLASES Y FUNCIONES
    - EXTRA 01 ---- CONSTRUCTOR '__init__'
    - EXTRA 02 ---- HERENCIA

    - CAPÍTULO [02] CÓDIGO "PRINCIPAL" DEL PROGRAMA (básico)
    
    - EXTRA 03 ---- ATRIBUTO ESPECIAL '__name__'
    - PARTE 06 (1r) Instanciar objetos
    - PARTE 07 (2n) Llamar a los objetos
    - PARTE 08 (3r) Funciones de Entrada y Salida de datos
    - PARTE 09 (4t) Conversión de tipos de datos
    - PARTE 10 (5t) Listado de operadores
    - PARTE 11 (6t) Listado de comparadores
    - PARTE 12 (7t) Condicionales (if-else-elif)
    - PARTE 13 (8t) Bucles (while/for)
    - PARTE 14 (9n) Listas, Sets, tuplas
    - PARTE 15 (10) diccionarios
    
    - CAPÍTULO [03] EXTRAS
    
    - EXTRA 04 ---- Copy & Deepcopy
    - EXTRA 05 ---- Modos de importación
    - EXTRA 06 ---- DECORADORES
    - EXTRA 07 ---- MANEJO DE EXCEPCIONES
    - EXTRA 08 ---- Lectura & Escritura
    - EXTRA 09 ---- Interfaz Gráfica (TKinter)
    - EXTRA 10 ---- Ejecutables
    - EXTRA 11 ---- PEP 8
    - EXTRA 12 ---- CMD
    - EXTRA 13 ---- Control de versiones
    - EXTRA 14 ---- RECURSOS

    - ----- -- ---- ------- ------- ------ ------ ----- ---- --- -- -
'''

'''
  Notepad++ es un bloc de notas orientado a la redacción de código.
  Es simple pero muy completo. Consume pocos recursos y tiene multitud
  de complementos que podemos añadir desde la pestaña de 'complementos'.
  Es OPEN-SOURCE (lo cual, quiere decir que podremos incluso incorporar
  y crear nuestras propias extensiones) y su uso es totalmente gratuito.
  
  Para su instalación, acceder al siguiente enlace:
  
  https://notepad-plus-plus.org/downloads/
  
  Para la instalación de python, acceder al siguiente enlace (windows):
  
  https://www.python.org/downloads/windows/
  
  Y para los usuarios de Apple, recomiendo que vendáis vuestro mac y
  os compréis un PC de verdad (¿Se nota mi aversión por Apple? XD).

'''
#########################################################################

# PARTE 01 [DESCRIPCIÓN DEL PROGRAMA] (opcional)

# Las primeras líneas deben contener una descripción de la(s)
# funcion(es) que realiza el programa comentadas en un 'docstring'.
# Esto facilitará a los desarrolladores (y a ti mismo) a entender cómo se
# debe utilizar el archivo y cómo manipular adecuadamente su información.

# En python, los comentarios mono-línea se generan usando el caracter especial (#)
# y los comentarios multi-línea se generan inscribiendo el texto dentro de (""")

# IMPORTANTE:

# Podemos utilizar tanto las comillas dobles (") como las comillas simples (')
# pero no ambas a la vez.

# El siguiente código sería un error:

print("Hola mundo')

'''
    NOMBRE DEL PROGRAMA:
    - Estructura de un programa

    DESCRIPCIÓN:
    - Archivo de muestra.
    - Este documento sirve de referencia como ejemplo
    - de estructura general que puede tener un programa.

    AUTOR: Nômino D Lord
    FECHA: 2023/--
'''

#########################################################################

# PARTE 02 [IMPORTAR LAS BIBLIOTECAS] (obligatorio)

# Las bibliotecas (o módulos) importados deben ser las primeras
# líneas del código de un programa (en caso de que hagamos uso de
# ellas, claro...).

# IMPORTANTE
# Para poder importar bibliotecas externas primero hay que instalarlas
# ejecutando en CMD el siguiente comando:

>>> pip install <biblioteca>
>>> pip3 install <biblioteca>   # Opción para versiones de python3+

# NOTA
# En algunas ocasiones podemos encontrarnos con código antiguo el cual
# es posible que contenga errores con la versión de python actual, por
# ese motivo, es posible tener instaladas distintas versiones de python.
# Con el comando 'pip' añadiremos las bibliotecas en la versión anterior
# a python3 y con el comando 'pip3' las añadiremos en su versión posterior.

# Si queremos actualizar la biblioteca a una versión más reciente:

>>> pip3 install --upgrade <biblioteca>

# Si queremos desinstalar una biblioteca:

>>> pip uninstall mi_biblioteca
>>> pip3 uninstall mi_biblioteca

# NOTA
# En algunas ocasiones podemos encontrarnos con código antiguo el cual
# es posible que contenga errores con la versión de python actual, por
# ese motivo, es posible tener instaladas distintas versiones de python.
# Con el comando 'pip' añadiremos las bibliotecas en la versión anterior
# a python3 y con el comando 'pip3' las añadiremos en su versión posterior.

# Para ver un listado de las bibliotecas que tenemos instaladas de python
# podemos usar los siguientes comandos:

>>> pip list
>>> pip3 list

# Si queremos actualizar pip a una versión más reciente:

>>> python.exe -m pip install --upgrade pip

# NOTA:
# Acceder a la ventana de comandos de windows:

## [Win]+[X] -> Ejecutar -> CMD -> Aceptar

import <nombre_biblioteca>
import <nombre_biblioteca> as <nombre_biblioteca_renombrada>
from <nombre_biblioteca> import <nombre_función>
from <nombre_biblioteca> import <nombre_función_1>, <nombre_función_2>, <nombre_función_3>
from <nombre_biblioteca> import <nombre_función> as <nombre_función_renombrada>

# AVISO:
# Los caracteres especiales "<" y ">" no se deben incluir en el
# código, son solo representativos de que la palabra introducida
# dentro de ellos es un valor descrito por el desarrollador y
# puede cambiar a lo largo de la ejecución del programa.

#########################################################################

# PARTE 03 [DEFINIR LAS VARIABLES] (recomendado)

# Definir las variables que vamos a utilizar al principio del programa es
# una buena práctica para tener agrupadas y facilmente localizados los
# valores que vamos a usar. Es posible que cuando empecemos a escribir el
# código aún no sepamos qué valor van a tener, aún así, podemos definirlas
# para tenerlas como referencia con un valor vacio (None).

variable_01 = <valor_01>
variable_02 = <valor_02>
variable_03 = None
variable_04 = None
variable_05 = <valor_05>

#########################################################################

# PARTE 04 [CLASES Y FUNCIONES] (externo)

# Aunque las 'clases' y 'funciones' suelen estar definidas en archivos
# diferentes (llamados módulos) que generalmente se ubican en el mismo
# directorio que el archivo de inicialización, (así se consigue tener
# el código del programa más límpio, organizado y con posibilidad de
# reutilizar el código para otras aplicaciones) en programas simples
# que no requieren de un código muy extenso, podemos agruparlo todo en
# el mismo archivo.

class <NombreDeLaClase>:

# NOTA:
# Aunque no es obligatorio, el primer caracter del nombre de una 'clase'
# deberíamos ponerlo en MAYÚSCULAS ya que en algunos otros lenguajes de
# programación sí que es obligatorio y en caso de que tengamos que escribir
# código en otro lenguaje, esto nos facilitará la transición de un lenguaje
# a otro (y a parte, esto nos permitirá saber también que lo que estamos
# usando es un objeto).

# -----------------------------------------------------------------------
# EXTRA 01 [CONSTRUCTORES]
# __init__

# Aunque el orden en el que los definamos es cosa ya más personal,
# sí que hay una clase/función "especial" que deberíamos indicar
# en primer lugar y esta será la que lleve el constructor __init__.

# __init__ es el constructor de una clase y se utiliza para establecer
# los atributos iniciales de un objeto.

# IMPORTANTE:
# Únicamente debemos definir un único __init__ por clase creada.
 
    def __init__(self, <argumento_01>, <argumento_02>, <argumento_03>):
        self.<argumento_01> = <argumento_01>
        self.<argumento_02> = <argumento_02>
        self.<argumento_03> = <argumento_03>

# -----------------------------------------------------------------------

# NOTA:
# A las 'variables' creadas dentro de una clase, se les llama 'atributos'
# Y a las 'funciones' dentro de una clase se les llama 'métodos'.

    def <función_método_simple>(self, <argumento>, <argumento>):
        return <argumento> + <argumento>

# NOTA:
# La "keyword" 'return' se utiliza para retornar uno (o varios) valores
# generados dentro de una función.

# Para ver la lista de 'keywords' disponibles podemos ingresar en la consola
# de python [abrir CMD -> inscribir 'python']:

>>> help("keywords")

# También podemos usar help() para ver otros listados de opciones disponible.

    def <función_método_arg>(self, *args):
        for arg in args:
            print(arg)

# NOTA:
# El argumento *args se utiliza cuando queremos pasarle una seríe de
# parámetros indefinidos (quiere decir, que podemos añadir 0, 5 o 50
# parámetros a la función/método).

    def <función_método_kwargs>(self, **kwargs):
        for clave, valor in kwargs.items():
            print(f"{clave}: {valor}")

# NOTA:
# El argumento *kwargs se utiliza cuando queremos pasarle una seríe de
# pares de valores indefinidos (se usan para los diccionarios).

# NOTA:
# El nombre <args> o <kwargs> es un nombre usado por convención y
# por lo tanto, podemos definirlo con un nombre distinto, lo que sí
# es obligatorio incluir son los <*> y <**>. 

    def <función_m_subclase>(self):
        pass

# NOTA:
# 'pass' es una palabra-clave (keyword) que se utiliza para dejar vacia
# una función/condición/excepción que queremos realizar, pero que aún
# no está implementado el código (similar a crear una variable con el
# valor 'None')

# IMPORTANTE:
# Las funciones creadas dentro de una clase SIEMPRE deben empezar con
# el argumento 'self' (bueno... en realidad podríamos llamarlo
# 'pepe', pero para no liar las cosas, utilizamos el nombre 'self').

# -----------------------------------------------------------------------
# EXTRA 02 [HERENCIA]

# Una clase puede heredar parte del código de otra clase.
# La clase a la que se accede se le llama 'superclase'
# La clase que recibe el código se le llama 'subclase'

# Aquí es dónde entra en juego el contructor __init__
# Toda subclase que acceda a la superclase heredará simpre el código
# contenido dentro de __init__ pero no el resto del código...
# de no ser que se acceda a ellos llamando a su función:

class NombreDeLaSubclase(NombreDeLaClase):
    def <función_m_subclase>(self):
        <codigo>
        return <valor>

# En esta subclase lo que hacemos es heredar el código contenido en __init__
# y a la vez, estamos completando la función <función_m_subclase> que hemos
# dejado sin contenido.

# Podriamos haber escrito el contenido directamente en la superclase. Sí.
# Pero si quisieramos crear una función distinta accediendo a la función
# de la superclase, ya no nos valdría y tendriamos que crear una nueva.

# La herencia es una herramienta muy potente pero también muy liosa así que
# se explicará más detalladamente en la documentación y ejercicios.

# -----------------------------------------------------------------------

#########################################################################

# EXTRA 03 [ATRIBUTO ESPECIAL __name__] (opcional)

# El atributo especial __name__ se utiliza para determinar si un
# archivo de Python se está ejecutando como un programa independiente
# o si se está importando como un módulo en otro programa.

if __name__ == '__main__':
    print("Este archivo es solo de demostración")

# En caso de que se ejecute un archivo con el nombre distinto a main.py,
# el programa lanzará un aviso por consola indicando el mensaje introducido
# en la función 'print()'

# AVISO:
# Si ejecutas este archivo, el aviso que lanzará el programa será
# un error ya que los nombres de las importaciónes/clases/funciones/etc
# no están correctamente definidos por que son solo representativos.

# Y en caso de que este fuera el archivo 'main.py', las líneas de código
# de nuestro programa deberán estar indentadas dentro de este atributo para
# que se ejecute correctamente.

# El nombre que indiquemos no tiene que ser concretamente '__main__',
# (podriamos llamarlo '__antonio__'), pero como es lógico, resultaría
# algo complicado de encontrar el archivo principal si (graciosillos de
# nosotros) le ponemos otro nombre que no sea el convencional (aunque 
# sería una buena forma de putear a alguien). Por ese motivo "siempre"
# encontrarás que el archivo de inicialización principal en cualquier
# programa tiene como nombre 'main'.

# EJEMPLOS:

## main.py
## main.js
## main.c
## main.java

#########################################################################

# PARTE 06 [CÓDIGO DEL PROGRAMA] (1r)
# <Instanciar objetos>

# Una vez tengamos ya todas las funciones, clases y variables,
# solo faltaría escribir el código para utilizarlas.

# Si estamos trabajando con clases (osea... objetos) lo primero
# que vamos a tener que realizar será la creación de estos.

nombre_objeto_01 = NombreDeLaClase(<argumento_01>, <argumento_02>, <argumento_03>)
nombre_objeto_02 = NombreDeLaClase(<argumento_01>, <argumento_02>, <argumento_03>)
nombre_objeto_03 = NombreDeLaClase(<argumento_01>, <argumento_02>, <argumento_03>)

# NOTA:
# A la creación de objetos se les llama 'instancias'

# IMPORTANTE
# Los argumentos que debemos introducir están relacionados
# con el constructor __init__ ya que este es un método que se
# ejecuta siempre al crear un objeto.

#########################################################################

# PARTE 07 [CÓDIGO DEL PROGRAMA] (2n)
# <Llamar a los objetos>

# Una vez creadas las instancias de los objetos, podemos llamar a alguno
# de los métodos (función dentro de la clase/objeto) que contiene.

nombre_objeto_01.<función_método_simple>(<valor_01>, <valor_02>)
nombre_objeto_02.<función_método_arg>(<arg_01>, <arg_02>, <arg_03>, <...>)
nombre_objeto_03.<función_método_kwargs>(<clave_01>=<valor_01>,
                                         <clave_02>=<valor_02>,
                                         <clave_03>=<valor_03>,
                                         <clave_Nº>=<valor_Nº>,
                                         <........>=<........>)

#########################################################################

# PARTE 08 [CÓDIGO DEL PROGRAMA] (3r)
# <Funciones de Entrada y Salida de datos>

# Para introducir un valor de forma externa al código usaremos la
# función 'input()' y para la salida de datos la función <print()>

valor_introducido = input("Introduce un valor: ")
print(f"El valor introducido es: {valor_introducido}")

# NOTA:
# Para introducir un valor dentro de la función 'print()' podemos usar
# el método 'f-string' con el que introducir un valor dentro de las
# llaves "{" y "}"

print("Hola", "Mundo")

# La función 'print()' en python, admite el poder insertar varios
# argumentos dentro de ella.

print("Hola", "Mundo", end="\n", sep=" ")

# La función 'print()', además, incluye dos argumentos (opcionales)

# Argumento 'end': Sirve para especificar qué acción realizará la
# función 'print()' al finalizar (por defecto, un salto de línea '\n')

# Argumento 'sep': Sirve para especificar el tipo de separación cuando
# se da a la función 'print()' más de un valor (por defecto, un espacio).

# CARACTERES DE ESCAPE
# Los caracteres de escape son caracteres especiales que se utilizan
# para representar caracteres que son difíciles de insertar o para
# representar ciertos caracteres que tienen significados especiales.

## \n   # Salto de línea
## \t   # Tabulación
## \\   # Barra invertida
## \'   # Comilla simple
## \"   # Comilla doble
## \r   # Retorno de carro
## \b   # Retroceso
## \f   # Avance de página

# IMPORTANTE:
# Los valores introducidos fuera del código del programa serán siempre
# del tipo 'strings' (cadenas de texto).

#########################################################################

# PARTE 09 [CÓDIGO DEL PROGRAMA] (4t)
# <Conversión de tipos de datos>

# Para saber a que tipo de dato corresponde un valor, aplicamos la
# función 'type()'

type(<valor>)

# Al introducimos un valor númerico fuera del código del programa,
# el valor introducido se leerá como una cadena de texto.
# Para realizar la conversión de este tipo de dato a un número,
# haremos uso de las función 'int()' (si es un número entero)
# o 'float()' si es un número decimal

numero_entero = int(input("Introduce un número entero: "))
numero_decimal = float(input("Introduce un número decimal: "))

# De esta forma, podremos utilizar los valores introducidos
# en operaciones, por ejemplo:

suma_entero_y_decimal = numero_entero + numero_decimal
print(suma_entero_y_decimal)

# CASTING (Conversión explícita)

# Este tipo de conversiones de llaman Casting.
# Otros tipos de conversión de datos son:

int()   # Convierte el valor en un número entero.
float() # Convierte el valor en un número de punto flotante.
str()   # Convierte el valor en una cadena de texto.
list()  # Convierte el valor en una lista.
tuple() # Convierte el valor en una tupla.
dict()  # Convierte el valor en un diccionario.
set()   # Convierte el valor en un conjunto.
bool()  # Convierte el valor en un booleano (True o False).

# Existen más funciones, pero las principales y más importantes son estas,
# las demás, muy raramente tendrás que usarlas hasta no tener un nivel
# mucho más avanzado, así que... concéntrate en estas.

# IMPORTANTE
# Para los números en punto flotante (float), hay que tener en cuenta que
# los datos son del todo exactos (prueba de sumar 0.1 + 0.2 y entenderás
# a lo que me refiero).

# NOTA
# Para representar números decimales con una limitación en su longitud
# podemos indicarlo de la siguiente forma:

>>> 


#########################################################################

# PARTE 10 [CÓDIGO DEL PROGRAMA] (5t)
# <Listado de operadores>

# Los operadores los usaremos para realizar operaciones matemáticas

# Adición (+)
# Suma dos valores.

suma = valor_01 + valor_02

# Sustracción (-)
# Resta el valor derecho del valor izquierdo.

resta = valor_01 - valor_02

# Multiplicación (*)
# Multiplica dos valores.

multiplica = valor_01 * valor_02

# División (/)
# Divide el valor izquierdo por el valor derecho.
# El dato resultante es siempre de tipo 'float()'.

divide = valor_01 / valor_02

# División entera (//)
# Divide el valor izquierdo por el valor derecho y redondea
# hacia abajo al entero más cercano.

divide_entero = valor_01 / valor_02

# Módulo (%)
# Devuelve el residuo de la división del valor izquierdo por
# el valor derecho.

modulo = valor_01 % valor_02

# Potencia (**)
# Eleva el valor izquierdo a la potencia del valor derecho.

potencia = valor_01 ** valor_02

# Otro tipo de operadores son los de incremento/decremento

incremento += 1
Decremento -= 1

# Incrementa una variable por un valor específico.
# Decrementa una variable por un valor específico.

# NOTA:
# Los operadores de incremento/decremento se utilizan para
# crear (generalmente) bucles, los cuales, queremos que una
# parte del código se ejecute un número de veces determinado.

#########################################################################

# PARTE 11 [CÓDIGO DEL PROGRAMA] (6t)
# <Listado de comparadores>

# Los comparadores se utilizan para comparar dos valores y
# evaluar expresiones booleanas (True/False)

# Igualdad (==)
# Identidad (is) o (is not)
# Comprueba si dos valores son iguales o identicos.
# El comparador de identidad implica que, además de que los dos valores
# sean iguales, también deben ser del mismo tipo de dato.

id(valor)

# Al igual que usamos la función 'type()' para averigual el tipo de
# dato de un valor, con la función 'id()' podemos averiguar su identidad.

valor_01 = 5
valor_02 = 5
valor_03 = 5.0

valor_01 == valor_02
# >>> True
valor_01 == valor_03
# >>> True
valor_01 is valor_02
# >>> True
valor_01 is valor_03
# >>> False
valor_01 is not valor_03
# >>> True

# NOTA:
# En otros lenguajes, se suele usar como operador de igualdad '==='
# pero en python se utiliza en su lugar la palabra-clave 'is'

# Diferencia (!=)
# Comprueba si dos valores son diferentes.

valor_01 != valor_02
# False
valor_01 != valor_03
# False

# Menor que... (<) o igual (<=)
# Mayor que... (>) o igual (>=)
# Comprueba si un valor es menor/mayor que otro (o igual.

valor_01 < valor_02
## False
valor_01 > valor_02
## False
valor_01 < valor_03
## False
valor_01 <= valor_02
## True
valor_01 >= valor_02
## True
valor_01 <= valor_03
## True

#########################################################################

# PARTE 12 [CÓDIGO DEL PROGRAMA] (7t)
# <Condicionales (if-else-elif)>

# Los comparadores estan estrechamente ligados con los condicionales.
# Los condicionales se utilizar para controlar el flujo de lectura
# de un programa o en otras palabras, las lineas de código que no
# cumplan con la condición asignada (False) no se ejecutarán.

# IMPORTANTE:
# El código dentro de los condicionales de ir indentado.

# CONDICIONAL (if)

##  if <valor> <comparador> <valor>:
##      <código a ejecutar si 'True'>

if 5 > 2:
    print("Este código SÍ se ejecutará")

# CONDICIONAL (if-if-if)

##  if <valor> <comparador> <valor>:
##      <código a ejecutar si 'True'>
##      if <valor> <comparador> <valor>:
##          <código a ejecutar si 'True'>
##          if <valor> <comparador> <valor>:
##              <código a ejecutar si 'True'>

if (1*2*3) == (3*2*1):
    print("Este código SÍ se ejecutará")
    if "hola" > "HOLA":
        print("Este código SÍ se ejecutará")
            if 1.00 is 1.0
                print("Este código SÍ se ejecutará")

# Podemos realizar comparaciones tanto con operaciones dentro
# del condiconal como también podemos comprarar cadenas de texto.

if 5 < 6:
    print("Este código SÍ se ejecutará")
    if 5 > 6:
        print("Este código NO se ejecutará")
            if 5 == 5:
                print("Este código NO se ejecutará")

# IMPORTARTE:
# En este ejemplo podemos ver que aunque el tercer condicional es
# 'verdadero', no se ejecutará porque está indentado dentro del segundo
# condicional que es 'falso'.

# CONDICIONAL (if-elif)

##  if <valor> <comparador> <valor>:
##      <código a ejecutar si 'True'>
##  elif <valor> <comparador> <valor>:
##      <código a ejecutar si anteriors = 'False' y actual = 'True'>

if 5 > 6:
    print("Este código NO se ejecutará")
elif 5 < 6:
    print("Este código SÍ se ejecutará")

# NOTA:
# Podemos incluir tantos 'elif' como sean necesarios:

if 1 >= 5:
    print("Este código NO se ejecutará")
elif 2 >= 5:
    print("Este código NO se ejecutará")
elif 3 >= 5:
    print("Este código NO se ejecutará")
elif 4 >= 5:
    print("Este código NO se ejecutará")
elif 5 >= 5:
    print("Este código SÍ se ejecutará")
elif 5 >= 5:
    print("Este código NO se ejecutará")

# IMPORTANTE
# En este ejemplo podemos ver aunque el último 'elif' es 'verdadero'
# no se ejecutará dado que el programa se detiene en cuanto encuetra
# el primer valor 'verdadero' (contrario a lo que ocurre con la 
# estructura indentada if-if-if).

# CONDICIONAL (if-elif-else)

##  if <valor> <comparador> <valor>:
##      <código a ejecutar si 'True'>
##  elif <valor> <comparador> <valor>:
##      <código a ejecutar si anterior 'False' actual 'True'>
##  else:
##      <código a ejecutar si los anteriores son 'False'>

if 1 > 5:
    print("Este código NO se ejecutará")
elif 2 > 5:
    print("Este código NO se ejecutará")
elif 3 > 5:
    print("Este código NO se ejecutará")
else:
    print("Este código SÍ se ejecutará")

# IMPORTANTE
# El condicional 'else' NO debe contener ninguna condición
# ya que este se deberá ejecutar SIEMPRE que las condiciones
# anteriores hayan sido descartadas.

if 1 > 5:
    print("Este código NO se ejecutará")
else:
    print("Este código SÍ se ejecutará")

# NOTA:
# Es posible prescindir del condicional 'elif' y pasar
# directamente al condicional 'else'

# COMBINACIÓN DE CONDICIONALES

if 1 < 3:
    print("A")
    if 2 < 3:
        print("B")
        if 3 < 3:
            print("C")
        elif 1 == 2:
            print("D")
        elif 2 == 2:
            print("E")
        else:
            print("F")
    else:
        print("G")
else:
    print("H")


# CONDICIONAL TERCIARIO o OPERADOR TERNARIO

# Este condicional se utiliza en situaciones en las que deseas tomar
# una decisión simple y asignar un valor en función de una condición
# sin necesidad de escribir un bloque if-else

##  <valor_si_cierto> if <condicion> else <valor_si_falso>

# Ejemplo:

puntuacion = float(input("Ingresar puntuación: "))
resultado = "Aprobado" if puntuacion >= 60 else "Suspendido"
print(resultado)

#########################################################################

# PARTE 13 [CÓDIGO DEL PROGRAMA] (8t)
# <Bucles (while/for)>

# Los bucles permiten repetir bloques de código de manera controlada
# iterando sobre los elementos de una lista/tupla/set/disccionario/etc.

# NOTA:
# La iteración es un concepto fundamental en programación que se
# refiere al proceso de repetir una o más instrucciones o un
# bloque de código varias veces.

# BUCLE 'WHILE'
# Se utiliza para repetir un bloque de código mientras
# una condición sea verdadera.

contar = 0
while contar <= 9:
    print(contar)
    contar += 1

# Este código imprimirá los números del 0 al 9

contar = 0
while contar <= 9:
    contar += 1
    print(contar)

# Este código imprimirá los números del 1 al 10

# IMPORTANTE
# Hay que tener cuidado de colocar el incremento en el lugar correcto.

# NOTA
# Si indicamos True en la condición, se generará un bucle infinito.

while True:
    print(contar)

# En caso de que esto suceda, presionareos [Ctrl]+[C] para así
# forzar la detención del programa.

# BUCLE 'FOR'
# Se utiliza para iterar sobre una secuencia, como una lista,
# una tupla o una cadena de texto

##  nombre_lista = [<dato_01>, <dato_02>, <dato_03>, <...>]
##  for nombre_lista in <datos>:
##      print<nombre_lista>

# Ejemplo 01:
# Usamos el bucle for para iterar sobre los elementos de una lista.

frutas = ["manzana", "plátano", "cereza"]
for fruta in frutas:
    print(fruta)

# Salida del bucle 'for':

## >>> manzana
## >>> plátano
## >>> cereza

# Ejemplo 02:
# Calcular la suma de los primeros 10 números:

suma = 0
for numero in range(1, 11):  # Itera desde 1 hasta 10 (inclusive)
    suma += numero

print("La suma de 1 a 10 es:", suma)

# Salida del bucle 'for':

## >>> La suma de 1 a 10 es: 55

# En este ejemplo usamos la función 'range()' para iterar
# sobre un rango de números.

# IMPORTANTE:
# La función 'range()' es muy útil y la debemos tener guardada
# en nuestra sección (mental) de "funciones favoritas"

# Ejemplo 03:
# Imprime "Hola, mundo" sin saltos de línea entre las letras.

frase = "Hola mundo"
for letra in frase:
    print(letra, end='')

# Salida del bucle 'for':

## >>> Hola mundo

# Ejemplo 04:

palabra1, palabra2 = "hola ", "mundo"
for letra1, letra2 in zip(palabra1, palabra2):
   print(letra1, letra2)

# Salida del bucle 'for':

## >>> H m
## >>> o u
## >>> l n
## >>> a d
## >>>   o

# NOTA:
# Utilizamos la función zip() para iterar simultáneamente a través
# de las letras de ambas palabras para que luego las imprima.

# IMPORTANTE:
# Si te fijas, el codigo anterior muestra las dos palabras
# correctamente porque he añadido un espacio despues del 'hola'
# de no ser así, el codigo de salida resultante sería:

## >>> H m
## >>> o u
## >>> l n
## >>> a d

# Este resultado es debido a que el bucle itera hasta la
# longitud más más corta. Para rectificar este "error", podemos
# realizarlo de la sigiuente manera:

# Ejemplo 05:

palabra1, palabra2 = "hola", "mundos"
longitud_maxima = max(len(palabra1), len(palabra2))

for i in range(longitud_maxima):
    letra1 = palabra1[i] if i < len(palabra1) else " "
    letra2 = palabra2[i] if i < len(palabra2) else " "
    print(letra1, letra2)

# De esta forma el código calculará la longitud máxima entre las
# dos palabras y luego iterará a través de las letras de ambas
# palabras, rellenando con espacios " " cuando una de las palabras
# sea más corta.

# La función 'max()' se utiliza para encontrar el valor máximo entre
# un conjunto de valores.

# La función 'len()' se utiliza para calcular la longitud de un objeto iterable

# Estas dos funciones son también muy útiles y debemos guardarlas
# en nuestra sección (mental) como "funciones favoritas"

#########################################################################

# PARTE 14 [CÓDIGO DEL PROGRAMA] (9n)
# <Listas, Sets, tuplas y diccionarios>

# Aunque esta sea la parte más "tostón" (para mi) de la programación (por
# eso me la he dejado para el final) es una parte muy importante que hay
# que aprender. Aunque podamos realizar programas mediamente complejos
# sin llegar a usarlas, es de vital importancia conocerlas en profundidad.

# LISTAS -> [] 

# Las listas son una estructura de datos fundamental en Python que se
# utiliza para almacenar una colección ordenada de elementos.

>>> listas = [<dato_01>, <dato_02>, <dato_03>, <dato_04>, <...>]

# Las listas pueden contener tipos de datos diferentes.

lista_de_elementos_distintos = [1, 2.0, False, "String"]

for elementos in lista_de_elementos_distintos:
    print(type(elementos))

# Salida del código

## >>> <class 'int'>
## >>> <class 'float'>
## >>> <class 'bool'>
## >>> <class 'str'>

# LISTAS dentro de LISTAS

# Podemos incluir listas dentro de listas:

lista_dentro_de_lista = ["uno", "dos", "tres", ["cuatro", "cinco"], "seis"]

for elemento in lista_dentro_de_lista:
    if type([]) == type(elemento):          # Comprobamos si el elemento es una lista.
        for subelemento in elemento:        # Si es una lista, volver a iterar sobre sus elementos
            print(subelemento)
    else:                                   # Si el elemento no es una lista, dejamos de iterar
        print(elemento)                     # para imprimir el elemento y no los caracteres.

# Para sacar cada elemento de las listas sin cometer el error de iterar sobre las
# String, debemos verificar si el elemento que estamos iterando es una lista o no.

# Si queremos consultar los elementos de una lista individualmente:

print(lista_dentro_de_lista[0])
print(lista_dentro_de_lista[1])
print(lista_dentro_de_lista[3][0])

# El primer elemento de una lista tendrá como índice el 0
# Para acceder a los elementos de una lista dentro de otra lista debemos "marcar"
# primero la posición de la lista y después el elemento.

# LISTAS VACÍAS

# Podemos ir añadiendo elementos a una lista vacía utilizando la función 'append()'.

lista = []
lista.append(1)
lista.append(2)
lista.append(3)

# Esto irá añadiendo los elementos uno a uno al final de la lista.
# Pero como es un poco "coñazo" añadirlos de uno en uno, mejor lo automatizamos con un 'for'

for numeros in range(4, 9):
    lista.append(numeros)

print(lista)

# Pero si queremos añadir los elementos de una lista dentro de una lista, no podemos
# usar la función 'append()' ya que, lo que agregariamos, sería la lista y no sus
# elementos individuales. Para hacerlo, nuestro famoso bucle 'for' tiene la solución
# para casi todos nuestros problemas.

lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
lista_3 = []

for elemento in lista_1:
    lista_3.append(elemento)
for elemento in lista_2:
    lista_3.append(elemento)
            
print(lista_3)

# O simplemente... también podemos hacer uso de la función 'extend()' (XD)

lista_4 = []
lista_4.extend(lista_1)
lista_4.extend(lista_2)
print(lista_4)

# Para remover un elemento en concreto usamos la función 'remove()'

lista.remove(3)
print(lista)

# O si lo queremos elimimnar por su índice, tenemos 2 formas de hacerlo:

lista.pop(3)    # Con la función 'pop()'
print(lista)    # Recuerda: "Cuando haces 'pop' ya no hay 'stop'"

del lista[3]    # O con la 'keyword' 'del'
print(lista)    # Que viene de 'delete' => 'borrar'

# Para ordenar nuestras listas usaremos:

lista.sort()        # La función 'sort()' para ordenar de menor a mayor.
print(lista)

lista.reverse()     # La función 'reverse()' para invertir el orden de la lista.
print(lista)

# Y si te estás preguntado si se me ha olvidado de añadir la función para ordenar
# de 'mayor a menor', la respuesta es NOOooOooOoOoOOoOoOo.

# ¡No existe dicha función! ¿Por qué? Pues porque supongo que los desarrolladores
# de python pensaron "¿¿¿Pa' qué molestarnos en crear una función para ordenar de
# 'mayor a menor' si pueden usar primero la función 'sort() para ordenar de 'menor a
# a mayor' y después darle la vuelta???" Así que... bueno... una función menos que aprender.

# Bueno, sigamos...

# También podemos buscar elementos concretos de una lista haciendo uso
# del condicional 'for' y con la keyword 'in' (y podemos usar un 'else')

if 4 in lista:
    print("El número ha sido encontrado")
else:
    print("El número no ha sido encontrado")

# Para saber en que posición se encuentra un elemento dentro de una lista
# podemos usar la función 'index()'

encontrar_elemento = 7

if encontrar_elemento in lista:
    indice = lista.index(encontrar_elemento)
    print(f"El elemento se encuentra en la posición {indice+1} y su índice es el {indice}")
else:
    print("El elemento no ha sido encontrado")

# IMPORTANTE
# Aunque la verdad... esta función es un poco inútil si queremos encontrar varios
# elementos iguales dentro de una lista porque solo nos va a indicar la posición
# del primer elemento encontrado.

# Para realizar una busqueda completa de todos los elementos de una lista y saber
# su índice podemos hacer uso de nuestra imaginación y nuestros super-poderes como
# como (futuros) programadores y crearnos nuestra propia función:

lista_nueva = [1, 2, 3, 2, 1]
encontrar_elemento = 2

def buscar_elementos(lista, buscar):
    indice = -1
    for elemento in lista:
        indice += 1
        if buscar == elemento:
            print(f"Elemento encontrado en posición {indice+1} con índice {indice}")

buscar_elementos(lista_nueva, encontrar_elemento)

# Para saber la longitud de una lista, podemos usar la función 'len()'

print(len(lista))

# Para cambiar un elemento por otro indicamos en qué posición está y le asignamos
# el elemento en cuestión:

lista[1] = 0    # Esta es fácil ¿no?
print(lista)    # Compliquemosla...

lista[0], lista[2], lista[3] = 0, 0, 0      # Sí, también es posible asignar valores de esta
print(lista)                                # forma, pero puede ser confuso, así que no abuseis.

# También podríamos haberlo hecho con un 'for', pero mejor os lo dejo como tarea, que a estas
# alturas no debería ser algo dificil.

# -----------------------------------------------------------------------
# EXTRA 04 [Copy & Deepcopy]

# ¡Y para acabar de presentar las funciones más famosas de las listas... ¡Ta-ta-ta-chaaaan!
# La función 'copy' (adivina... sirve para copiar listas)

# Aunque parezca una "tontería de función" ya que podríamos copiar una lista simplemente
# asignandola a otra variable tipo:

lista_sin_copiar = [1, 2, [3, 4], 5]
lista_copiada = lista_sin_copiar

print(lista_sin_copiar)
print(lista_copiada)

# Salida del código:

>>> [1, 2, [3, 4], 5]
>>> [1, 2, [3, 4], 5]

# Bien ¿no? Pues no... con esto tenemos un problema.

# Esta asignación no sería realmente una copia de la primera variable, sino,
# que sería una referencia. ¿Qué quiere decir esto?

# Veamoslo con un ejemplo:

lista_sin_copiar[1] = 0

print(lista_sin_copiar)
print(lista_copiada)

# Salida del código:

>>> [1, 0, [3, 4], 5]
>>> [1, 0, [3, 4], 5]

# El problema que tenemos aquí es que si cambiamos la variable 'lista_sin_copiar'
# también se cambiará la variable 'lista_copiada'.

# Y es precisamente para estos casos que tenemos la función 'copy()'

# -----------------------------------------------------------------------
# EXTRA 05 [Modos de importación]

# IMPORTANTE (¡MUY IMPORTANTE!)
# Para usar la función 'copy()' vamos a tener que importarla, ya que no es parte de las funciones
# internas (Built-in-functions) de Python.

lista_sin_copiar = [1, 2, [3, 4], 5]
lista_copiada = lista_sin_copiar

import copy

lista_copiada_con_copy = copy.copy(lista_sin_copiar)

# Demasiados "copy's" ¿No? ... Mmmmmm.... Hagamoslo de otro modo...

from copy import copy

lista_copiada_con_copy = copy(lista_sin_copiar)

# Podemos retocarlo un poco más...

from copy import copy as fotocopiadora

lista_copiada_con_copy = fotocopiadora(lista_sin_copiar)

# ¡Bien! Ahora sí. Y a demás hemos practicado los distintos tipos de
# importación diferentes que podemos aplicar.

lista_sin_copiar[1] = 0

print(f"Imprimir variable \'lista_sin_copiar\':       {lista_sin_copiar}")
print(f"Imprimir variable \'lista_copiada\':          {lista_copiada}")
print(f"Imprimir variable \'lista_copiada_con_copy\': {lista_copiada_con_copy}")

# NOTA
# Recuerda que para imprimir caracteres especiales como las comillas se deben usar
# los caracteres de escape (\').

# Salida del código

>>> Imprimir variable 'lista_sin_copiar':       [1, 0, [3, 4], 5]
>>> Imprimir variable 'lista_copiada':          [1, 0, [3, 4], 5]
>>> Imprimir variable 'lista_copiada_con_copy': [1, 2, [3, 4], 5]

# ¿Solucionado?
# Hagamos un última prueba:

lista_sin_copiar[2][1] = 0

print(f"Imprimir variable \'lista_sin_copiar\':       {lista_sin_copiar}")
print(f"Imprimir variable \'lista_copiada\':          {lista_copiada}")
print(f"Imprimir variable \'lista_copiada_con_copy\': {lista_copiada_con_copy}")

# Salida del código

>>> Imprimir variable 'lista_sin_copiar':       [1, 0, [3, 0], 5]
>>> Imprimir variable 'lista_copiada':          [1, 0, [3, 0], 5]
>>> Imprimir variable 'lista_copiada_con_copy': [1, 2, [3, 0], 5]

# ¿Qué ocurrió? ¡Houston! ¡Houston! ¡Tenemos un problema!

# ¡IMPORTANTE!
# ¡La función copy no nos copia la listas dentro de otras listas!

## Pero tranquilos... ¡Tenemos la solución!
## ¡Use la función 'deepcopy()' para realizar copias profundas de sus listas!
## ¡Recuérdelo! ¡¡¡¡deeeeeeeeepcopy()!!!! De bibliotecas 'copy()'
## [Y no use marcas blancas] (guiño, guiño)

from copy import copy as fotocopiadora
from copy import deepcopy as copia_profunda

# Volvamos a intentarlo...

lista_sin_copiar = [1, 2, [3, 4], 5]

lista_copiada = lista_sin_copiar
lista_copiada_con_copy = fotocopiadora(lista_sin_copiar)
lista_copiada_con_deepcopy = copia_profunda(lista_sin_copiar)

lista_sin_copiar[1] = 0
lista_sin_copiar[2][1] = 0

print(f"Imprimir variable \'lista_sin_copiar\':           {lista_sin_copiar}")
print(f"Imprimir variable \'lista_copiada\':              {lista_copiada}")
print(f"Imprimir variable \'lista_copiada_con_copy\':     {lista_copiada_con_copy}")
print(f"Imprimir variable \'lista_copiada_con_deepcopy\': {lista_copiada_con_deepcopy}")

# Salida del código

>>> Imprimir variable 'lista_sin_copiar':           [1, 0, [3, 0], 5]
>>> Imprimir variable 'lista_copiada':              [1, 0, [3, 0], 5]
>>> Imprimir variable 'lista_copiada_con_copy':     [1, 2, [3, 0], 5]
>>> Imprimir variable 'lista_copiada_con_deepcopy': [1, 2, [3, 4], 5]

# Y ahora sí, todo correcto. ;)

# -----------------------------------------------------------------------

## Bueeeeno... ahora sí, por fin hemos acabado con las listas.
## Ahora solo faltan los Sets, las Tuplas y los diccionarios.
## ¿Ahora me entendéis cuando dije que este tema era un "tostón"?)

# A parte de los 'diccionarios', los 'Sets' y 'Tuplas' son prácticamente
# iguales a las listas, pero con algunas diferencias:

''' TABLA DE PROPIEDADES :: LISTAS | TUPLAS | SETS | FROZENSET ::
 -----------------------------------------------------------------------
 |   LISTAS  []  |    TUPLAS  ()   |     SETS  {}    |  FROZENSET  {}  |
 -----------------------------------------------------------------------
 |  Mutabilidad  |  Inmutabilidad  |  Mutabilidad    |  Inmutabilidad  |
 |  Orden        |  Orden          |  Desorden       |  Desorden       |
 |  Diversidad   |  Diversidad     |  Identidad      |  Identidad      |
 -----------------------------------------------------------------------

'''

# Los cuatro son agrupaciones de datos con la diferencia de que...


# Listas    ->  Datos sí localizados, sí editables, sí duplicados.
# Tuplas    ->  Datos sí localizados, no editables, sí duplicados.
# Sets      ->  Datos no localizados, sí editables, no duplicados.
# Frozenset ->  Datos no localizados, no editables, no duplicados.


# Como casi todas las funciones usadas con las 'Listas' se pueden utilizar
# igual con las 'Tuplas' y los 'Sets', no hay necesidad de extender mucho
# más esto, así que...

# -----------------------------------------------------------------------

# PARTE 15 [DICCIONARIOS] (10)

# Los 'diccionarios' son pares de elementos (osea... que siempre van de dos en dos)
# Se podría decir que el primer elemento es la 'palabra' (key) por la que
# accederemos a su 'definición' (vamos... como un diccionario de los de toda la vida).

# Ejemplo:

diccionario = {
    "Clave 01": "Definición 01",
    "Clave 02": "Definición 02",
    "Clave 03": "Definición 03",
    "Clave 04": "Definición 04"
    }

# NOTA
# No hace falta colocar unas debajo de otras, pero de esta forma resulta más cómodo y
# facil de ver a simple vista.

# IMPORTANTE
# Las 'keys' asignadas a las definiciones deben ser únicas, eso quiere decir,
# que no se pueden usar dos palabras iguales para definir dos elementos distintos.

# Si queremos acceder a una definición dentro de un diccionario se hará usando su clave:

print(diccionario["Clave 01"])

# O si queremos acceder a todas ellas... tenemos tres formas:

ver_diccionario = diccionario   # Aunque esta es la manera más sencilla es bastante fea
print(ver_diccionario)          # (pruebalo tú mismo y verás 'por qué')

for clave in diccionario:           # Como siempre, con el bucle 'for'
    valor = diccionario[clave]      # podemos hacer milagros.
    print(f"{clave}: {valor}")

for clave, valor in diccionario.items():    # Y por último, podemos usar la función
    print(f"{clave}: {valor}")              # items() para acortar un poco más el código.

# También es posible añadir, cambiar o eliminar otro par <clave:valor>

diccionario["Nueva Clave"] = "Nueva Definición" # Añadimos una nueva clave con su 'definición'

# ¿Y qué pasa si lo que queremos es juntar dos listas, las cuales, una
# se usará como clave, y la otra como su valor?

# Si piensas en que podríamos hacerlo con un bucle 'for' estás en lo cierto,
# pero esta vez vamos a usar la función 'zip()' que es mucho más sencillo:

lista_de_claves = ["Clave 1", "Clave 2", "Clave 3"]
lista_de_valores = ["Valor 1", "Valor 2", "Valor 3"]

diccionario_nuevo = dict(zip(lista_de_claves, lista_de_valores))

# IMPORTANTE
# Ten en cuenta de que si una lista es más corta que la otra, sólo se añadirá
# hasta la posición de la lista de menor longitud.

# Para eleminar un elemento usaremos la keyword 'del'

del diccionario["Clave 02"]     # Esto eliminará tanto su valor como su clave

# NOTA
# Si queremos cambiar el valor de una clave, simplemente debemos re-asignarle
# un nuevo valor a la clave, pero si lo que queremos cambiar es la clave y
# no su valor, esto no es posible (aunque siempre podemos crear una 'clave nueva'
# con el valor de la 'clave vieja' y después eliminarla).


# También podemos usar el condicional 'if' para saber si existe una clave...

if "Clave 03" in diccionario:
    print("Clave encontrada.")

# o si existe ya un valor dentro del diccionario.

for clave in diccionario:
    if "Definición 01" in diccionario[clave]:
        print("Valor encontrado.")

#########################################################################

# EXTRA 06 [DECORADORES] (avanzado)

# Los decoradores son una característica poderosa y flexible que se utiliza
# para modificar o extender el comportamiento de una función/método sin
# modificar su código fuente (aunque este concepto está presente en otros
# lenguajes de programación, su nombre y modo de implementación puede variar)

# Ejemplo simple:

def decoracion(decorar):
    def envoltura():
        print("Primero")
        decorar()
        print("Segundo")
    return envoltura

@decoracion     # Los decoradores usan el carácter '@' para ser llamados.
def decorando():
    print("Tercero")

decorando()

# Ejemplo de una función con decorador sin usar el decorador:

def decoracion(decorar):
    def envoltura():
        print("Primero")
        decorar()
        print("Segundo")
    return envoltura

def funcion_decorativa():
    pass

envoltura_de_decoracion = decoracion(funcion_decorativa)
envoltura_de_decoracion()

# Ejemplo pasando por un argumento al decorador:

def decoracion(decorar):
    def envoltura(envoltorio):
        print("Primero")
        decorar(envoltorio)
        print("Segundo")
    return envoltura

@decoracion
def decorando(envoltorio):
    print(envoltorio)

decorando("Tercero")

# Aunque el concepto de los decoradores es para un nivel más avanzado,
# es algo a tener en cuenta para cuando ya nos sintamos cómodos escribiendo
# código, ya que, si no se domina bien, nos puede llevar a cometer muchos
# errores y no es recomendable para aquellos que están empezando.

#########################################################################

# EXTRA 07 [MANEJO DE EXCEPCIONES] (Importante)

# El manejo de excepciones es una parte importantísima del código ya que,
# con ella podremos manejar posibles errores sin perjudicar el resto del código
# y que el programa siga abanzando incluso si se encuentra con un error.

# Las excepciones se manejan de forma similar a los condicionales.

# Ejemplo general:

try:
    # Código que puede lanzar una excepción
    resultado = operacion_potencialmente_problematica()
except <TipoDeExcepcion> as <nombre_de_variable>:
    # Código que maneja la excepción
    print("Se produjo una excepción:", nombre_de_variable)
else:
    # Código que se ejecuta si no se produjo ninguna excepción
    print("La operación se realizó con éxito.")
finally:
    # Código que siempre se ejecutará, ocurra o no una excepción
    print("Finalizando la operación.")

# NOTA
# En la condición 'except' debemos especificar el tipo de error esperado
# como por ejemplo <TypeError>, <NameError>, <SyntaxError>, etc
# Si no especificamos el tipo de error, se deberá usar la 'keyword' <Exception>.

#########################################################################

# EXTRA 08 [Lectura & Escritura]

# En algunas ocasiones necesitaremos leer y editar datos de archivos,
# para ello, Python incorpora en su biblioteca interna algunas funciones
# para realizar estas tareas con archivos de texto.

# Esta función es muy útil para poder guardar información que luego vamos
# a necesitar, por ejemplo, al crear un juego en el que el jugador pueda
# guardar su partida para continuar más adelante.

# Función para abrir/cerrar archivos

open(<archivo>, <modo>)   

    # "r"  ->  Modo Lectura (por defecto)
    # "w"  ->  Modo Escritura
    # "a"  ->  Modo Adición
    # "x"  ->  Modo Creación
    # "t"  ->  Modo texto (predeterminado)


file.close()    # Cerrar archivo después de usar.

# ¡¡¡CUIDADO!!!
# En el 'Modo Escritura" lo que harás será reemplazar el texto actual del
# archivo por el texto nuevo, por lo que, se borrarán TODOS los datos antiguos.
# Para añadir sin modificar la información anterior debemos usar el 'Modo Adición'

# Funciones para escribir en archivos

file.write("texto")         # Escribir texto en archivo.

file.writelines(<lines>):   # Escribir textos en archivo.


# Funciones para leer los archivos

file.read()                 # Lee el contenido del archivo como una cadena.

file.readline()             # Lee una línea del archivo.

file.readlines()            # Lee todas las líneas del archivo y las devuelve como una lista de cadenas.

for <line> in file          # Itera a través de las líneas del archivo usando un bucle for.

# Otras funciones

with open(<archivo>, <modo>) as file:

# Este contexto maneja la declaración asegura que el archivo se cierre
# adecuadamente al salir del bloque with.

os.path.exists(<archivo>)    # Comprueba si un archivo existe.

os.path.isfile(<archivo>)    # Comprueba si un objeto es un archivo.


# Ejemplo 1

file = open("ejemplo.txt", "w")

file.write("Primera línea de texto.\n")
file.write("Segunda línea de texto.\n")

file.close()


# Ejemplo 4

text = "Línea de texto"

with open("ejemplo.txt", "w") as file:

    file.write(text)


# Ejemplo 3

lines = ["Primera línea", "Segunda línea", "Tercera línea"]

with open("ejemplo.txt", "w") as file:

    file.writelines(line + "\n" for line in lines)


#########################################################################

# EXTRA 09 [INTERFAZ GRÁFICA] (TKinter)

# Tkinter es una de las bibliotecas internar de Python que se utilizan
# para la creación de interfaces gráficas.

# Ejemplo de interfaz simple:

import tkinter as tk

# Función a ejecutar al presionar botón
def mostrar_mensaje():
    etiqueta.config(text="¡Hola, Mundo!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry("200x100")
ventana.title("Ejemplo de Tkinter")

# Crear etiqueta para mostrar mensaje
etiqueta = tk.Label(ventana, text="Presiona el botón")
etiqueta.pack(pady=10)

# Crear un botón para cambiar etiqueta
boton = tk.Button(ventana, text="Mostrar Mensaje", command=mostrar_mensaje)
boton.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()

# -----------------------------------------------------------------------

# LISTADO DE FUNCIONES DE TKINTER

# Funciones generales

>>> Tk()            # Crea una ventana principal para la aplicación.
>>> mainloop()      # Bucle principal (maneja eventos y la interfaz de usuario).
>>> Label()         # Crea una etiqueta de texto.
>>> Button()        # Crea un botón interactivo.
>>> Entry()         # Crea un campo de entrada de texto.
>>> Text()          # Crea un área de texto editable.
>>> Toplevel()      # Crea una nueva ventana superior.

# Widgets de selección y entrada

>>> Checkbutton()   # Crea una casilla de verificación.
>>> Radiobutton()   # Crea un botón de radio.
>>> Scale()         # Crea un control deslizante.
>>> Spinbox()       # Crea una caja de valores numéricos.
>>> Listbox()       # Crea una lista de selección.
>>> Menu()          # Crea un menú desplegable.
>>> OptionMenu()    # Crea un menú desplegable de opciones.

# Widgets de contenedor y organización

>>> Frame()         # Crea un marco para organizar widgets.
>>> LabelFrame()    # Crea un marco con una etiqueta.
>>> PanedWindow()   # Crea una ventana dividida.
>>> Notebook()      # Crea un cuaderno de pestañas.
>>> Labelframe()    # Crea un marco con una etiqueta.
>>> Canvas()        # Crea un lienzo para dibujos personalizados.

# Ventanas de diálogo y cajas de mensaje

>>> tkMessageBox.showinfo()     # Muestra un mensaje informativo.
>>> tkMessageBox.showwarning()  # Muestra una advertencia.
>>> tkMessageBox.showerror()    # Muestra un mensaje de error.
>>> tkSimpleDialog.askstring()  # Solicita una cadena al usuario.
>>> tkSimpleDialog.askinteger() # Solicita un número entero al usuario.

# Widgets avanzados

>>> Treeview()      # Crea una vista de árbol.
>>> Progressbar()   # Crea una barra de progreso.
>>> Scrollbar()     # Crea una barra de desplazamiento.


#########################################################################

# EXTRA 10 [Ejecutables]

# Los archivos ejecutables nos permiten ejecutar un programa en un Sistema
# Operativo concreto sin la necesidad de tener instalado el lenguaje en el
# que ha estado programado. Esto es útil si queremos distribuir nuestro
# programa a otras personas.

# IMPORTANTE
# Se debe crear un ejecutable distinto para cada Sistema Operativo.

# Para realizar el empaquemiento de nuestro programa, necesitaremos tener
# instalada la biblioteca pyinstaller

>>> pip install pyinstaller

# Una vez instalada, usamos el siguiente comando:

>>><dir> pyinstaller --onefile <nombre_del_programa.py>

# Al ejecutar este comando y definir el archivo a empaquetar, se crearán:

# Carpeta 'dist'  -> Contiene el archivo ejecutable '.exe'
# Carpeta 'build' -> Contiene los archivos creados durante el empquetamiento.
# Archivo '.spec' -> Personaliza la construcción de la aplicación.

# NOTA
# Una vez creado el archivo '.exe' no es necesario conservar los archivos/capetas
# generados durante el empaquetamiento, pero sí el archivo '.py' original, ya que
# si lo eliminamos, no podremos acceder al código del programa.

#########################################################################

# EXTRA 11 [PEP 8]

# PEP 8 es una guía de estilo para escribir código en el lenguaje de programación Python.
# PEP es el acrónimo de "Python Enhancement Proposal" (Propuesta de Mejora de Python),
# y el número 8 se refiere a este documento específico.



#########################################################################

# EXTRA 12 [CMD]
# Consola de comandos

# Controlar el uso de la consola de comandos es esencial para poder
# probar el código, por lo que, antes de aprender a programar primero
# debemos aprender a usar esta herramienta.

# NAVEGACIÓN POR LOS DIRECTORIOS

>>> cd <siguiente_directorio>    # Cambia el directorio actual.
>>> dir                          # Listado de elementos del directorio.
>>> cd..                         # Retrocede un directorio.
>>> cd\                          # Retrocede al directoria raiz.

## NOTA: Escribiendo 'cd' en la consola y pulsando [Tab] podremos pasar
## por la lista de opciones que podremos seleccionar sin tener que escribir
## el nombre completo a mano.

# ELIMINAR/CREAR DIRECTORIOS

>>> mkdir <nombre_nuevo_directorio>     # Crea un nuevo directorio.
>>> rmdir /s /q <nombre_directorio>     # Elimina un directorio y su contenido (¡CUIDADO!).

# MANEJO DE ARCHIVOS

>>> copy <archivo_origen> <archivo_destino>     # Copia un archivo.
>>> move <archivo_origen> <archivo_destino>     # Mueve un archivo.
>>> ren <nombre_actual> <nuevo_nombre>          # Renombra un archivo.
Gestión de archivos:

>>> del <nombre_archivo>        # Borra un archivo.
>>> type <nombre_archivo>       # Muestra el contenido de un archivo.
>>> edit <nombre_archivo>       # Abre el Bloc de notas para editar un archivo de texto.

# REDES Y CONECTIVIDAD

>>> ipconfig                    # Muestra la configuración de red de la computadora.
>>> ping <dirección_ip>         # Verifica la conectividad con una dirección IP.

# AYUDA

>>> help                        # Muestra una lista de comandos disponibles.
>>> <nombre_comando> /?         # Obtiene información sobre el uso de un comando específico.

# VARIABLES DE ENTORNO

set                             # Muestra las variables de entorno.
set <variable>=<valor>          # Crea o modifica una variable de entorno.

# OTROS

exit        # Cierra la ventana de CMD.

# NOTA

# Para abrir un archivo de python, debemos indicarlo de la siguiente manera:

>>> C:\> python <ruta/del/archivo>

# Para añadir la ruta de un archivo en concreo, podemos realizar
# la acción de arrastrar el archivo a la ventana de CMD

#########################################################################

# EXTRA 13 [Control de versiones]

# El control de versiones es un sistema que registra y gestiona los cambios
# realizados en archivos y carpetas a lo largo del tiempo. Permite llevar un
# historial de modificaciones, facilita la colaboración en proyectos y ayuda
# a recuperar versiones anteriores en caso de errores o necesidad de referencia.

# El control de versiones se puede realizar tanto de manera local como remota.
# Existen distintas plataformas online (llamadas 'repositorios') que nos premiten
# alojar y compartir nuestro código tanto de forma privada como publica.

# GIT & GITHUB

# El principal repositorio para gestionar nuestro código es GitHub, el cual, nos
# proporciona una herramienta (Git) para las tareas de control tanto de forma
# local como de remota.

# La mayoria de programas de edición de código tienen compatibilidad con Git e
# incluso incorporan una interfaz con la que no nos tendrémos que preocupar de
# ir insertando comandos en por consola.

# Sublime Text & Sublime Merge

# 'Sublime' es un programa (o mejor dicho, dos) que se centra tanto al desarrollo
# del código (Sublime Text) como a su gestión (Sublime Merge) el cual recomiendo
# ya que integra una interfaz para el control de versiones muy buena y sin
# consumir una gran cantidad de recursos. 


 aún así, es recomendable aprender su
# uso ya que no es dificil de manejar.

# COMANDOS BÁSICOS

>>> git init                            # Inicializa un nuevo repositorio Git en el directorio actual.
>>> git clone <url>                     # Clona un repositorio remoto en tu máquina local.
>>> git add <archivo>                   # Añade un archivo o cambios al área de preparación.
>>> git commit -m "Texto"               # Confirma los cambios en el repositorio local con un mensaje descriptivo.
>>> git status                          # Muestra el estado actual del repositorio.
>>> git log                             # Muestra un registro de los commits realizados.
>>> git branch                          # Lista todas las ramas en el repositorio.
>>> git checkout <nombre-de-rama>       # Cambia a una rama específica.
>>> git pull                            # Actualiza el repositorio local con los cambios del repositorio remoto.
>>> git push                            # Sube tus cambios al repositorio remoto.

# COMANDOS DE RAMIFICACIÓN

>>> git branch <nombre-de-rama>         # Crea una nueva rama.
>>> git branch -d <nombre-de-rama>      # Elimina una rama (solo si los cambios están fusionados).
>>> git merge <nombre-de-rama>          # Fusiona una rama en la rama actual.
>>> git checkout -b <nombre-de-rama>    # Crea y cambia a una nueva rama en un solo paso.

# COMANDOS PARA REPOSITORIOS REMOTOS

>>> git remote -v                       # Muestra la URL del repositorio remoto.
>>> git remote add <nombre> <url>       # Agrega un repositorio remoto con un nombre específico.
>>> git fetch <nombre-remoto>           # Descarga los cambios del repositorio remoto.
>>> git pull <nombre-remoto> <rama>     # Actualiza la rama actual con los cambios del repositorio remoto.
>>> git push <nombre-remoto> <rama>     # Sube los cambios de la rama local al repositorio remoto.

# COMANDOS AVANZADOS

>>> git stash                           # Guarda cambios no comprometidos temporalmente.
>>> git rebase                          # Reorganiza commits para facilitar la integración de cambios.
>>> git cherry-pick <commit>            # Aplica un commit específico a la rama actual.
>>> git tag <nombre-tag> <commit>       # Crea una etiqueta para un commit específico.

# COMANDOS ESPECÍFICOS DE GITHUB

>>> git pull origin main --rebase       # Realiza un pull con rebase desde la rama principal (main) del repositorio remoto.
>>> git push origin --tags              # Sube las etiquetas al repositorio remoto.
>>> hub create <nombre-repo>            # Crea un nuevo repositorio en GitHub desde la línea de comandos.
>>> hub browse                          # Abre el repositorio actual en tu navegador web.

#########################################################################

# EXTRA 14 [RECURSOS]


#    EDITORES DEV

>>> https://notepad-plus-plus.org/downloads/              # Notepad++
>>> https://www.sublimetext.com/download                  # Sublime Text 
>>> https://www.sublimemerge.com/download                 # Sublime Merge
>>> https://www.jetbrains.com/es-es/pycharm/              # PyCharm
>>> https://code.visualstudio.com/download                # Visual Studio Code



#    DOCUMENTACIÓN

>>> https://devdocs.io                                    # Documentación Dev
>>> https://docs.python.org/es/3/contents.html            # Python
>>> https://books.goalkicker.com                          # Manuales


#    CREACIÓN DIAGRAMAS DE FLUJO

>>> https://app.diagrams.net                              # Diagrama de flujo [OnLine]
>>> https://github.com/jgraph/drawio-desktop/releases     # Diagrama de flujo [Desktop]


>>> https://roadmap.sh                                    # Planificación de estudio

#    INTELIGENCIA ARTIFICIAL

>>> https://chat.openai.com                               # IA


#    CONTROL DE VERSIONES

>>> https://git-scm.com/download/win                      # Git


#    PYTHON

>>> https://www.python.org/downloads/                     # Descargar Python


### LISTA DE BIBLIOTECAS DE PYTHON [INTERNAS]

>>> os              # Para interactuar con el sistema operativo, manipular rutas de archivos y directorios, y realizar operaciones de sistema.
>>> sys             # Para acceder a variables y funciones específicas del sistema, como argumentos de línea de comandos.
>>> math            # Para realizar operaciones matemáticas avanzadas.
>>> datetime        # Para trabajar con fechas y horas.
>>> json            # Para trabajar con datos en formato JSON.
>>> csv             # Para leer y escribir archivos CSV (Valores Separados por Comas).
>>> collections     # Ofrece estructuras de datos adicionales como diccionarios con claves por defecto y colas.
>>> urllib          # Para realizar solicitudes HTTP y trabajar con URL.
>>> random          # 
>>> re              # Para expresiones regulares y búsqueda de patrones en texto.
>>> sqlite3         # Para interactuar con bases de datos SQLite.
>>> email           # Para enviar y recibir correos electrónicos.
>>> pickle          # Para serialización de objetos en Python.
>>> argparse        # Para analizar argumentos de línea de comandos de forma fácil.
>>> threading       # Para programación concurrente y creación de hilos.
>>> socket          # Para programación de red y comunicación en red.
>>> xml             # Para análisis y generación de documentos XML.
>>> subprocess      # Para ejecutar comandos y procesos externos.
>>> unittest        # Para escribir y ejecutar pruebas unitarias.

### LISTA DE BIBLIOTECAS DE PYTHON [EXTERNAS]

>>> numpy           # Cálculos numéricos y arrays multidimensionales
>>> pandas          # Análisis de datos y manipulación de estructuras de datos
>>> matplotlib      # Visualización de datos y creación de gráficos
>>> scikit-learn    # Aprendizaje automático y modelado de datos
>>> tensorflow      # Desarrollo de aplicaciones de aprendizaje profundo.
>>> torch           # Desarrollo de aplicaciones de aprendizaje profundo.
>>> nltk            # Procesamiento de lenguaje natural
>>> opencv-python   # Visión por computadora y procesamiento de imágenes
>>> requests        # Realizar solicitudes HTTP y trabajar con APIs
>>> flask           # Desarrollo web
>>> django          # Desarrollo web
>>> beautifulsoup4  # Análisis de páginas web y extracción de datos.
>>> selenium        # Automatización de navegadores web

# ¡RECUERDA!
# Para usar las bibliotecas externas primero debes tenerlas instaladas:

[CMD] >>> pip3 install <nombre_de_biblioteca>

'''

===== ===== ===== ===== ===== ===== ===== =====       N  O  T  A  S      ===== ===== ===== ===== ===== ===== ===== =====


########################################################################################################################
########################################################################################################################
########################################################################################################################
###############################################                          ###############################################
###############################################       N  O  T  A  S      ###############################################
###############################################                          ###############################################
########################################################################################################################
########################################################################################################################
########################################################################################################################


[ ] > Código    ::: Caracteres Unicode
[ ] > Python    ::: Usar distintas versiones de Python
[ ] > Docstring ::: TODO
[ ] > Docstring ::: print("""\n\n\n\n""")
[ ] > Docstring ::: print(clase_o_funcion.__doc__)
[ ] > Hash
[ ] > for _ in  ::: Iterar prescindiendo de la primera variable