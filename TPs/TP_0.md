---
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
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Prueba de Jupyter en Obsidian

```python
for i in range(10):
	print(f"Hola Willy {i:02d}")
```

```python
from matplotlib import pyplot as plt
import numpy as np

N = 360
x = np.linspace(0.0001,6*np.pi,N)
y = sin(x)/x

plt.plot(x,y,'r-')
plt.grid()
plt.show()
```

Esto es la ecuación:
$$ y = \frac{\sin x}{x}  \ \ \ \ \ x \in [0,6\pi]
$$

```python
plt.plot(x,y**2,'r-')
plt.grid()
plt.show()
```
