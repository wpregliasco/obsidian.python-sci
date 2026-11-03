import time
from functools import wraps

def timeit(func):
    @wraps(func) # Preserva el nombre y docstring de la función original
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter() # Usa perf_counter para mayor precisión
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"La función '{func.__name__}' tardó {elapsed_time:.4f} segundos")
        return result
    return wrapper

@timeit
def calcular_suma(n):
    """Simula un cálculo pesado."""
    return sum(range(n))

# Al llamar a la función, el decorador se ejecuta automáticamente
calcular_suma(1000000)



