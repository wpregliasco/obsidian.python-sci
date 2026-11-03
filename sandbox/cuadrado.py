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