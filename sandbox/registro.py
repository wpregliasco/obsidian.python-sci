from loguru import logger
import numpy as np
import sys


def main() -> int:
    logger.remove()  # evitar el handler stderr por defecto si no lo querés
    logger.add(
        "experimento.log",
        level="DEBUG",
        rotation="10 MB",
        retention="7 days",
        compression="zip",
        encoding="utf-8",
        enqueue=True,
    )
    logger.add(sys.stdout, level="INFO", colorize=True)

    mediciones = np.array([10.2, 10.4, 10.1, 10.3, 10.5])
    logger.debug("Datos: {}", mediciones)
    logger.info("Cantidad de mediciones: {}", mediciones.size)
    logger.success("Promedio calculado: {:.3f}", mediciones.mean())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
