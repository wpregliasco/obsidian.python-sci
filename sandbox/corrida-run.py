#!/usr/bin/env python3

import subprocess
import sys

# Encabezado de la tabla
print("n\tCuadrado")
print("-"*20)

# Campaña de corridas
for n in range(11):

    # Ejecutar el programa de cálculo
    proceso = subprocess.run(
        [sys.executable, "./cuadrado.py", str(n)],
        capture_output=True,
        text=True,
        check=False,
    )

    # Recuperar el resultado
    resultado = float(proceso.stdout)

    # Mostrar resultados
    print(f"{n}\t{resultado}")