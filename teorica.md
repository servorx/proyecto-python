# 📔Introducción a la Programación

## 📖¿Qué es Python y porqué aprenderlo

Python es un lenguaje de programación interpretado y orientado a objetos desarrollado por Guido van Rossum en la década de 1980. Es unido al sistema operativo Unix y se utiliza para crear aplicaciones, scripts, proyecciones y ediciones gráficas.

**Características clave de Python:**

1. **Interpretación**: Python es un lenguaje de programación interpretado, lo que significa que no se compila antes de ejecutarse.
2. **Orientado a objetos**: Python utiliza conceptos orientados a objetos (OO) para crear programas más estructurados y seguros.
3. **Simplicidad**: La sintaxis de Python es simple y fácil de entender, lo que la hace accesible a programadores de todos los niveles.
4. **Librerías extensas**: Python tiene una gran cantidad de librerías extensas que simplifican el desarrollo de aplicaciones y proyectos.

**Por qué estudiar Python?**

1. **Aplicaciones prácticas**: Python es una de las lenguajes de programación más populares para la creación de aplicaciones web, programación de bases de datos, análisis de datos, inteligencia artificial y más.
2. **Desarrollo web**: Python es un lenguaje ideal para el desarrollo de aplicaciones web dinámicas, gracias a las bibliotecas como Django y Flask.
3. **Programación de bases de datos**: Python es utilizado para la creación de aplicaciones de programación de bases de datos, como SQLAlchemy y PySQLAlchemy.
4. **Análisis de datos**: Python es una herramienta popular para el análisis de datos, gracias a bibliotecas como Pandas, NumPy y Matplotlib.
5. **Ciencia de los datos**: Python se utiliza en la ciencia de los datos para la creación de modelos estadísticos, algoritmos de aprendizaje automático y más.
6. **Desarrollo de aplicaciones móviles**: Python es una opción popular para el desarrollo de aplicaciones móviles, gracias a frameworks como Kivy y Buildozer.

**Beneficios del estudio de Python:**

1. **Aprendizajes prácticos**: El estudio de Python te enseñará a programar de manera efectiva y a entender los conceptos fundamentales de la programación.
2. **Diversidad de aplicaciones**: La experiencia con Python te permitirá explorar diversas áreas de interés, desde la web hasta el análisis de datos y más.
3. **Flexibilidad**: El lenguaje de Python es muy versátil y se puede utilizar para una amplia variedad de proyectos.

En resumen, estudiar Python te permitirá aprender a programar de manera efectiva, a crear aplicaciones prácticas y a entender los conceptos fundamentales de la programación.

## 📖Introducción al modo interactivo de Python

El **modo interactivo de Python** es una de las maneras más rápidas y sencillas de trabajar con el lenguaje. Es útil para aprender, probar fragmentos de código o realizar cálculos rápidos. A continuación, se presenta una introducción detallada:

------

### 📃**¿Qué es el modo interactivo?**

El modo interactivo es una interfaz en la que puedes escribir código de Python línea por línea, recibir retroalimentación inmediata y ver el resultado de cada instrucción. Funciona como una calculadora avanzada y permite explorar el lenguaje de manera práctica.

------

### 📃**Cómo acceder al modo interactivo**

1. **Desde la terminal o línea de comandos:**

   - Abre la terminal (en Linux o macOS) o el símbolo del sistema (en Windows).

   - Escribe `python` o `python3` y presiona Enter.

   - Verás algo como esto:
   
     En windows
   
     ![](https://i.ibb.co/5k3FpK5/image.png)
   
     En Linux
   
     ![](https://i.ibb.co/DKSywrz/image.png)

2. **Desde entornos de desarrollo integrados (IDE):**
- Muchos IDEs como PyCharm, VSCode o IDLE tienen consolas interactivas integradas.

------

### 📃**Características principales**

- **Ejecución inmediata:** Cada instrucción que ingresas se ejecuta al instante y muestra el resultado.

  ```less
  >>> 2 + 2
  4
  ```

- **Exploración rápida:** Puedes probar funciones, métodos y estructuras de datos fácilmente.

  ```less
  >>> "Hola".upper()
  'HOLA'
  >>> len([1, 2, 3])
  3
  ```

- **Autocompletado y ayuda integrada:**

  - Utiliza 

    ```
    help()
    ```

     para obtener información sobre funciones, clases o módulos.

    ```
    >>> help(print)
    ```
    
  - Con teclas como `Tab`, puedes autocompletar nombres de métodos o variables (disponible en REPL mejorados como IPython).

------

### 📃**Ejemplos básicos**

1. **Usar Python como calculadora:**

   ```
   >>> 5 * 8
   40
   >>> (10 + 5) / 2
   7.5
   ```

2. **Definir variables y funciones:**

   ```
   >>> x = 10
   >>> y = 20
   >>> x + y
   30
   >>> def suma(a, b):
   ...     return a + b
   ...
   >>> suma(3, 5)
   8
   ```

3. **Probar estructuras de control:**

   ```
   >>> for i in range(3):
   ...     print(i)
   ...
   0
   1
   2
   ```

4. **Importar módulos:**

   ```
   >>> import math
   >>> math.sqrt(16)
   4.0
   ```

------

### 📃**Ventajas del modo interactivo**

- Ideal para aprender y experimentar con Python.
- Facilita la depuración rápida de código.
- Proporciona retroalimentación inmediata sobre el resultado de las instrucciones.

------

### 📃**Limitaciones del modo interactivo**

- No está diseñado para ejecutar programas largos o complejos.
- Cada vez que cierras la sesión, las variables y funciones definidas se pierden.
- Para proyectos más grandes, es mejor usar archivos `.py` y ejecutarlos en el intérprete.

------

### 📃**Alternativas mejoradas**

- IPython:

   Ofrece una experiencia interactiva más rica con características como historial avanzado, salida más clara y soporte para gráficos.

  ```
  pip install ipython
  ipython
  ```

------

​	Windows

![](https://i.ibb.co/9w33GkV/image.png)

​	Linux

![](https://i.ibb.co/PWjW894/image.png)

### 📃**Salir del modo interactivo**

- Escribe `exit()` o usa la combinación de teclas `Ctrl+D` (Linux/macOS) o `Ctrl+Z` seguido de Enter (Windows).

## 📔Palabras reservadas en Python

Las palabras reservadas en Python son identificadores predefinidos que tienen un significado especial dentro del lenguaje y no pueden ser utilizados como nombres de variables, funciones o clases. Estas palabras forman parte de la sintaxis de Python y son fundamentales para estructurar programas.

------

### 📃**Lista de palabras reservadas en Python**

A continuación, se muestra una lista de las palabras reservadas en Python (válida para versiones 3.10 y posteriores):

```less
plaintextCopiarEditarFalse      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

------

### 📃**Categorías de las palabras reservadas**

1. **Valores lógicos:**
   - `True`, `False`, `None`
2. **Control de flujo:**
   - `if`, `elif`, `else`, `while`, `for`, `break`, `continue`, `pass`
3. **Declaración de funciones y clases:**
   - `def`, `return`, `lambda`, `class`
4. **Manejo de excepciones:**
   - `try`, `except`, `finally`, `raise`, `assert`
5. **Operadores lógicos:**
   - `and`, `or`, `not`, `is`, `in`
6. **Manipulación de alcance:**
   - `global`, `nonlocal`, `del`
7. **Manejo de contexto:**
   - `with`, `as`
8. **Programación asíncrona:**
   - `async`, `await`

------

### 📃**Características importantes**

1. **Prohibido usarlas como identificadores:** Intentar utilizar una palabra reservada como nombre de una variable o función generará un error de sintaxis.

   ```less
   >>> def class():
   ...     pass
   SyntaxError: invalid syntax
   ```

2. **Sensibilidad a mayúsculas y minúsculas:** Las palabras reservadas distinguen entre letras mayúsculas y minúsculas. Por ejemplo, `True` es válido, pero `true` no lo es.

3. **Significado específico:** Cada palabra reservada tiene una función clara dentro del lenguaje, como definir estructuras condicionales, bucles, excepciones, entre otras.

------

### 📃**Ejemplo de uso**

#### **🔖Control de flujo:**

```less
if True:
    print("Esto se ejecuta")
else:
    print("Esto no se ejecutará")
```

#### 🔖**Definición de funciones:**

```
def sumar(a, b):
    return a + b
```

#### 🔖**Bucles:**

```less
for i in range(3):
    print(i)
```

#### **🔖Manejo de excepciones:**

```less
try:
    x = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre cero")
```

### 📃**Consulta de palabras reservadas**

Puede obtener la lista de palabras reservadas en Python utilizando el módulo `keyword`:

```less
import keyword
print(keyword.kwlist)
```

![](https://i.ibb.co/WsRPFD4/image.png)

## 📔Operadores matemáticos, lógicos y relacionales

### 📃Operadores Matemáticos

Los operadores matemáticos permiten realizar cálculos básicos y avanzados. A continuación, se presentan los más comunes:

| Operador | Descripción      | Ejemplo   | Resultado |
| -------- | ---------------- | --------- | --------- |
| `+`      | Suma             | `5 + 3`   | `8`       |
| `-`      | Resta            | `10 - 4`  | `6`       |
| `*`      | Multiplicación   | `2 * 3`   | `6`       |
| `/`      | División         | `10 / 4`  | `2.5`     |
| `//`     | División entera  | `10 // 4` | `2`       |
| `%`      | Módulo (residuo) | `10 % 3`  | `1`       |
| `**`     | Potenciación     | `2 ** 3`  | `8`       |

------

### 📃**Operadores relacionales (de comparación)**

Los operadores relacionales comparan valores y devuelven un valor booleano (`True` o `False`).

| Operador | Descripción       | Ejemplo  | Resultado |
| -------- | ----------------- | -------- | --------- |
| `==`     | Igual a           | `5 == 5` | `True`    |
| `!=`     | Diferente de      | `5 != 3` | `True`    |
| `>`      | Mayor que         | `10 > 5` | `True`    |
| `<`      | Menor que         | `3 < 8`  | `True`    |
| `>=`     | Mayor o igual que | `7 >= 7` | `True`    |
| `<=`     | Menor o igual que | `4 <= 6` | `True`    |

------

### 📃**Operadores lógicos**

Los operadores lógicos permiten combinar condiciones o valores booleanos.

| Operador | Descripción                              | Ejemplo          | Resultado |
| -------- | ---------------------------------------- | ---------------- | --------- |
| `and`    | Retorna `True` si ambos son `True`       | `True and False` | `False`   |
| `or`     | Retorna `True` si al menos uno es `True` | `True or False`  | `True`    |
| `not`    | Niega el valor booleano                  | `not True`       | `False`   |

------

### 📃**Ejemplos combinados**

#### **🔖Uso de operadores matemáticos:**

```less
x = 10
y = 3

print(x + y)  # 13
print(x % y)  # 1
print(x ** y) # 1000
```

#### 🔖**Uso de operadores relacionales:**

```less
a = 5
b = 7

print(a > b)  # False
print(a <= b) # True
```

#### 🔖**Uso de operadores lógicos:**

```less
x = 5
y = 10

print(x > 2 and y < 15) # True
print(x < 0 or y > 15)  # False
print(not(x == 5))      # False
```

## 📔Entrada y salida  de usuario por modo interactivo

En Python, la entrada y salida de usuario en modo interactivo permite interactuar con el programa, solicitando datos al usuario y mostrando resultados. Esto se logra principalmente con las funciones integradas `input()` para la entrada y `print()` para la salida.

------

### 📃**Entrada de usuario con `input()`**

La función `input()` permite al usuario ingresar datos desde el teclado.

#### 📃**Sintaxis básica:**

```python
variable = input("Mensaje al usuario: ")
```

- `input()` siempre devuelve el valor ingresado como una **cadena de texto** (tipo `str`).

#### 📃**Ejemplo de uso:**

```python
nombre = input("¿Cuál es tu nombre? ")
print("Hola,", nombre)
```

#### 📃**Convertir la entrada a otros tipos de datos:**

Si se necesita un valor numérico, es necesario convertir explícitamente el valor ingresado:

```python
edad = int(input("¿Cuántos años tienes? "))
print("El próximo año tendrás", edad + 1, "años.")
```

------

### 📖**Salida de datos con `print()`**

La función `print()` muestra información en la pantalla.

#### 📃**Sintaxis básica:**

```python
print(valor1, valor2, ..., sep=' ', end='\n')
```

- **`sep`**: Define el separador entre valores (por defecto, un espacio `' '`).
- **`end`**: Define lo que se agrega al final de la línea (por defecto, un salto de línea `'\n'`).

#### 📃**Ejemplos de uso:**

```python
print("Hola, mundo")  # Salida: Hola, mundo
print("Python", "es", "genial", sep="-")  # Salida: Python-es-genial
print("Fin", end="!")  # Salida: Fin!
```

------

#### 📃**Ejemplo combinado: Calculadora interactiva**

Un programa que pide dos números y muestra la suma:

```python
print("Bienvenido a la calculadora interactiva.")
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
suma = num1 + num2
print("La suma de los números es:", suma)
```

------

## **Uso avanzado de `print()` con formato**

La función `print()` admite el uso de cadenas formateadas para una salida más legible.

#### **Formato con `f-strings` (Python 3.6+):**

```python
nombre = "Ana"
edad = 25
print(f'Hola, {nombre}. Tienes {edad} años.')
```

![](https://i.ibb.co/FXtVxt3/image.png)

#### **Formato con `str.format()`:**

```python
print("Hola, {}. Tienes {} años.".format("Ana", 25))
```

![](https://i.ibb.co/YfFPgKq/image.png)

# 📔**Manejo de excepciones en la entrada**

Para evitar errores si el usuario ingresa datos no válidos, se pueden usar excepciones:

```python
try:
    numero = int(input("Introduce un número entero: "))
    print("El doble de tu número es:", numero * 2)
except ValueError:
    print("Por favor, introduce un número válido.")
```

------

# 📔Variables y tipos de datos

### **📖Variables y constantes**

#### 📃**Definición de variables**

Una **variable** es un espacio en la memoria que se utiliza para almacenar datos. En Python, las variables no necesitan ser declaradas con un tipo de dato explícito, ya que Python es un lenguaje de tipado dinámico.

**Sintaxis básica:**

```python
nombre_variable = valor
```

**Ejemplo:**

```python
nombre = "Juan"
edad = 25
es_estudiante = True
```

- Reglas para nombrar variables:
  - Deben comenzar con una letra o un guion bajo (`_`).
  - No pueden empezar con un número.
  - No pueden contener espacios ni caracteres especiales.
  - No se deben usar palabras reservadas de Python.

#### 📃**Constantes**

Aunque Python no tiene una forma nativa de declarar constantes, se sigue una convención: usar nombres en **mayúsculas** para indicar que el valor no debe cambiar.

**Ejemplo:**

```python
PI = 3.14159
GRAVEDAD = 9.8
```

------

### 📖**Tipos de datos básicos**

Python ofrece tres tipos de datos básicos más comunes:

#### 📃**Numéricos**

- **Enteros (`int`):** Números sin decimales.

  ```python
  entero = 42
  ```

- **Flotantes (`float`):** Números con decimales.

  ```python
  flotante = 3.14
  ```

- **Complejos (`complex`):** Números con parte real e imaginaria.

  ```python
  complejo = 2 + 3j
  ```

#### 📃**Cadenas de texto (`str`)**

- Se utilizan para almacenar texto, definido entre comillas simples (`'`) o dobles (`"`).

  ```python
  saludo = "Hola, mundo"
  ```

- Soportan operaciones como concatenación y repetición:

  ```python
  mensaje = "Hola" + " " + "Mundo"
  print(mensaje)  # Salida: Hola Mundo
  
  repetido = "Hola" * 3
  print(repetido)  # Salida: HolaHolaHola
  ```

#### 📃**Booleanos (`bool`)**

- Representan valores de verdad: 

  ```
  True
  ```

   o 

  ```
  False
  ```

  .

  ```python
  es_activo = True
  print(type(es_activo))  # Salida: <class 'bool'>
  ```

------

### 📖**Conversión de tipos de datos o "casting"**

En Python, es posible convertir un tipo de dato en otro utilizando funciones de conversión.

#### 📃**Conversión implícita**

Python realiza conversiones automáticas cuando no hay pérdida de información:

```python
num_entero = 5
num_flotante = 2.0
resultado = num_entero + num_flotante
print(resultado)  # Salida: 7.0
```

#### 📃**Conversión explícita**

Se usa cuando es necesario transformar un tipo de dato de forma manual.

**Funciones comunes:**

- `int()`: Convierte a entero.

  ```python
  entero = int(3.7)
  print(entero)  # Salida: 3
  ```

- `float()`: Convierte a flotante.

  ```python
  flotante = float(5)
  print(flotante)  # Salida: 5.0
  ```

- `str()`: Convierte a cadena.

  ```python
  texto = str(42)
  print(texto)  # Salida: "42"
  ```

- `bool()`: Convierte a booleano.

  ```python
  valor = bool(0)
  print(valor)  # Salida: False
  ```

#### 🔖**Ejemplo práctico de conversión de tipos:**

```python
edad = "25"  # Cadena
edad_entera = int(edad)  # Conversión a entero
print(edad_entera + 5)  # Salida: 30
```

------

#### 📜**Resumen final**

- Las **variables** almacenan datos y las **constantes** se usan para valores que no cambian.
- Los **tipos de datos básicos** son numéricos, cadenas y booleanos.
- La **conversión de tipos** permite transformar datos entre distintos tipos, ya sea de forma implícita o explícita. Esto es útil para operaciones entre datos de diferentes tipos.

# 📔Estructuras de control

### 📖**Condiciones: `if` y `else`**

Las estructuras condicionales permiten ejecutar diferentes bloques de código dependiendo de si una condición se cumple o no.

#### **Sintaxis básica:**

```python
if condición:
    # Código a ejecutar si la condición es verdadera
else:
    # Código a ejecutar si la condición es falsa
```

#### **Ejemplo básico:**

```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

#### **Uso de `elif`:**

Se utiliza cuando hay múltiples condiciones.

```python
nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")
```

### 📖**`match` (Switch)**

A partir de Python 3.10, la declaración `match` permite realizar múltiples comparaciones de manera más legible.

#### **Sintaxis básica:**

```python
match variable:
    case valor1:
        # Código si variable == valor1
    case valor2:
        # Código si variable == valor2
    case _:
        # Código para cualquier otro caso
```

#### **Ejemplo:**

```python
opcion = 2
match opcion:
    case 1:
        print("Elegiste opción 1")
    case 2:
        print("Elegiste opción 2")
    case _:
        print("Opción no válida")
```

### 📖**Bucle `while`**

El bucle `while` ejecuta un bloque de código mientras una condición sea verdadera.

#### **Sintaxis básica**

```less
while condición:
    # Código a ejecutar mientras la condición sea verdadera
```

#### **Ejemplo básico**

```less
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
```

#### **Bucle infinito**

Un `while` sin una condición de salida puede generar un bucle infinito.

```less
while True:
    entrada = input("Escribe 'salir' para terminar: ")
    if entrada == "salir":
        break
```

### 📖**Bucle `for`**

El bucle `for` se utiliza para iterar sobre elementos de una secuencia como listas, cadenas o rangos.

#### **Sintaxis básica:**

```python
for elemento in secuencia:
    # Código a ejecutar por cada elemento
```

#### **Ejemplo básico:**

```python
frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)
```

#### **Uso con `range()`:**

```python
for i in range(1, 6):
    print(i)
```

### 📖**`continue`, `break` y `else` en bucles**

Estos comandos permiten controlar la ejecución dentro de un bucle.

#### 📃**`break`:**

Finaliza el bucle de forma inmediata.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

#### 📃**`continue`:**

Omite la iteración actual y pasa a la siguiente.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

#### 📃**`else`:**

El bloque `else` en un bucle se ejecuta cuando el bucle termina de forma normal (sin un `break`).

```python
for i in range(5):
    print(i)
else:
    print("Bucle completado")
```

# 📔Manejo de errores con Try, Except y Finally

El manejo de errores en Python se realiza mediante las sentencias `try`, `except`, y `finally`. Estas estructuras permiten gestionar situaciones en las que el código puede generar errores, asegurando que el programa no se detenga inesperadamente y ofreciendo soluciones controladas a los problemas.

------

### 📖**¿Qué es el manejo de errores?**

El manejo de errores consiste en anticipar posibles excepciones (errores) que puedan surgir durante la ejecución de un programa y definir cómo responder ante ellas. Esto mejora la robustez y estabilidad del código.

------

### 📖**La estructura básica**

#### **Sintaxis:**

```python
try:
    # Código que puede generar un error
except ExcepcionEspecifica:
    # Código que se ejecuta si ocurre la excepción especificada
finally:
    # Código que se ejecuta siempre, ocurra o no una excepción (opcional)
```

------

### 📖**Explicación de las cláusulas**

#### **📃`try`:**

Contiene el código que se ejecuta normalmente, pero que puede generar una excepción.

#### **📃 `except`:**

Se ejecuta solo si ocurre una excepción en el bloque `try`. Puede manejar excepciones específicas o generales.

**Ejemplo de manejo específico:**

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
```

**Ejemplo de manejo general:**

```python
try:
    resultado = int("texto")
except Exception as e:
    print(f"Error general: {e}")
```

#### **📃 `finally`:**

Se ejecuta siempre, independientemente de si ocurre o no una excepción. Útil para realizar acciones de limpieza como cerrar archivos o liberar recursos.

**Ejemplo:**

```python
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
finally:
    print("Finalizando proceso...")
    if 'archivo' in locals() and not archivo.closed:
        archivo.close()
```

------

### 📖**Capturar múltiples excepciones**

Un bloque `try` puede manejar diferentes tipos de excepciones usando varios bloques `except`:

```python
try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
except ValueError:
    print("Debes introducir un número válido.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
```

------

### 📖**Usar `else` en el manejo de errores**

La cláusula `else` se ejecuta si no se produce ninguna excepción en el bloque `try`. Es útil para realizar acciones solo cuando no hubo errores.

**Ejemplo:**

```python
try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
else:
    print("Operación exitosa. Resultado:", resultado)
finally:
    print("Fin del programa.")
```

### 📖Tipos de excepciones
| **Tipo de Error**        | **Descripción**                                                                 | **Ejemplo**                                                                                     |
|---------------------------|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| **`SyntaxError`**         | Se genera cuando hay un error en la sintaxis del código, lo que impide que sea interpretado. | ```python\nif True print("Hola")\n``` **Salida:** `SyntaxError: expected ':'`                 |
| **`IndentationError`**    | Se produce cuando hay un problema con la indentación, como faltas o exceso de espacios.       | ```python\ndef funcion():\nprint("Hola")\n``` **Salida:** `IndentationError: expected an indented block` |
| **`NameError`**           | Ocurre cuando se intenta usar una variable o función que no ha sido definida.               | ```python\nprint(x)\n``` **Salida:** `NameError: name 'x' is not defined`                     |
| **`TypeError`**           | Se lanza cuando se realiza una operación no permitida entre tipos incompatibles.            | ```python\nresultado = "texto" + 5\n``` **Salida:** `TypeError: can only concatenate str (not "int") to str` |
| **`ValueError`**          | Ocurre cuando se proporciona un valor inapropiado para una operación válida.                | ```python\nnumero = int("texto")\n``` **Salida:** `ValueError: invalid literal for int() with base 10: 'texto'` |
| **`ZeroDivisionError`**   | Se genera cuando se intenta dividir un número entre cero, lo cual no está permitido.         | ```python\nresultado = 10 / 0\n``` **Salida:** `ZeroDivisionError: division by zero`          |
| **`IndexError`**          | Se lanza cuando se intenta acceder a un índice que está fuera del rango de una lista o secuencia. | ```python\nlista = [1, 2, 3]\nprint(lista[5])\n``` **Salida:** `IndexError: list index out of range` |
| **`KeyError`**            | Se produce cuando se intenta acceder a una clave inexistente en un diccionario.             | ```python\ndiccionario = {"a": 1}\nprint(diccionario["b"])\n``` **Salida:** `KeyError: 'b'`   |
| **`AttributeError`**      | Ocurre cuando se intenta acceder a un atributo que no existe en un objeto.                  | ```python\ntexto = "Hola"\ntexto.append("!")\n``` **Salida:** `AttributeError: 'str' object has no attribute 'append'` |
| **`ModuleNotFoundError`** | Se genera cuando se intenta importar un módulo que no está disponible o no existe.          | ```python\nimport modulo_inexistente\n``` **Salida:** `ModuleNotFoundError: No module named 'modulo_inexistente'` |
| **`ImportError`**         | Ocurre cuando un módulo existe, pero hay problemas al importar algo específico.             | ```python\nfrom math import raiz\n``` **Salida:** `ImportError: cannot import name 'raiz' from 'math'` |
| **`FileNotFoundError`**   | Se lanza cuando se intenta abrir un archivo que no existe en el sistema.                    | ```python\nwith open("archivo_inexistente.txt", "r") as archivo:\n    contenido = archivo.read()\n``` **Salida:** `FileNotFoundError: [Errno 2] No such file or directory: 'archivo_inexistente.txt'` |
| **`IOError`**             | Ocurre durante operaciones de entrada/salida que fallan, como leer o escribir un archivo.   | ```python\nwith open("/ruta_protegida/archivo.txt", "w") as archivo:\n    archivo.write("Texto")\n``` **Salida:** `IOError: [Errno 13] Permission denied: '/ruta_protegida/archivo.txt'` |
| **`OverflowError`**       | Se produce cuando un cálculo numérico excede el límite permitido.                          | ```python\nimport math\nresultado = math.exp(1000)\n``` **Salida:** `OverflowError: math range error` |
| **`RecursionError`**      | Se lanza cuando se excede el límite de recursión permitido en una función recursiva.        | ```python\ndef recursiva():\n    return recursiva()\nrecursiva()\n``` **Salida:** `RecursionError: maximum recursion depth exceeded` |
| **`MemoryError`**         | Se genera cuando el sistema no tiene suficiente memoria para completar una operación.       | ```python\nlista = [1] * (10**10)\n``` **Salida:** `MemoryError`                              |
| **`RuntimeError`**        | Error genérico que ocurre en tiempo de ejecución por condiciones inesperadas.               | ```python\nraise RuntimeError("Error inesperado")\n``` **Salida:** `RuntimeError: Error inesperado` |

# 📔Cadena de Caracteres

## 📖**Métodos para Manipulación Básica**

Python proporciona varios métodos integrados para manipular cadenas de caracteres. Estos permiten modificar, buscar, reemplazar o dividir cadenas fácilmente.

### 📃**Principales métodos:**

| **Método**              | **Descripción**                                              | **Ejemplo**                             | **Resultado**       |
| ----------------------- | ------------------------------------------------------------ | --------------------------------------- | ------------------- |
| `len(cadena)`           | Devuelve la longitud de la cadena.                           | `len("Hola")`                           | `4`                 |
| `cadena.lower()`        | Convierte todos los caracteres de la cadena a minúsculas.    | `"Hola".lower()`                        | `"hola"`            |
| `cadena.upper()`        | Convierte todos los caracteres de la cadena a mayúsculas.    | `"Hola".upper()`                        | `"HOLA"`            |
| `cadena.strip()`        | Elimina espacios en blanco al inicio y al final de la cadena. | `" Hola ".strip()`                      | `"Hola"`            |
| `cadena.replace(a, b)`  | Reemplaza todas las ocurrencias de `a` por `b` en la cadena. | `"Hola Mundo".replace("Hola", "Adiós")` | `"Adiós Mundo"`     |
| `cadena.split(sep)`     | Divide la cadena en una lista de palabras utilizando el separador `sep`. | `"Hola Mundo".split(" ")`               | `["Hola", "Mundo"]` |
| `cadena.join(iterable)` | Une los elementos de un iterable en una sola cadena usando `cadena` como separador. | `" ".join(["Hola", "Mundo"])`           | `"Hola Mundo"`      |

------

## 📖**Métodos para Validación**

Estos métodos se utilizan para verificar si una cadena cumple con ciertas condiciones. Devuelven un valor booleano (`True` o `False`).

### 📃**Principales métodos:**

| **Método**                   | **Descripción**                                              | **Ejemplo**                       | **Resultado** |
| ---------------------------- | ------------------------------------------------------------ | --------------------------------- | ------------- |
| `cadena.isalpha()`           | Retorna `True` si todos los caracteres son alfabéticos.      | `"Hola".isalpha()`                | `True`        |
| `cadena.isdigit()`           | Retorna `True` si todos los caracteres son dígitos.          | `"1234".isdigit()`                | `True`        |
| `cadena.isalnum()`           | Retorna `True` si todos los caracteres son alfanuméricos (letras o números). | `"Hola123".isalnum()`             | `True`        |
| `cadena.isspace()`           | Retorna `True` si todos los caracteres son espacios en blanco. | `" ".isspace()`                   | `True`        |
| `cadena.startswith(prefijo)` | Retorna `True` si la cadena comienza con el prefijo especificado. | `"Hola Mundo".startswith("Hola")` | `True`        |
| `cadena.endswith(sufijo)`    | Retorna `True` si la cadena termina con el sufijo especificado. | `"Hola Mundo".endswith("Mundo")`  | `True`        |

------

## 📖**Métodos de Formateo**

Estos métodos permiten ajustar o modificar el formato de una cadena.

### 📃**Principales métodos:**

| **Método**                       | **Descripción**                                              | **Ejemplo**                          | **Resultado**   |
| -------------------------------- | ------------------------------------------------------------ | ------------------------------------ | --------------- |
| `cadena.center(ancho)`           | Centra la cadena dentro de un espacio de ancho especificado. | `"Hola".center(10)`                  | `" Hola "`      |
| `cadena.ljust(ancho)`            | Justifica la cadena a la izquierda con un ancho especificado. | `"Hola".ljust(10)`                   | `"Hola "`       |
| `cadena.rjust(ancho)`            | Justifica la cadena a la derecha con un ancho especificado.  | `"Hola".rjust(10)`                   | `" Hola"`       |
| `cadena.zfill(ancho)`            | Rellena la cadena con ceros a la izquierda hasta alcanzar el ancho especificado. | `"123".zfill(5)`                     | `"00123"`       |
| `cadena.format(*args, **kwargs)` | Reemplaza marcadores de posición `{}` en la cadena con los valores proporcionados. | `"Hola, {}".format("Mundo")`         | `"Hola, Mundo"` |
| `f"Código {variable}"`           | Cadenas formateadas (`f-strings`), permite insertar variables en la cadena. | `nombre = "Juan"; f"Hola, {nombre}"` | `"Hola, Juan"`  |

## ❇**Taller Guiado: Trabajando con Cadenas de Caracteres en Python**

Este taller está diseñado para practicar el uso de cadenas de caracteres en Python. Cada ejercicio tiene instrucciones claras y una explicación de cómo resolverlo.

------

### **Objetivo del taller**

- Aprender a manipular, validar y formatear cadenas de caracteres.
- Usar los métodos básicos de las cadenas para resolver problemas prácticos.

------

### **Ejercicio 1: Contando caracteres**

#### **Instrucción:**

Escribe un programa que solicite al usuario una frase y muestre:

1. La cantidad total de caracteres en la frase.
2. La cantidad de espacios en la frase.

#### **Guía:**

1. Usa `len()` para contar el total de caracteres.
2. Usa el método `count()` para contar los espacios.

#### **Código base:**

```python
frase = input("Escribe una frase: ")
total_caracteres = len(frase)
espacios = frase.count(" ")

print(f"La frase tiene {total_caracteres} caracteres en total.")
print(f"La frase tiene {espacios} espacios.")
```

------

### **Ejercicio 2: Validando nombres**

#### **Instrucción:**

Crea un programa que solicite al usuario su nombre completo y verifique:

1. Que solo contenga letras.
2. Que comience con mayúscula.

#### **Guía:**

1. Usa `isalpha()` para verificar que solo hay letras.
2. Usa `istitle()` para verificar que las palabras comiencen con mayúscula.

#### **Código base:**

```python
nombre = input("Escribe tu nombre completo: ")

if nombre.replace(" ", "").isalpha():
    if nombre.istitle():
        print("El nombre es válido.")
    else:
        print("El nombre debe comenzar con mayúscula.")
else:
    print("El nombre solo debe contener letras.")
```

------

### **Ejercicio 3: Invirtiendo palabras**

#### **Instrucción:**

Escribe un programa que pida al usuario una palabra y muestre la palabra invertida.

#### **Guía:**

1. Usa el operador de slicing `[::-1]` para invertir la cadena.

#### **Código base:**

```python
palabra = input("Escribe una palabra: ")
invertida = palabra[::-1]
print(f"La palabra invertida es: {invertida}")
```

------

### **Ejercicio 4: Cifrando texto**

#### **Instrucción:**

Crea un programa que solicite al usuario una frase y reemplace todas las vocales por un carácter especial (*).

#### **Guía:**

1. Usa `replace()` repetidamente para reemplazar las vocales.
2. Asegúrate de manejar tanto mayúsculas como minúsculas.

#### **Código base:**

```python
frase = input("Escribe una frase: ")

frase_cifrada = frase.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*")
frase_cifrada = frase_cifrada.replace("A", "*").replace("E", "*").replace("I", "*").replace("O", "*").replace("U", "*")

print(f"La frase cifrada es: {frase_cifrada}")
```

------

### **Ejercicio 5: Contador de vocales**

#### **Instrucción:**

Escribe un programa que cuente cuántas vocales hay en una frase ingresada por el usuario.

#### **Guía:**

1. Usa `count()` para contar las vocales individualmente.
2. Suma los resultados.

#### **Código base:**

```python
frase = input("Escribe una frase: ")

a = frase.count("a") + frase.count("A")
e = frase.count("e") + frase.count("E")
i = frase.count("i") + frase.count("I")
o = frase.count("o") + frase.count("O")
u = frase.count("u") + frase.count("U")

total_vocales = a + e + i + o + u

print(f"La frase tiene {total_vocales} vocales.")
```

------

### **Ejercicio 6: Formateando cadenas**

#### **Instrucción:**

Escribe un programa que tome un número de teléfono ingresado por el usuario (10 dígitos) y lo formatee como `(XXX) XXX-XXXX`.

#### **Guía:**

1. Usa slicing para dividir la cadena en partes.
2. Usa `f-strings` o concatenación para formatear.

#### **Código base:**

```python
telefono = input("Escribe un número de teléfono de 10 dígitos: ")
if len(telefono) == 10 and telefono.isdigit():
    telefono_formateado = f"({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}"
    print(f"El número formateado es: {telefono_formateado}")
else:
    print("El número debe tener exactamente 10 dígitos.")
```

------

### **Ejercicio 7: Detectando palíndromos**

#### **Instrucción:**

Escribe un programa que determine si una palabra ingresada por el usuario es un palíndromo (se lee igual al derecho y al revés).

#### **Guía:**

1. Usa slicing para invertir la palabra.
2. Compara la palabra original con la invertida.

#### **Código base:**

```python
palabra = input("Escribe una palabra: ").lower()
invertida = palabra[::-1]

if palabra == invertida:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
```

# 📔Estructuras de datos

## 📖Listas

Las listas en Python son estructuras de datos **ordenadas**, **mutables** y que pueden contener elementos de cualquier tipo (números, cadenas, otros objetos, incluso otras listas). Son muy flexibles y se utilizan para almacenar colecciones de elementos.

#### 📃**Características clave:**

- Las listas están delimitadas por corchetes (`[]`).
- Los elementos están separados por comas.
- Pueden contener datos heterogéneos.

**Ejemplo básico:**

```python
pythonCopiarEditarmi_lista = [1, "Python", True, 3.14]
print(mi_lista)  # Salida: [1, 'Python', True, 3.14]
```

------

#### 📃**Creación de listas**

Existen varias formas de crear listas en Python.

##### **🔖Listas literales:**

Se crean directamente utilizando corchetes (`[]`).

```python
mi_lista = [1, 2, 3]
```

##### **🔖 Listas vacías:**

```python
lista_vacia = []
```

##### **🔖Usando el constructor `list()`:**

```python
mi_lista = list((1, 2, 3))  # Se pasa una tupla como argumento
```

##### **🔖Con comprensión de listas:**

Una forma concisa de crear listas usando bucles.

```python
cuadrados = [x**2 for x in range(5)]  # Salida: [0, 1, 4, 9, 16]
```

------

### 📃**Manipulación de listas**

Python proporciona muchos métodos y operadores para manipular listas.

#### **🔖`append(x)`**

Añade un elemento al final de la lista.

**Ejemplo:**

```
mi_lista = [1, 2, 3]
mi_lista.append(4)
print(mi_lista)  # Salida: [1, 2, 3, 4]
```

------

#### 🔖

Extiende la lista añadiendo todos los elementos de un iterable (como otra lista, una tupla o un string).

**Ejemplo:**

```
mi_lista = [1, 2, 3]
mi_lista.extend([4, 5, 6])
print(mi_lista)  # Salida: [1, 2, 3, 4, 5, 6]
```

------

#### **🔖`insert(i, x)`**

Inserta un elemento en una posición específica. `i` es el índice donde se insertará el elemento.

**Ejemplo:**

```
mi_lista = [1, 2, 3]
mi_lista.insert(1, "Python")
print(mi_lista)  # Salida: [1, 'Python', 2, 3]
```

------

#### **🔖 `remove(x)`**

Elimina la primera aparición del valor `x` en la lista. Lanza un error si el valor no está presente.

**Ejemplo:**

```
mi_lista = [1, 2, 3, 2]
mi_lista.remove(2)
print(mi_lista)  # Salida: [1, 3, 2]
```

------

#### **🔖 `pop([i])`**

Elimina y devuelve el elemento en la posición `i`. Si no se especifica `i`, elimina y devuelve el último elemento.

**Ejemplo:**

```
mi_lista = [1, 2, 3]
ultimo = mi_lista.pop()
print(ultimo)  # Salida: 3
print(mi_lista)  # Salida: [1, 2]
```

------

#### **🔖`clear()`**

Elimina todos los elementos de la lista, dejándola vacía.

**Ejemplo:**

```
mi_lista = [1, 2, 3]
mi_lista.clear()
print(mi_lista)  # Salida: []
```

------

#### **🔖 `index(x[, start[, end]])`**

Devuelve el índice de la primera aparición de `x` en la lista. Opcionalmente, se puede buscar dentro de un rango con `start` y `end`.

**Ejemplo:**

```
mi_lista = [10, 20, 30, 20]
indice = mi_lista.index(20)
print(indice)  # Salida: 1
```

**Con rango:**

```
indice = mi_lista.index(20, 2)
print(indice)  # Salida: 3
```

------

#### **🔖`count(x)`**

Devuelve el número de veces que `x` aparece en la lista.

**Ejemplo:**

```
mi_lista = [1, 2, 2, 3, 2]
cantidad = mi_lista.count(2)
print(cantidad)  # Salida: 3
```

------

#### **🔖`sort(key=None, reverse=False)`**

Ordena los elementos de la lista de menor a mayor (por defecto). Se puede personalizar el orden con los parámetros:

- **`key`:** Una función que define el criterio de orden.
- **`reverse`:** Si es `True`, ordena de mayor a menor.

**Ejemplo básico:**

```
mi_lista = [3, 1, 4, 2]
mi_lista.sort()
print(mi_lista)  # Salida: [1, 2, 3, 4]
```

**Orden descendente:**

```
mi_lista.sort(reverse=True)
print(mi_lista)  # Salida: [4, 3, 2, 1]
```

**Con clave personalizada:**

```
mi_lista = ["hola", "Python", "mundo"]
mi_lista.sort(key=len)
print(mi_lista)  # Salida: ['hola', 'mundo', 'Python']
```

------

#### **🔖`reverse()`**

Invierte el orden de los elementos en la lista.

**Ejemplo:**

```
mi_lista = [1, 2, 3]
mi_lista.reverse()
print(mi_lista)  # Salida: [3, 2, 1]
```

------

#### **🔖 `copy()`**

Devuelve una copia superficial de la lista. Los cambios en la copia no afectan a la lista original.

**Ejemplo:**

```
mi_lista = [1, 2, 3]
copia = mi_lista.copy()
copia.append(4)
print(mi_lista)  # Salida: [1, 2, 3]
print(copia)     # Salida: [1, 2, 3, 4]
```

------

#### 📒**Resumen de Métodos de Listas**

| **Método**         | **Descripción**                                              |
| ------------------ | ------------------------------------------------------------ |
| `append(x)`        | Añade un elemento al final de la lista.                      |
| `extend(iterable)` | Añade todos los elementos de un iterable a la lista.         |
| `insert(i, x)`     | Inserta un elemento en la posición especificada.             |
| `remove(x)`        | Elimina la primera aparición del valor dado.                 |
| `pop([i])`         | Elimina y devuelve el elemento en la posición especificada (o el último). |
| `clear()`          | Elimina todos los elementos de la lista.                     |
| `index(x[, s, e])` | Devuelve el índice de la primera aparición de un valor.      |
| `count(x)`         | Cuenta cuántas veces aparece un valor en la lista.           |
| `sort()`           | Ordena los elementos de la lista.                            |
| `reverse()`        | Invierte el orden de los elementos de la lista.              |
| `copy()`           | Devuelve una copia de la lista.                              |

## 📖**Lista de listas**

Las listas pueden contener otras listas, lo que permite crear estructuras anidadas (matrices, tablas, etc.).

#### 📃**Acceso a listas anidadas:**

```python
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[0])       # Salida: [1, 2, 3]
print(matriz[0][1])    # Salida: 2
```

#### **📃Manipulación de listas anidadas:**

```python
matriz[1].append(10)
print(matriz)  # Salida: [[1, 2, 3], [4, 5, 6, 10], [7, 8, 9]]
```

------

#### **Resumen**

Las listas en Python son una estructura de datos fundamental que permite almacenar y manipular colecciones de elementos de forma flexible. Aprender a usarlas de manera eficiente, incluyendo su creación, manipulación y uso en estructuras más complejas como listas anidadas, es clave para desarrollar programas robustos.

## 📔Diccionarios

### 📖**Conceptos básicos**

Un diccionario en Python es una colección de pares clave-valor, donde:

- Cada clave es única e inmutable (puede ser un número, cadena o tupla).
- Cada valor está asociado con una clave y puede ser de cualquier tipo.

### 📖**Características principales:**

- Los diccionarios son mutables (pueden modificarse después de ser creados).
- No admiten claves duplicadas, pero los valores sí pueden repetirse.

#### **Ejemplo básico:**

```python
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Bogotá"
}
print(mi_diccionario)  # Salida: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Bogotá'}
```

### 📖**Creación de diccionarios**

Python ofrece varias formas de crear diccionarios.

#### **a) Usando llaves (`{}`):**

```python
diccionario = {"clave1": "valor1", "clave2": "valor2"}
```

#### **b) Usando el constructor `dict()`:**

```python
diccionario = dict(clave1="valor1", clave2="valor2")
```

#### **c) Diccionario vacío:**

```python
diccionario = {}
```

#### **d) Usando `zip()`:**

Asocia elementos de dos listas para formar pares clave-valor.

```python
claves = ["nombre", "edad", "ciudad"]
valores = ["Ana", 25, "Medellín"]
diccionario = dict(zip(claves, valores))
print(diccionario)  # Salida: {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Medellín'}
```

### 📖Metodos

#### **1. `dict.get(clave, valor_por_defecto=None)`**

Obtiene el valor asociado a una clave. Si la clave no existe, devuelve un valor por defecto (por defecto es `None`).

**Ejemplo:**

```python
diccionario = {"nombre": "Ana", "edad": 25}
print(diccionario.get("nombre"))  # Salida: Ana
print(diccionario.get("ciudad", "No especificado"))  # Salida: No especificado
```

------

#### **2. `dict.keys()`**

Devuelve una vista de todas las claves del diccionario.

**Ejemplo:**

```python
diccionario = {"nombre": "Ana", "edad": 25}
print(diccionario.keys())  # Salida: dict_keys(['nombre', 'edad'])
```

------

#### **3. `dict.values()`**

Devuelve una vista de todos los valores del diccionario.

**Ejemplo:**

```python
diccionario = {"nombre": "Ana", "edad": 25}
print(diccionario.values())  # Salida: dict_values(['Ana', 25])
```

------

#### **4. `dict.items()`**

Devuelve una vista de todos los pares clave-valor como tuplas.

**Ejemplo:**

```python
diccionario = {"nombre": "Ana", "edad": 25}
print(diccionario.items())  # Salida: dict_items([('nombre', 'Ana'), ('edad', 25)])
```

------

#### **5. `dict.update(otro_diccionario)`**

Actualiza el diccionario con los pares clave-valor de otro diccionario o iterable.

**Ejemplo:**

```python
diccionario = {"nombre": "Ana"}
nuevo_datos = {"edad": 25, "ciudad": "Bogotá"}
diccionario.update(nuevo_datos)
print(diccionario)  # Salida: {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Bogotá'}
```

------

#### **6. `dict.pop(clave, valor_por_defecto)`**

Elimina la clave especificada y devuelve su valor. Si la clave no existe, devuelve el valor por defecto.

**Ejemplo:**

```python
diccionario = {"nombre": "Ana", "edad": 25}
edad = diccionario.pop("edad")
print(edad)  # Salida: 25
print(diccionario)  # Salida: {'nombre': 'Ana'}
```

------

#### **7. `dict.popitem()`**

Elimina y devuelve un par clave-valor aleatorio (en Python 3.7+ elimina el último).

**Ejemplo:**

```python
diccionario = {"nombre": "Ana", "edad": 25}
par = diccionario.popitem()
print(par)  # Salida: ('edad', 25)
print(diccionario)  # Salida: {'nombre': 'Ana'}
```

------

#### **8. `dict.clear()`**

Elimina todos los elementos del diccionario, dejándolo vacío.

**Ejemplo:**

```python
diccionario = {"nombre": "Ana", "edad": 25}
diccionario.clear()
print(diccionario)  # Salida: {}
```

------

#### **9. `dict.copy()`**

Devuelve una copia superficial del diccionario.

**Ejemplo:**

```python
diccionario = {"nombre": "Ana", "edad": 25}
copia = diccionario.copy()
copia["ciudad"] = "Bogotá"
print(diccionario)  # Salida: {'nombre': 'Ana', 'edad': 25}
print(copia)  # Salida: {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Bogotá'}
```

------

#### **10. `dict.setdefault(clave, valor_por_defecto)`**

Devuelve el valor de la clave si existe. Si no, agrega la clave con el valor por defecto y devuelve ese valor.

**Ejemplo:**

```python
diccionario = {"nombre": "Ana"}
valor = diccionario.setdefault("ciudad", "Bogotá")
print(valor)  # Salida: Bogotá
print(diccionario)  # Salida: {'nombre': 'Ana', 'ciudad': 'Bogotá'}
```

------

#### **11. `dict.fromkeys(iterable, valor_por_defecto=None)`**

Crea un diccionario con las claves del iterable y un valor por defecto para cada clave.

**Ejemplo:**

```python
claves = ["nombre", "edad", "ciudad"]
diccionario = dict.fromkeys(claves, "Desconocido")
print(diccionario)  # Salida: {'nombre': 'Desconocido', 'edad': 'Desconocido', 'ciudad': 'Desconocido'}
```

------

#### **12. Comparando diccionarios**

Se pueden usar operadores de comparación para verificar igualdad.

**Ejemplo:**

```python
diccionario1 = {"nombre": "Ana", "edad": 25}
diccionario2 = {"edad": 25, "nombre": "Ana"}
print(diccionario1 == diccionario2)  # Salida: True
```

------

#### **Resumen de Métodos**

| **Método**                      | **Descripción**                                              |
| ------------------------------- | ------------------------------------------------------------ |
| `get(clave, valor_por_defecto)` | Devuelve el valor de una clave o un valor por defecto.       |
| `keys()`                        | Devuelve todas las claves del diccionario.                   |
| `values()`                      | Devuelve todos los valores del diccionario.                  |
| `items()`                       | Devuelve todos los pares clave-valor como tuplas.            |
| `update()`                      | Actualiza el diccionario con pares clave-valor de otro.      |
| `pop(clave, valor_por_defecto)` | Elimina y devuelve el valor asociado a una clave.            |
| `popitem()`                     | Elimina y devuelve un par clave-valor aleatorio.             |
| `clear()`                       | Elimina todos los elementos del diccionario.                 |
| `copy()`                        | Devuelve una copia superficial del diccionario.              |
| `setdefault(clave, valor)`      | Devuelve el valor de una clave, si no existe la agrega con el valor dado. |
| `fromkeys(iterable, valor)`     | Crea un diccionario con las claves del iterable y un valor común. |

# 📔Persistencia

### 📖**Persistencia en Programación**

La **persistencia en programación** se refiere a la capacidad de un sistema o aplicación para **almacenar y recuperar datos de manera duradera**, incluso después de que el programa haya terminado su ejecución. Es un concepto fundamental en el desarrollo de software, especialmente en aplicaciones que requieren conservar información a lo largo del tiempo.

------

### 📖**Tipos de Persistencia**

1. **Persistencia en Memoria (Volátil)**

   - Los datos se almacenan en la RAM mientras el programa está en ejecución.
   - Ejemplo: Variables, arreglos, estructuras de datos temporales.
   - **Desventaja:** Los datos se pierden cuando el programa se cierra.

2. **Persistencia en Archivos (No Volátil)**

   - Guarda los datos en archivos en el sistema de almacenamiento.

   - Formatos comunes: `.txt`, `.csv`, `.json`, `.xml`, `.log`.

   - Ejemplo en Python:

     ```
     rwith open("datos.txt", "w") as archivo:
         archivo.write("Hola, esto es un archivo de texto")
     ```

3. **Persistencia en Bases de Datos**

   - Usa sistemas de bases de datos para almacenar grandes volúmenes de información.

   - Puede ser **relacional** (SQL) o **NoSQL** (MongoDB, Firebase).

   - Ejemplo en SQL (MySQL):

     ```
     CREATE TABLE usuarios (
         id INT PRIMARY KEY AUTO_INCREMENT,
         nombre VARCHAR(50),
         email VARCHAR(100)
     );
     ```

4. **Persistencia en la Nube**

   - Almacenamiento de datos en servidores remotos accesibles por Internet.
   - Ejemplos: Google Firebase, AWS S3, Microsoft Azure.

5. **Persistencia en Caché**

   - Se almacenan datos temporalmente en memoria para mejorar el rendimiento.
   - Ejemplo: Redis, Memcached.

------

### 📖**Mecanismos de Persistencia**

✅ **Bases de Datos Relacionales (SQL)**

- MySQL, PostgreSQL, Oracle, SQL Server.
- Usa **tablas y relaciones** para organizar los datos.

✅ **Bases de Datos NoSQL**

- MongoDB, Firebase, CouchDB.
- Almacenan datos en formato **JSON o BSON**, sin estructuras fijas.

✅ **Archivos Locales**

- Archivos JSON, XML, CSV, binarios.

✅ **ORM (Object-Relational Mapping)**

- Herramientas como Hibernate (Java), SQLAlchemy (Python), TypeORM (JavaScript) permiten interactuar con bases de datos mediante objetos en lugar de SQL puro.

✅ **Almacenamiento en la Nube**

- Firebase, AWS S3, Google Cloud Storage.

✅ **Session Storage & Local Storage (Web)**

- Para persistencia en navegadores sin necesidad de base de datos.

- Ejemplo en JavaScript:

  ```
  localStorage.setItem("usuario", "Johlver");
  console.log(localStorage.getItem("usuario")); // "Johlver"
  ```

------

### 📖**Ejemplo de Persistencia con JSON en JavaScript**

```
// Crear objeto
const usuario = { nombre: "Johlver", edad: 25 };

// Convertir a JSON y guardar en localStorage
localStorage.setItem("usuario", JSON.stringify(usuario));

// Recuperar datos
const datosRecuperados = JSON.parse(localStorage.getItem("usuario"));
console.log(datosRecuperados); // { nombre: "Johlver", edad: 25 }
```

------

### 📖**Importancia de la Persistencia**

- Permite que los datos **se mantengan después de cerrar el programa**.
- Es clave en aplicaciones web, móviles y sistemas empresariales.
- Mejora la escalabilidad y accesibilidad de la información.
- Facilita la **integración con otras aplicaciones** y servicios.

### 📔Archivos en python

En Python, el manejo de archivos se realiza con la función `open()`, que permite leer, escribir, modificar y cerrar archivos. A continuación, te explicaré los **métodos** y **parámetros** más usados en la manipulación de archivos.

#### **📌 `open()` - Apertura de Archivos**

La función `open()` se usa para abrir un archivo y devuelve un objeto de tipo archivo.

#### **🔹 Sintaxis:**

```
archivo = open("nombre_del_archivo", "modo", encoding="utf-8")
```

- `"nombre_del_archivo"`: Nombre del archivo con su ruta (ejemplo: `"datos.txt"`).
- `"modo"`: Indica la acción que se realizará sobre el archivo.
- `encoding="utf-8"`: (Opcional) Especifica la codificación del archivo, recomendada para caracteres especiales.

------

#### **📜 Modos de Apertura de Archivos**

Los modos de apertura determinan qué operación se realizará sobre el archivo:

| Modo   | Acción                                                       |
| ------ | ------------------------------------------------------------ |
| `"r"`  | Modo **lectura** (por defecto). Da error si el archivo no existe. |
| `"w"`  | Modo **escritura**, sobrescribe el archivo si ya existe. Si no existe, lo crea. |
| `"a"`  | Modo **agregar** (append). Agrega texto al final sin sobrescribir el contenido existente. |
| `"x"`  | Modo **creación exclusiva**. Da error si el archivo ya existe. |
| `"r+"` | **Lectura y escritura**, sin borrar el contenido.            |
| `"w+"` | **Lectura y escritura**, pero sobrescribe el contenido.      |
| `"a+"` | **Lectura y escritura**, pero agrega datos al final.         |
| `"b"`  | Se usa junto con otros modos (`rb`, `wb`, `ab`) para archivos binarios. |

------

#### **📌 Métodos para el Manejo de Archivos**

Una vez que se abre un archivo, se pueden usar los siguientes métodos:

#### **📖 Lectura de Archivos**

##### 🔹 `read()` - Lee todo el contenido del archivo

```python
with open("archivo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)
```

📌 **Nota:** Si el archivo es muy grande, `read()` puede consumir mucha memoria.

##### 🔹 `readline()` - Lee una sola línea

```python
with open("archivo.txt", "r", encoding="utf-8") as archivo:
    primera_linea = archivo.readline()
    print(primera_linea)
```

📌 **Nota:** Cada llamada a `readline()` lee la siguiente línea.

##### 🔹 `readlines()` - Lee todas las líneas y las almacena en una lista

```python
with open("archivo.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    print(lineas)  # ['Primera línea\n', 'Segunda línea\n']
```

📌 **Nota:** Cada línea incluye el salto de línea `\n`.

------

#### **✍️ Escritura en Archivos**

##### 🔹 `write()` - Escribe una cadena en el archivo

```python
with open("archivo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola, este es un archivo de prueba.\n")
```

📌 **Nota:** Si el archivo existe, se sobrescribe.

##### 🔹 `writelines()` - Escribe una lista de líneas en el archivo

```python
lineas = ["Línea 1\n", "Línea 2\n", "Línea 3\n"]

with open("archivo.txt", "w", encoding="utf-8") as archivo:
    archivo.writelines(lineas)
```

📌 **Nota:** `writelines()` **no** añade automáticamente `\n`, hay que incluirlo en cada línea.

------

#### **📝 Agregar Texto sin Sobrescribir**

Si quieres **añadir contenido al final** del archivo sin eliminar lo que ya existe, usa el modo `"a"`:

```python
with open("archivo.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Esta línea se agrega al final.\n")
```

------

#### **🚀 Lectura y Escritura al Mismo Tiempo**

Si deseas **leer y escribir** en el mismo archivo, usa `"r+"`, `"w+"` o `"a+"`:

```python
with open("archivo.txt", "r+", encoding="utf-8") as archivo:
    contenido = archivo.read()  # Leer contenido existente
    archivo.write("\nNueva línea agregada.")  # Escribir sin borrar
```

------

#### **📌 Cerrar un Archivo con `close()`**

Es importante cerrar los archivos después de usarlos para evitar pérdida de datos.

```python
archivo = open("archivo.txt", "r", encoding="utf-8")
contenido = archivo.read()
archivo.close()
```

✅ **Recomendación:** Usa `with open()` en lugar de `close()`, ya que Python cierra el archivo automáticamente.

------

#### **📂 Ejemplo Completo: Gestión de Notas en un Archivo**

```python
def agregar_nota(nota):
    with open("notas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(nota + "\n")

def mostrar_notas():
    with open("notas.txt", "r", encoding="utf-8") as archivo:
        print("📄 Notas Guardadas:")
        print(archivo.read())

# Agregar notas
agregar_nota("Estudiar Python")
agregar_nota("Practicar archivos en Python")

# Mostrar notas almacenadas
mostrar_notas()
```

------

#### **🔹 Resumen**

| Método         | Descripción                                            |
| -------------- | ------------------------------------------------------ |
| `open()`       | Abre un archivo para lectura, escritura o ambos.       |
| `read()`       | Lee todo el contenido del archivo.                     |
| `readline()`   | Lee una línea del archivo.                             |
| `readlines()`  | Lee todas las líneas y las guarda en una lista.        |
| `write()`      | Escribe una cadena en el archivo (sobreescribe).       |
| `writelines()` | Escribe una lista de líneas en el archivo.             |
| `close()`      | Cierra el archivo (no es necesario con `with open()`). |

### 📔Persistencia con Archivos de texto

**Ejemplo práctico** que utiliza el manejo de archivos de texto en Python. Implementaremos un **gestor de tareas**, donde el usuario podrá:

✅ Agregar tareas
✅ Listar tareas
✅ Marcar tareas como completadas
✅ Eliminar tareas
✅ Guardar todas las tareas en un archivo de texto (`tareas.txt`)**

#### **📜 Código del Gestor de Tareas**

```python
import os

ARCHIVO_TAREAS = "tareas.txt"

# Función para inicializar el archivo de tareas
def inicializar_archivo():
    if not os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
            archivo.write("")

# Función para agregar una tarea
def agregar_tarea(tarea):
    with open(ARCHIVO_TAREAS, "a", encoding="utf-8") as archivo:
        archivo.write(f"{tarea} | Pendiente\n")
    print(f"✅ Tarea agregada: {tarea}")

# Función para listar todas las tareas
def listar_tareas():
    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
        tareas = archivo.readlines()
    
    if not tareas:
        print("📂 No hay tareas registradas.")
    else:
        print("\n📋 Lista de Tareas:")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea.strip()}")

# Función para marcar una tarea como completada
def completar_tarea(numero):
    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
        tareas = archivo.readlines()

    if 1 <= numero <= len(tareas):
        tareas[numero - 1] = tareas[numero - 1].replace("Pendiente", "Completada")
        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
            archivo.writelines(tareas)
        print(f"✅ Tarea {numero} marcada como completada.")
    else:
        print("❌ Número de tarea inválido.")

# Función para eliminar una tarea
def eliminar_tarea(numero):
    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
        tareas = archivo.readlines()

    if 1 <= numero <= len(tareas):
        tarea_eliminada = tareas.pop(numero - 1)
        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
            archivo.writelines(tareas)
        print(f"🗑️ Tarea eliminada: {tarea_eliminada.strip()}")
    else:
        print("❌ Número de tarea inválido.")

# Función principal con menú interactivo
def menu():
    inicializar_archivo()
    while True:
        print("\n📌 Menú de Gestor de Tareas")
        print("1️⃣ Agregar tarea")
        print("2️⃣ Listar tareas")
        print("3️⃣ Marcar tarea como completada")
        print("4️⃣ Eliminar tarea")
        print("5️⃣ Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            tarea = input("Descripción de la tarea: ")
            agregar_tarea(tarea)
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            listar_tareas()
            num = int(input("Número de la tarea a completar: "))
            completar_tarea(num)
        elif opcion == "4":
            listar_tareas()
            num = int(input("Número de la tarea a eliminar: "))
            eliminar_tarea(num)
        elif opcion == "5":
            print("👋 Saliendo del gestor de tareas...")
            break
        else:
            print("❌ Opción inválida. Inténtalo de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()

```

#### **🔍 Explicación del Código**

1. **`inicializar_archivo()`**
   - Crea el archivo `tareas.txt` si no existe.
2. **`agregar_tarea(tarea)`**
   - Añade una nueva tarea al archivo, marcándola como `Pendiente`.
3. **`listar_tareas()`**
   - Muestra todas las tareas guardadas en el archivo.
4. **`completar_tarea(numero)`**
   - Cambia el estado de una tarea de `Pendiente` a `Completada`.
5. **`eliminar_tarea(numero)`**
   - Borra una tarea específica del archivo.
6. **`menu()`**
   - Muestra un menú interactivo para gestionar las tareas.

### 📔Persistencia de datos CSV

#### **📌 Ejercicio: Gestión de Contactos**

Crea un programa en Python que permita:

1. **Agregar contactos** con nombre, teléfono y correo electrónico.
2. **Listar los contactos** guardados en el archivo `contactos.csv`.
3. **Buscar un contacto** por nombre.
4. **Eliminar un contacto** por nombre.

------

##### **📜 Código Base**

```python
import csv
import os

# Nombre del archivo CSV
ARCHIVO_CSV = "contactos.csv"

# Función para verificar si el archivo CSV existe, si no, lo crea con encabezados
def inicializar_archivo():
    if not os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Nombre", "Teléfono", "Email"])

# Función para agregar un contacto
def agregar_contacto(nombre, telefono, email):
    with open(ARCHIVO_CSV, mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nombre, telefono, email])
    print(f"✅ Contacto {nombre} agregado correctamente.")

# Función para listar contactos
def listar_contactos():
    with open(ARCHIVO_CSV, mode="r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        contactos = list(lector)

    if len(contactos) <= 1:
        print("📂 No hay contactos almacenados.")
    else:
        print("\n📜 Lista de contactos:")
        for i, contacto in enumerate(contactos[1:], start=1):  # Saltar encabezado
            print(f"{i}. {contacto[0]} - {contacto[1]} - {contacto[2]}")

# Función para buscar un contacto por nombre
def buscar_contacto(nombre):
    with open(ARCHIVO_CSV, mode="r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Saltar encabezado
        for contacto in lector:
            if contacto[0].lower() == nombre.lower():
                print(f"🔍 Contacto encontrado: {contacto[0]} - {contacto[1]} - {contacto[2]}")
                return
    print(f"❌ Contacto '{nombre}' no encontrado.")

# Función para eliminar un contacto por nombre
def eliminar_contacto(nombre):
    contactos_actualizados = []
    contacto_eliminado = False

    with open(ARCHIVO_CSV, mode="r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        contactos_actualizados.append(next(lector))  # Guardar encabezado

        for contacto in lector:
            if contacto[0].lower() == nombre.lower():
                contacto_eliminado = True
            else:
                contactos_actualizados.append(contacto)

    if contacto_eliminado:
        with open(ARCHIVO_CSV, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(contactos_actualizados)
        print(f"🗑️ Contacto '{nombre}' eliminado correctamente.")
    else:
        print(f"❌ Contacto '{nombre}' no encontrado.")

# Función principal para el menú interactivo
def menu():
    inicializar_archivo()
    while True:
        print("\n📞 Menú de Contactos")
        print("1️⃣ Agregar contacto")
        print("2️⃣ Listar contactos")
        print("3️⃣ Buscar contacto")
        print("4️⃣ Eliminar contacto")
        print("5️⃣ Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            agregar_contacto(nombre, telefono, email)
        elif opcion == "2":
            listar_contactos()
        elif opcion == "3":
            nombre = input("Ingresa el nombre a buscar: ")
            buscar_contacto(nombre)
        elif opcion == "4":
            nombre = input("Ingresa el nombre del contacto a eliminar: ")
            eliminar_contacto(nombre)
        elif opcion == "5":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida. Inténtalo de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
```

------

##### **💡 Explicación del Código**

1. 📂 **Crea un archivo CSV si no existe**, con encabezados (`Nombre`, `Teléfono`, `Email`).
2. ➕ **Agrega contactos** escribiéndolos en el archivo CSV.
3. 📄 **Lista los contactos** leyéndolos del archivo CSV.
4. 🔎 **Busca un contacto** comparando el nombre ingresado con los datos guardados.
5. ❌ **Elimina un contacto** reescribiendo el archivo sin el contacto seleccionado.
6. 🖥️ **Menú interactivo** que permite elegir entre las diferentes opciones.

## 📔Persistencia de datos JSON

Modulo corefiles.py

```python
import os
import json
from typing import Dict, List, Optional

def read_json(file_path: str) -> Dict:
    """Lee y retorna el contenido del archivo JSON"""
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def write_json(file_path: str, data: Dict) -> None:
    """Escribe datos en el archivo JSON"""
    with open(file_path, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def update_json(file_path: str, data: Dict, path: Optional[List[str]] = None) -> None:
    """
    Actualiza datos en el JSON, opcionalmente en una ruta específica
    Ejemplo: update_json('db.json', {'nuevo': 'dato'}, ['ruta', 'subruta'])
    """
    current_data = read_json(file_path)
    
    if not path:
        current_data.update(data)
    else:
        current = current_data
        for key in path[:-1]:
            current = current.setdefault(key, {})
        if path:
            current.setdefault(path[-1], {}).update(data)

    write_json(file_path, current_data)

def delete_json(file_path: str, path: List[str]) -> bool:
    """
    Elimina datos en la ruta especificada
    Retorna True si se eliminó exitosamente
    """
    data = read_json(file_path)
    current = data

    for key in path[:-1]:
        if key not in current:
            return False
        current = current[key]

    if path and path[-1] in current:
        del current[path[-1]]
        write_json(file_path, data)
        return True
    return False

def initialize_json(file_path: str, initial_structure: Dict) -> None:
    """
    Inicializa el archivo con una estructura base si no existe
    """
    if not os.path.isfile(file_path):
        write_json(file_path, initial_structure)
    else:
        current_data = read_json(file_path)
        for key, value in initial_structure.items():
            if key not in current_data:
                current_data[key] = value
        write_json(file_path, current_data)
```

main.py

```python
import corefiles as cf
import json

# Inicialización
DB_FILE = "database.json"

def menu_principal():
    while True:
        print("\n🎯 SISTEMA DE GESTIÓN ACADÉMICA")
        print("1. Gestionar Campers")
        print("2. Gestionar Rutas")
        print("3. Ver datos")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            menu_campers()
        elif opcion == "2":
            menu_rutas()
        elif opcion == "3":
            mostrar_datos()
        elif opcion == "4":
            print("¡Hasta luego! 👋")
            break
        else:
            print("❌ Opción inválida")

def menu_campers():
    while True:
        print("\n👥 GESTIÓN DE CAMPERS")
        print("1. Agregar camper")
        print("2. Editar camper")
        print("3. Eliminar camper")
        print("4. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            id_camper = input("ID del camper: ")
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            
            nuevo_camper = {
                id_camper: {
                    "nombre": nombre,
                    "edad": edad
                }
            }
            
            cf.update_json(DB_FILE, nuevo_camper, ["campers"])
            print("✅ Camper agregado exitosamente")
            
        elif opcion == "2":
            id_camper = input("ID del camper a editar: ")
            datos = cf.read_json(DB_FILE)
            
            if id_camper in datos.get("campers", {}):
                print("\nDatos actuales:")
                print(f"Nombre: {datos['campers'][id_camper]['nombre']}")
                print(f"Edad: {datos['campers'][id_camper]['edad']}")
                
                nombre = input("\nNuevo nombre (Enter para mantener actual): ")
                edad = input("Nueva edad (Enter para mantener actual): ")
                
                camper_actualizado = {}
                if nombre:
                    camper_actualizado["nombre"] = nombre
                else:
                    camper_actualizado["nombre"] = datos['campers'][id_camper]['nombre']
                    
                if edad:
                    camper_actualizado["edad"] = edad
                else:
                    camper_actualizado["edad"] = datos['campers'][id_camper]['edad']
                
                cf.update_json(DB_FILE, camper_actualizado, ["campers", id_camper])
                print("✅ Camper actualizado exitosamente")
            else:
                print("❌ Camper no encontrado")
            
        elif opcion == "3":
            id_camper = input("ID del camper a eliminar: ")
            cf.delete_json(DB_FILE, ["campers", id_camper])
            print("🗑️ Camper eliminado exitosamente")
            
        elif opcion == "4":
            break
        else:
            print("❌ Opción inválida")

def menu_rutas():
    while True:
        print("\n📚 GESTIÓN DE RUTAS")
        print("1. Crear nueva ruta")
        print("2. Editar ruta")
        print("3. Agregar nivel a ruta")
        print("4. Eliminar ruta")
        print("5. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            nombre_ruta = input("Nombre de la ruta: ")
            nueva_ruta = {
                nombre_ruta: {
                    "nivel1": {},
                    "nivel2": {},
                    "nivel3": {}
                }
            }
            cf.update_json(DB_FILE, nueva_ruta, ["rutas"])
            print("✅ Ruta creada exitosamente")
            
        elif opcion == "2":
            nombre_ruta = input("Nombre de la ruta a editar: ")
            datos = cf.read_json(DB_FILE)
            
            if nombre_ruta in datos.get("rutas", {}):
                nivel = input("Nivel a editar (nivel1/nivel2/nivel3): ")
                
                if nivel in datos["rutas"][nombre_ruta]:
                    print("\nDatos actuales:")
                    nivel_actual = datos["rutas"][nombre_ruta][nivel]
                    if "trainer" in nivel_actual:
                        print(f"Trainer actual: {nivel_actual['trainer']}")
                    
                    nuevo_trainer = input("\nNuevo trainer (Enter para mantener actual): ")
                    
                    if nuevo_trainer:
                        info_nivel = {
                            "trainer": nuevo_trainer,
                            "estudiantes": nivel_actual.get("estudiantes", {})
                        }
                        cf.update_json(DB_FILE, info_nivel, ["rutas", nombre_ruta, nivel])
                        print("✅ Ruta actualizada exitosamente")
                else:
                    print("❌ Nivel no encontrado")
            else:
                print("❌ Ruta no encontrada")
            
        elif opcion == "3":
            ruta = input("Nombre de la ruta: ")
            nivel = input("Nivel (nivel1/nivel2/nivel3): ")
            trainer = input("Nombre del trainer: ")
            
            info_nivel = {
                "trainer": trainer,
                "estudiantes": {}
            }
            
            cf.update_json(DB_FILE, info_nivel, ["rutas", ruta, nivel])
            print("✅ Nivel agregado exitosamente")
            
        elif opcion == "4":
            ruta = input("Nombre de la ruta a eliminar: ")
            cf.delete_json(DB_FILE, ["rutas", ruta])
            print("🗑️ Ruta eliminada exitosamente")
            
        elif opcion == "5":
            break
        else:
            print("❌ Opción inválida")

def mostrar_datos():
    datos = cf.read_json(DB_FILE)
    print("\n📊 DATOS ACTUALES:")
    print(json.dumps(datos, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    estructura_inicial = {
        "campers": {},
        "rutas": {}
    }
    cf.initialize_json(DB_FILE, estructura_inicial)
    menu_principal()
```

### **1️⃣ `read_json(file_path: str) -> Dict`**

🔹 **Lee el archivo JSON y retorna su contenido como un diccionario**.
🔹 Si el archivo no existe, devuelve `{}` (un diccionario vacío).

```
def read_json(file_path: str) -> Dict:
    """Lee y retorna el contenido del archivo JSON"""
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
```

✅ **Ejemplo de uso**:

```
data = read_json("datos.json")
print(data)
```

Si `datos.json` contiene:

```
{
    "nombre": "Juan",
    "edad": 25
}
```

Salida:

```
{'nombre': 'Juan', 'edad': 25}
```

------

### **2️⃣ `write_json(file_path: str, data: Dict) -> None`**

🔹 **Escribe un diccionario en un archivo JSON**, sobrescribiendo el contenido.

```
def write_json(file_path: str, data: Dict) -> None:
    """Escribe datos en el archivo JSON"""
    with open(file_path, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4)
```

✅ **Ejemplo de uso**:

```
write_json("datos.json", {"usuario": "Pedro", "edad": 30})
```

Esto generará un archivo `datos.json` con:

```
{
    "usuario": "Pedro",
    "edad": 30
}
```

------

### **3️⃣ `update_json(file_path: str, data: Dict, path: Optional[List[str]] = None) -> None`**

🔹 **Actualiza datos dentro del JSON**, ya sea globalmente o en una ruta específica.
🔹 Si `path` es `None`, actualiza la raíz.
🔹 Si `path` tiene una lista de claves, actualiza solo esa parte.

```
def update_json(file_path: str, data: Dict, path: Optional[List[str]] = None) -> None:
    """
    Actualiza datos en el JSON, opcionalmente en una ruta específica
    Ejemplo: update_json('db.json', {'nuevo': 'dato'}, ['ruta', 'subruta'])
    """
    current_data = read_json(file_path)
    
    if not path:
        current_data.update(data)
    else:
        current = current_data
        for key in path[:-1]:
            current = current.setdefault(key, {})
        if path:
            current.setdefault(path[-1], {}).update(data)

    write_json(file_path, current_data)
```

✅ **Ejemplo 1 (Actualizar la raíz del JSON)**:

```
update_json("datos.json", {"telefono": "123456789"})
```

Si `datos.json` tenía:

```
{
    "usuario": "Pedro",
    "edad": 30
}
```

Ahora tendrá:

```
{
    "usuario": "Pedro",
    "edad": 30,
    "telefono": "123456789"
}
```

✅ **Ejemplo 2 (Actualizar un valor dentro de una estructura anidada)**:

```
update_json("datos.json", {"ciudad": "Bogotá"}, ["direccion"])
```

Si `datos.json` era:

```
{
    "usuario": "Pedro",
    "direccion": {}
}
```

Después de la actualización:

```
{
    "usuario": "Pedro",
    "direccion": {
        "ciudad": "Bogotá"
    }
}
```

------

### **4️⃣ `delete_json(file_path: str, path: List[str]) -> bool`**

🔹 **Elimina datos dentro del JSON en una ruta específica**.
🔹 Retorna `True` si se eliminó correctamente, `False` si la clave no existe.

```
def delete_json(file_path: str, path: List[str]) -> bool:
    """
    Elimina datos en la ruta especificada
    Retorna True si se eliminó exitosamente
    """
    data = read_json(file_path)
    current = data

    for key in path[:-1]:
        if key not in current:
            return False
        current = current[key]

    if path and path[-1] in current:
        del current[path[-1]]
        write_json(file_path, data)
        return True
    return False
```

✅ **Ejemplo de uso**:

```
delete_json("datos.json", ["direccion", "ciudad"])
```

Si `datos.json` tenía:

```
{
    "usuario": "Pedro",
    "direccion": {
        "ciudad": "Bogotá",
        "codigo_postal": "110111"
    }
}
```

Después de la eliminación:

```
{
    "usuario": "Pedro",
    "direccion": {
        "codigo_postal": "110111"
    }
}
```

Si la clave no existe, la función devuelve `False`.

------

### **5️⃣ `initialize_json(file_path: str, initial_structure: Dict) -> None`**

🔹 **Crea un archivo JSON con una estructura inicial si no existe**.
🔹 Si ya existe, verifica si faltan claves y las agrega sin modificar los datos existentes.

```
def initialize_json(file_path: str, initial_structure: Dict) -> None:
    """
    Inicializa el archivo con una estructura base si no existe
    """
    if not os.path.isfile(file_path):
        write_json(file_path, initial_structure)
    else:
        current_data = read_json(file_path)
        for key, value in initial_structure.items():
            if key not in current_data:
                current_data[key] = value
        write_json(file_path, current_data)
```

✅ **Ejemplo de uso**:

```
initialize_json("datos.json", {"usuarios": {}, "config": {"modo": "oscuro"}})
```

Si `datos.json` no existe, se crea con:

```
{
    "usuarios": {},
    "config": {
        "modo": "oscuro"
    }
}
```

Si `datos.json` ya existía con:

```
{
    "usuarios": {
        "Juan": {"edad": 25}
    }
}
```

Después de `initialize_json()`, se actualizará a:

```
{
    "usuarios": {
        "Juan": {"edad": 25}
    },
    "config": {
        "modo": "oscuro"
    }
}
```

🔹 La clave `"usuarios"` no se modifica porque ya existía.
🔹 Se agrega `"config"` porque no estaba presente.

------

## **📌 Resumen del Código**

| **Función**                                     | **Descripción**                                          |
| ----------------------------------------------- | -------------------------------------------------------- |
| `read_json(file_path)`                          | Lee un JSON y lo retorna como diccionario.               |
| `write_json(file_path, data)`                   | Escribe datos en un JSON, sobrescribiéndolo.             |
| `update_json(file_path, data, path)`            | Actualiza datos en una ruta específica del JSON.         |
| `delete_json(file_path, path)`                  | Elimina datos en una ruta específica del JSON.           |
| `initialize_json(file_path, initial_structure)` | Inicializa un JSON con una estructura base si no existe. |
