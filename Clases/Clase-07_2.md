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
### Clase 7b - Decoradores y  programación funcional

![](../Imgs/Pasted%20image%2020261101154909.png)
---
#  Que es un decorador

Un **decorador** es, en palabras simples, **una función que “envuelve” a otra función para agregarle un comportamiento extra**, sin modificar el código de la función original.

Se usa con la sintaxis `@nombre_decorador` encima de una función:

```python
@medir_tiempo
def mi_funcion():
    ...
```

Eso es equivalente a:

```python
mi_funcion = medir_tiempo(mi_funcion)
```

En resumen: **un decorador es una capa reutilizable que se pone alrededor de una función para agregarle una funcionalidad, sin tocar el algoritmo que está dentro.**
## `@cache` : guardo los resultados parciales en memoria 
```python
from functools import cache

@cache
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(40))

print(fibonacci(4))
```

## `@timeit`: caclula el tiempo de ejecucion

```python
import time
from functools import wraps
def timeit(func):
    @wraps(func) # Preserva el nombre y docstring de la función original
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter() # Usa perf_counter para mayor precisión
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"La función '{func.__name__}' tardó {elapsed_time:.4f} segundos")
        return result
    return wrapper
    
    
@timeit
def calcular_suma(n):
    """Simula un cálculo pesado."""
    return sum(range(n))

# Al llamar a la función, el decorador se ejecuta automáticamente
calcular_suma(1000000)
```

# Programacion funcional:
