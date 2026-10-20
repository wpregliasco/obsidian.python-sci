---
theme: gaia
publish: "true"
---
# Python Científico
## de la ecuación al programa
### Clase 5b - Git

![bg right:60%](Imgs/Clase-05_2.png)

---

## Configurar el sistema

<style scoped> section { font-size: 50px; } </style>

```bash
git config --global user.name "Nombre Apellido" 
git config --global user.email email@domain.com 
git config --global init.defaultBranch main
```

---

## Repositorios nuevos

- **Existente en Gitlab** No crear un directorio del proyecto.  
    Desde la raíz ejecutar  
    `git clone git@gitlab.com:wpregliasco/test.git`  
    y se descarga el contenido a un directorio local
    
- **Existente en la computadora**
    
    ```
    cd existing_folder
    git init <-b main>
    git remote add origin git@gitlab.com:wpregliasco/test.git
    git add .
    git commit -m "Initial commit"
    git push -u origin main
    ```