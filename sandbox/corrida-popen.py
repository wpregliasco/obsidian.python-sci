#!/usr/bin/env python3

import subprocess
import sys

# Encabezado de la tabla
print("n\tCuadrado")
print("-" * 20)

# Campaña de corridas
for n in range(11):

    # Ejecutar el programa de cálculo
    proceso = subprocess.Popen(
        [sys.executable, "./cuadrado.py", str(n)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # Recuperar la salida del proceso
    stdout, stderr = proceso.communicate()

    # Recuperar el resultado
    resultado = float(stdout)

    # Mostrar resultados
    print(f"{n}\t{resultado}")