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