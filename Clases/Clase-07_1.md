---
theme: gaia
publish: "true"
jupyter:
  jupytext:
    cell_metadata_filter: -all
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.19.5
  kernelspec:
    display_name: Python (.venv)
    language: python
    name: jupymd-.venv-2a5df0dee3
---
# Python Científico
## de la ecuación al programa
### Clase 71 - Un monton de nada
![[Pasted image 20261027105344.png|300]]

---
# Bilbliotecas amigas....

## ¿Qué es pathlib?

`pathlib` permite representar y manipular rutas del sistema de archivos mediante objetos Python. Hace que el manejo de los directorios sea **identico** en Windows y en Linux!

```python
from pathlib import Path

ruta = Path.cwd()
print(ruta)

base = Path.home()
proyecto = base / "Python" / "Experimentos"
archivo = proyecto / "mediciones.csv"
print(archivo)
```

Tiene funciones utilitarias como:

```python
from pathlib import Path

ruta = Path("datos/mediciones.csv")

print(ruta.exists())   # Does it exist?
print(ruta.is_file())  # Is it a file?
print(ruta.is_dir())   # Is it a directory?
print(ruta.name)       # File name
print(ruta.stem)       # Name without extension
print(ruta.suffix)     # Extension
```

e  incorpora el `glob`

```python
data = Path.home()

for archivo in data.glob(".ba*"):
    print(archivo)
```




- pathlib
        - subprocess
        - datetime
1. Decoradores >>>>>>>>>>>>>>>>>>>>>>>>> 10/11 martes
    - Bibliotecas amigas
        - pathlib
        - subprocess
        - datetime
        - loguru
    - cache
    - timeit
    - dataclass
    - property
    - beartype
    - programación funcional
# Limpiando el código

Limpiar y reformatear el código mejora su legibilidad, facilita el mantenimiento y ayuda a detectar errores antes de que se conviertan en problemas. Mantener un estilo consistente reduce el ruido en las revisiones y permite concentrarse en la lógica y el contenido del programa, en lugar de en detalles de formato.

Herramientas como **Ruff** y **Black** automatizan estas tareas y ayudan a producir código más claro, consistente y fácil de compartir.
## Ruff

Analizar el código permite detectar errores potenciales, eliminar elementos innecesarios y mantener buenas prácticas de programación. Automatizar estas revisiones mejora la calidad y la confiabilidad del código.

- Detecta errores potenciales y malas prácticas.
- Identifica `imports` y variables sin usar.
- Aplica correcciones automática.    
- Verifica convenciones y reglas de estilo.

Antes:
```
import os
import sys

def calcular():
    resultado= 10+ 20
    mensaje = "Hola"
    return resultado

print(calcular( ) ) 
```

Después:
```python
def calcular():
	resultado = 10 + 20
	mensaje = "Hola"
	return resultado


print(calcular())
```
## Black

Reformatear el código mejora su legibilidad y mantiene un estilo consistente en todo el proyecto. Automatizar el formato facilita el mantenimiento, la revisión y el trabajo colaborativo.

- Reformatea automáticamente el código.    
- Unifica espacios, indentación y saltos de línea.    
- Mantiene un estilo consistente en todo el proyecto.    
- Facilita la lectura, revisión y mantenimiento del código.

Antes:
```python
def calcular_total(precio,cantidad,descuento=0):
    total=precio*cantidad
    if descuento>0:
        total=total-(total*descuento)
    return total
```

Después:
```python
def calcular_total(precio, cantidad, descuento=0):
	total = precio * cantidad
	if descuento > 0:
		total = total - (total * descuento)
	return total
```

En resumen: 
- **Ruff** revisa el código para detectar problemas; 
- **Black** normaliza su formato sin cambiar la lógica del programa.

# Artificial Intelligence

## Generar código: 

Un buen **prompt** es todo:

```
Implementá en Python una función estimate_pi(n, seed=None) que estime pi mediante el siguiente método:

Generá puntos uniformes en el cuadrado [-1, 1] × [-1, 1].
Contá los puntos que cumplen x² + y² <= 1. 
Devolvé la estimación de pi. 
Usá NumPy. 
Permití fijar una semilla para reproducir los resultados. 
Incluí un ejemplo de uso y explicá el método. 
No agregues bibliotecas innecesarias.
```

Devolverá  algo así:

```python
import numpy as np

def estimate_pi(n, seed=None):
    """Estimate pi using the Monte Carlo method."""
    rng = np.random.default_rng(seed)

    x = rng.uniform(-1, 1, n)
    y = rng.uniform(-1, 1, n)

    inside = x**2 + y**2 <= 1

    return 4 * np.mean(inside)


if __name__ == "__main__":
    estimate = estimate_pi(100_000, seed=42)
    print(f"Estimated pi: {estimate:.5f}")

```
## Corregir codigo:

Una ves mas, un buen  **prompt**  lo es todo!

Consideremos este código, el cual falla en su ejecución:
```python
def mean_value(data):`
    `total = 0`

    `for value in data:`
        `total += value`

    `return total / len(value)`


measurements = [2.1, 2.3, 2.0, 2.2]
print(mean_value(measurements))
```

Pidamos que lo resuelva:

```
Analizá este programa sin modificarlo inicialmente.

Identificá el error y explicá por qué ocurre.
Indicá qué concepto de Python está involucrado.
Proponé la corrección mínima.
Mostrá un caso de prueba normal y otro para una lista vacía.
Explicá qué decisión debería tomar el programa ante una lista vacía.
```

Devolverá  algo así:
```python
def mean_value(data):
    if not data:
        raise ValueError("No se puede calcular la media de una lista vacía")

    total = 0

    for value in data:
        total += value

    return total / len(data)


measurements = [2.1, 2.3, 2.0, 2.2]
print(mean_value(measurements))
```


## Cómo escribir buenos `prompts` técnicos, o al menos intentarlo

Un pedido útil no necesita ser largo, pero sí debe especificar el objetivo, las restricciones y el resultado esperado.

|   Pedido poco preciso   |                                     Pedido mejor definido                                     |
| :---------------------: | :-------------------------------------------------------------------------------------------: |
|   «Hacé un gráfico».    |       «Graficá los datos experimentales con barras de error y unidades en ambos ejes».        |
| «Optimizá este código». |             «Reducí el tiempo de ejecución sin cambiar los resultados numéricos».             |
|  «Arreglá este error».  | «Explicá la causa, proponé la corrección mínima y agregá una prueba que reproduzca el error». |
| «Hacé una simulación».  |        «Simulá un oscilador armónico y compará la solución numérica con la analítica».        |
## Criterios para el uso responsable de la IA

En computación científica hay una distinción esencial entre que un programa se ejecute correctamente y que sus resultados sean válidos.

- **No confiar en la apariencia:** un código elegante puede implementar mal una ecuación.
- **Verificar las fuentes:** comprobar las funciones y la documentación de las bibliotecas.
- **Probar los casos límite:** datos vacíos, valores extremos, unidades incompatibles y posibles errores numéricos.    
- **Comprender antes de entregar:** poder explicar el algoritmo, sus hipótesis y sus limitaciones.
---
