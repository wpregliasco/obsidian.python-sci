#!/usr/bin/env python3

import argparse
import math


def main():

    parser = argparse.ArgumentParser(
        description="Calcula el radio de una esfera a partir de su volumen.",
        epilog="El volumen se expresa en cm³ y el radio en cm."
    )

    parser.add_argument(
        "-v", "--volumen",
        type=float,
        required=True,
        help="Volumen de la esfera en cm³"
    )

    args = parser.parse_args()

    if args.volumen <= 0:
        parser.error("El volumen debe ser positivo.")

    radio = (3 * args.volumen / (4 * math.pi)) ** (1 / 3)

    print(f"Volumen: {args.volumen} cm³")
    print(f"Radio: {radio:.4f} cm")


if __name__ == "__main__":
    main()

