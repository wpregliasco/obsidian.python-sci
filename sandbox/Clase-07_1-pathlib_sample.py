#############################################

from pathlib import Path

ruta = Path.cwd()
print(ruta)

base = Path.home()
proyecto = base / "Python" / "Experimentos"
archivo = proyecto / "mediciones.csv"
print(archivo)

##############################################

from pathlib import Path

ruta = Path("datos/mediciones.csv")

print(f"{ruta.resolve() = }")  # Absolute path
print(f"{ruta.exists() = }")   # Does it exist?
print(f"{ruta.is_file() = }")  # Is it a file?
print(f"{ruta.is_dir() = }")   # Is it a directory?
print(f"{ruta.name = }")       # File name
print(f"{ruta.stem = }")       # Name without extension
print(f"{ruta.suffix = }")     # Extension

directorio = Path("resultados")  # Crea todos los directorios
directorio.mkdir(parents=True, exist_ok=True)

print(f"{directorio.resolve() = }")  # Absolute path


###############################################

from pathlib import Path

data = Path.home()

for archivo in data.glob(".ba*"):
    print(archivo)