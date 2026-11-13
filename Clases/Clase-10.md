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
### Clase 10 - Y ahora que hacemos?

![](../Imgs/Pasted%20image%2020261112082910.png)

Antes de empezar un proyecto de Python científico  conviene definir algunas cuestiones que van más allá de escribir el código. La idea es que el proyecto sea reproducible, mantenible, fácil de ejecutar y sencillo de compartir.
# 1. Definición del problema científico: Qué vamos a resolver?

Estas son las primeras preguntas que deberían estar respondidas.

- ¿Cuál es el problema físico, matemático o científico que quiero resolver?
- ¿Cuál es el objetivo concreto del programa?
- ¿Qué datos de entrada necesita?
- ¿Qué resultados debe producir?
- ¿Cuáles son las hipótesis y aproximaciones utilizadas?  
- ¿Cómo voy a verificar que los resultados son correctos?
- ¿Existe una solución analítica, un resultado conocido o un experimento de referencia?

# 2. Definición del entorno de desarrollo: Con qué vamos a trabajar?

Antes de iniciar el repositorio, conviene establecer:

- ¿Qué versión de Python vamos a utilizar?
- ¿Qué gestor de entornos y dependencias usaremos?
- ¿Qué bibliotecas científicas necesitamos?    

La idea es que el entorno sea explícito y reproducible, y que no dependa de las bibliotecas instaladas globalmente en la computadora.

# 3. Organización del proyecto: Cómo vamos a estructurar el código?

Preguntas importantes:

- ¿El proyecto será un único programa o tendrá varios módulos?
- ¿Conviene dividirlo en subproyectos?
- ¿Qué archivos serán ejecutables?
- ¿Qué funciones y clases serán reutilizables?
- ¿Dónde se almacenarán los datos?
- ¿Dónde se guardarán los resultados?
- ¿Qué archivos deben estar versionados en Git?

# 4. Control de versiones con Git: Cómo vamos a registrar los cambios?

Antes de comenzar, hay que definir algunas reglas.

- ¿El repositorio será público o privado?
- ¿Cuál será el nombre del repositorio?
- ¿Qué archivos vamos a ignorar?
- ¿Cómo vamos a nombrar los commits?
- ¿Trabajaremos sobre `main` o usaremos ramas?
- ¿Cómo vamos a gestionar las versiones del programa?
- ¿Qué información no debe subirse a GitHub?

# 5. Reproducibilidad científica

Cómo garantizar resultados confiables

Este es uno de los aspectos más importantes de un proyecto científico.

Preguntas:

- ¿El programa produce los mismos resultados con las mismas entradas?  
- ¿Se utilizan números aleatorios?
- ¿Se puede controlar la semilla del generador aleatorio?
- ¿Se registran los parámetros de cada corrida?
- ¿Se guardan las versiones de las bibliotecas?
- ¿Se conservan los datos originales?
- ¿Se documentan las unidades?
- ¿Se puede reconstruir una campaña de simulaciones?

# 6. Pruebas y validación

Cómo sabemos que funciona

Antes de escribir el programa, deberíamos definir:

- ¿Qué funciones necesitan pruebas?
- ¿Qué resultados conocidos podemos usar?
- ¿Qué tolerancia numérica es aceptable?
- ¿Qué sucede ante entradas incorrectas?
- ¿Cómo detectamos errores de unidades?
- ¿Cómo verificamos los límites del algoritmo?

# 7. Documentación

Cómo se utiliza el proyecto

Antes de empezar, deberíamos responder:

- ¿Qué información tendrá el `README.md`?
- ¿Cómo se instala el proyecto?
- ¿Cómo se ejecuta?
- ¿Qué argumentos acepta?
- ¿Qué resultados genera?
- ¿Qué metodología científica utiliza?
- ¿Quiénes son los autores?
- ¿Qué licencia tendrá?

El `README.md` debería permitir que una persona que nunca vio el proyecto pueda entenderlo y ejecutarlo.

Una estructura sugerida:

1. Nombre del proyecto.
2. Descripción.
3. Objetivo científico.
4. Instalación.
5. Uso.
6. Ejemplo de ejecución.
7. Metodología.
8. Validación.
9. Autores.
10. Licencia.
---