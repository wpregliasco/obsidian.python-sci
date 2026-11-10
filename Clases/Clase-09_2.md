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
### Clase 9b - Un poco de plomería, `piping` y `redirection`

![[Pasted image 20261110131802.png]]---

# Que es?

Cuando ejecutamos un programa Python desde una terminal, existen tres canales de comunicación fundamentales entre el programa y el entorno de ejecución:

- `stdin` (Standard Input): entrada estándar.
- `stdout` (Standard Output): salida estándar.
- `stderr` (Standard Error): salida de errores.

En Unix/Linux (también en Windows) estos canales se identifican mediante descriptores de archivo:

|Canal|Descriptor|Función|
|---|---|---|
|`stdin`|0|Recibir datos|
|`stdout`|1|Enviar resultados|
|`stderr`|2|Enviar mensajes de error|

# Un ejemplo

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def main():

    # Leer desde la entrada estándar
    linea = sys.stdin.readline()

    try:
        x = float(linea)

    except ValueError:
        print("Error: entrada no numérica",
              file=sys.stderr)
        sys.exit(1)

    # Calcular el cuadrado
    y = x**2

    # Enviar el resultado a stdout
    print(y, file=sys.stdout, flush=True)


if __name__ == "__main__":
    main()
```

## Resumen de operadores

Tabla de referencia para Unix/Linux y Windows CMD

|Operador|Función|
|---|---|
|`>`|Redirige stdout, sobrescribe|
|`>>`|Redirige stdout, agrega|
|`<`|Redirige stdin desde un archivo|
|`2>`|Redirige stderr|
|`2>>`|Agrega stderr|
|`2>&1`|Envía stderr al destino de stdout|
## Otro caso útil

```python

import io
import numpy as np

texto = '''
1
2
3
4
5
'''

datos = np.loadtxt(io.StringIO(texto))

print(datos)
print(datos**2)
```


---
