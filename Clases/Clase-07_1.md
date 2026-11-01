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
![](../Imgs/Pasted%20image%2020261031170445.png)

---
# Bilbliotecas amigas....

## `pathlib` todos los caminos conducen a Roma

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
from pathlib import Path

data = Path.home()

for archivo in data.glob(".ba*"):
    print(archivo)
```

##  `argparse` pasando argumentos

```python
#!/usr/bin/env python3

import argparse


def main():

    parser = argparse.ArgumentParser(
        description="Simulador de una esfera misteriosa.",
        epilog="Ningúna pariticula ha sido lastimada durante esta simulación."
    )

    # Radio de la esfera
    parser.add_argument(
        "-r", "--radio",
        type=float,
        default=1,
        help="Radio de la esfera en cm (por defecto: 1 cm)"
    )

    # Cantidad de partículas
    parser.add_argument(
        "-p", "--particulas",
        type=int,
        default=10000,
        help="Cantidad de partículas exploradoras (por defecto: 10000)"
    )

    args = parser.parse_args()

    print(f"Radio de la esfera: {args.radio} cm")
    print(f"Partículas enviadas: {args.particulas}")

if __name__ == "__main__":
    main()

```

## `datetime` el timpo es dinero...

Trabajar con fechas, horas, intervalos temporales y marcas de tiempo o `timestamps` siempre ha sido algo engorroso . Sin embargo es especialmente útil para organizar mediciones experimentales, registrar adquisiciones y analizar series temporales.

`datetime` forma parte de la biblioteca estándar de Python. No requiere instalación.

```python
from datetime import datetime

ahora = datetime.now()
print(ahora)

experimento = datetime(2026, 10, 31, 14, 30, 0)
print(experimento)

print(ahora-experimento)

```

```python
from datetime import datetime, timedelta

inicio = datetime.now()

# Simulate an experiment duration
duracion = timedelta(hours=2, minutes=30)

final = inicio + duracion

print(f"Start: {inicio}")
print(f"End:   {final}")

```

### Timestamp y Unix Time 

En computación científica es muy habitual representar fechas y horas mediante un número en lugar de utilizar una cadena de texto.

Esta representación se conoce como Unix Timestamp o Unix Time.y se define como la cantidad de segundos transcurridos desde el **1 de enero de 1970 a las 00:00:00 UTC**, conocido como Unix Epoch.

```python
from datetime import datetime

ahora = datetime.now()
timestamp = ahora.timestamp()

print(ahora)
print(timestamp)

timestamp = 1793458200
fecha = datetime.fromtimestamp(timestamp)

print(timestamp)
print(fecha)
```
## `subprocess` divide y triunfaras

`subprocess` es una biblioteca de Python que permite ejecutar programas y comandos del sistema operativo desde un script. La idea central es que Python **no tiene** que hacer todo por sí mismo: puede coordinar otros programas.

Sumpongamos que tenemos  el programa 

```python
import argparse

parser = argparse.ArgumentParser(
    description="Calcula el cuadrado de un número"
)

parser.add_argument(
    "n",
    type=float,
    help="Número de entrada"
)

args = parser.parse_args()

resultado = args.n**2

print(resultado)
```

Puedo ejecutar un programa en python que llame a ese programa  y su salida sea capturada....

```python
#!/usr/bin/env python3

import subprocess
import sys

# Encabezado de la tabla
print("   n     n²")
print("-------------")

# Campaña de corridas
for n in range(11):

    # Ejecutar el programa de cálculo
    proceso = subprocess.run(
        [sys.executable, "cuadrado.py", str(n)],
        capture_output=True,
        text=True
    )

    # Recuperar el resultado
    resultado = float(proceso.stdout)

    # Mostrar resultados
    print(f"{n:4d}   {resultado:6.1f}")
```

Esto ejecuta los procesos secuencialmente, es decir que espera que termine uno para inicial otro.

Si queremos que esto no ocurra se usoa `subprocess.Popen`
```python
#!/usr/bin/env python3

import subprocess
import sys

procesos = []

# Lanzar todas las corridas
for n in range(11):

    proceso = subprocess.Popen(
        [sys.executable, "cuadrado.py", str(n)],
        stdout=subprocess.PIPE,
        text=True
    )

    procesos.append((n, proceso))


# Esperar los resultados
print("   n     n²")
print("-------------")

for n, proceso in procesos:

    resultado = float(proceso.communicate()[0])

    print(f"{n:4d}   {resultado:6.1f}")

```

## `loguru` Everything Counts

Permite:
- Registrar información sobre el funcionamiento del programa.
- Identificar advertencias y errores.
- Guardar automáticamente los registros en archivos.
- Incorporar fecha y hora a cada mensaje.
- Rotar archivos de registro cuando alcanzan cierto tamaño.
- Registrar excepciones con información sobre dónde ocurrió el error.
- Facilitar el diagnóstico de programas que se ejecutan durante mucho tiempo.

```python
#!/usr/bin/env python3
from loguru import logger
import numpy as np

logger.add(
    "experimento.log",
    #level="WARNING"
    #rotation="10 MB",
    #retention="7 days",
    #compression="zip"
)

logger.info("Comenzando el programa")

mediciones = np.array([10.2, 10.4, 10.1, 10.3, 10.5])

logger.info("Cantidad de mediciones: {}", len(mediciones))

promedio = np.mean(mediciones)

logger.success("Promedio calculado: {:.3f}", promedio)

print(f"Promedio = {promedio:.3f}")
```
---
