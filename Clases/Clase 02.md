---
theme: gaia
---
# Python Científico
## de la ecuación al programa
### Clase 2
![bg left:50% 100%](../Imgs/python_install.png)

- Instalar y usar Python local
- variables `string`
- scripts, modules and packages
- loops y estructuras de control

---

## Python nativo

La máquina suele venir con un Python instalado.    
Si hace falta instalarlo
```Bash
# Linux
sudo apt install python3
# Windows
winget install Python.Python.3.14
```

(acá cuento los scripts de python y los shebang)

__PROBLEMAS !!!__
- bibliotecas instaladas
- interacción entre bibliotecas
- conflictos con actualizaciones de python

---
## Entornos virtuales

|                | Linux                              | Windows                  |
| -------------- | ---------------------------------- | ------------------------ |
| Crear          | `python -m venv .venv`             |                          |
| Activar        | `.venv/bin/activate`               | `.venv\Scripts\activate` |
| Desactivar     | `deactivate`                       |                          |
| Nuevos Módulos | `python pip install <antigravity>` |                          |
| Correr         | `(my venv)python3 -m <myprog.py>`  |                          |
__PROBLEMAS !!!__
- Compartir entornos
- Solución 
 ```Python
python -m pip freeze > requirements.txt
cat requirements.txt
    novas==3.1.1.3
    numpy==1.9.2
    requests==2.7.0
    
 python -m pip install -r requirements.txt
 ```

__Anaconda__

---
## UV  style


|          | Linux                                              | Windows                                                                             |
| -------- | -------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Instalar | `curl -LsSf https://astral.sh/uv/install.sh \| sh` | powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \| iex" |
| Crear    | `uv init [--python 3.12]`                          |                                                                                     |
| Módulos  | `uv add <antigravity>`                             |                                                                                     |
| Correr   | `uv run <mydir>`                                   |                                                                                     |
```
.
├── pyproject.toml
├── README.md
├── .python-version
├── src
│   └── test
│      └── __init.py__
├── .venv
└── uv.lock
```


---
- Tipos de Variables
	- num
	- lista
	- tupla
	- string
	- type() isnumeric() conversiones
- Control de flujo
	- if / elif / else
	- Loops
		- for 
		- while
		- continue / break
		- enumerate
- Módulos para leer un csv o un archivo de texto
- Script


| `set`     | `dict`              |
| --------- | ------------------- |
| `{1,2,3}` | `{'x': 1, 'y': 22}` |
|           | `{key: value}`      |
strings



