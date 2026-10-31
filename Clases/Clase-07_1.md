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


## `subprocess` divide y triunfaras

___


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
