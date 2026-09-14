# Herramientas de diff y merge para Git: delta, difftastic y mergiraf

Guía de instalación, configuración y flujo de trabajo para revisar diffs y resolver conflictos de merge, con foco en Python, Markdown e IPYNB.

---

## Resumen de roles

|Herramienta|Rol|Reemplaza a|
|---|---|---|
|**delta**|Pager de diff (colorizador rápido, línea por línea)|El pager default de Git|
|**difftastic**|Diff estructural (AST vía tree-sitter), ideal para Python|`git diff` cuando el diff de línea genera ruido (reindentación, reordenamiento)|
|**mergiraf**|Driver de _merge_ estructural — resuelve conflictos automáticamente cuando son solo aparentes|El algoritmo de merge default de Git (`ort`)|

Ninguna resuelve conflictos por sí sola excepto **mergiraf**. Delta y difftastic son de solo lectura.

---

## 1. Delta

### Instalación

```bash
cargo install git-delta
```

### Configuración (`~/.gitconfig`)

```ini
[core]
    pager = delta

[interactive]
    diffFilter = delta --color-only

[delta]
    navigate = true
    line-numbers = true
    syntax-theme = Monokai Extended
    side-by-side = false
```

Con esto, `git diff`, `git show`, `git log -p`, `git stash show -p` usan delta automáticamente (es un pager estándar, no necesita configuración extra en cada comando).

### En lazygit

```yaml
# ~/.config/lazygit/config.yml
git:
  pagers:
    - pager: delta --dark --paging=never --line-numbers
```

---

## 2. Difftastic

### Instalación

```bash
cargo install difftastic
```

### Configuración (`~/.gitconfig`)

Se deja como `difftool` explícito (no pisa `core.pager`), para elegir cuándo usarlo:

```ini
[diff]
    tool = difftastic

[difftool]
    prompt = false

[difftool "difftastic"]
    cmd = difft "$LOCAL" "$REMOTE"
```

Uso puntual:

```bash
git difftool                          # working tree vs HEAD
git difftool <hash1> <hash2> -- archivo.py
```

### En lazygit

Como pager alternable con la tecla `|` (difftastic necesita `externalDiffCommand`, no `pager`, porque requiere ver los archivos completos, no solo el diff de texto):

```yaml
git:
  pagers:
    - pager: delta --dark --paging=never --line-numbers
    - externalDiffCommand: difft --color=always
```

### Cuándo usar cada uno

- **delta**: diff cotidiano, rápido, todo lenguaje, Markdown.
- **difftastic**: Python cuando hay reindentación, refactors o reordenamiento de argumentos y el diff de línea genera ruido.
- **Markdown**: ninguno tiene parser estructural; ambos caen a diff de línea. Delta es preferible por el resaltado de palabras dentro de la línea.
- **`.ipynb`**: ninguno de los dos es adecuado (son JSON con outputs/metadata que generan ruido). Usar **nbdime** (`pip install nbdime`) con `.gitattributes`:
    
    ```
    *.ipynb diff=nbdime
    ```
    

---

## 3. Mergiraf

### Qué hace

Driver de **merge** (no de diff) que usa árboles de sintaxis (tree-sitter) para resolver automáticamente conflictos que son solo aparentes — por ejemplo, cuando una rama mueve una función de lugar y otra edita su contenido: Git los marca como conflicto (mismas líneas tocadas), mergiraf entiende que son cambios independientes y los combina. Solo deja como conflicto real los casos donde ambos lados tocaron literalmente lo mismo.

Para archivos/lenguajes no soportados, devuelve código de salida distinto de cero y Git cae automáticamente a su merge de texto normal — no rompe nada.

### Instalación

```bash
cargo install mergiraf
# alternativas: brew install mergiraf / conda install conda-forge::mergiraf
```

Verificar lenguajes soportados:

```bash
mergiraf languages
```

### Configuración (`~/.gitconfig`)

**No existe un comando de auto-registro** (`mergiraf register` no es válido en la versión actual). Se registra a mano:

```bash
git config --global merge.mergiraf.name mergiraf
git config --global merge.mergiraf.driver 'mergiraf merge --git %O %A %B -s %S -x %X -y %Y -p %P -l %L'
```

Equivalente editando el archivo directo:

```ini
[merge "mergiraf"]
    name = mergiraf
    driver = mergiraf merge --git %O %A %B -s %S -x %X -y %Y -p %P -l %L
```

### Activación por extensión (`.gitattributes`)

```
*.py merge=mergiraf
```

Se puede poner en el `.gitattributes` de cada repo (viaja con el proyecto, pero cada colaborador necesita tener mergiraf instalado y el driver registrado localmente) o en un `.gitattributes` global:

```bash
git config --global core.attributesfile ~/.gitattributes
```

### Comandos útiles

|Comando|Uso|
|---|---|
|`mergiraf languages`|Lista lenguajes soportados|
|`mergiraf review <archivo>`|Muestra qué decisiones tomó automáticamente el driver, para auditar|
|`mergiraf solve <archivo>`|Resuelve a mano un archivo que ya tiene marcadores de conflicto|

---

## 4. Configuración complementaria de conflictos

### Marcadores de 3 vías (`zdiff3`)

Por defecto Git muestra solo 2 bloques en un conflicto (tu versión / la otra). Con `zdiff3` se agrega el ancestro común, lo que permite ver qué cambió cada lado _respecto al original_ en vez de comparar a ciegas dos resultados finales:

```ini
[merge]
    conflictStyle = zdiff3
```

```
<<<<<<< HEAD (tu rama)
tu código
||||||| (ancestro común)
código original antes de ambos cambios
=======
código de la otra rama
>>>>>>> feature-x
```

### Mergetool visual para conflictos reales (Meld)

Mergiraf resuelve lo que puede automáticamente; lo que queda como conflicto real necesita resolución manual. **Meld** (GUI, 3 paneles) es la opción más cómoda visualmente:

```bash
sudo apt install meld
```

```ini
[merge]
    tool = meld

[mergetool "meld"]
    cmd = meld "$LOCAL" "$BASE" "$REMOTE" --output "$MERGED"
```

```bash
git mergetool   # navega TODOS los archivos en conflicto, uno por uno
```

Alternativa: lazygit tiene navegación y resolución de conflictos integrada en su panel de Files (atajos para elegir un lado, edición inline), sin salir de la terminal.

---

## 5. Secuencia de revisión ante un merge con conflictos

1. **Ver panorama general**
    
    ```bash
    git status
    ```
    
    o el panel de Files en lazygit (marca visualmente los archivos en conflicto).
    
2. **Dejar que mergiraf actúe primero** (automático si está bien configurado el `.gitattributes`) — muchos conflictos de Python desaparecen solos antes de llegar a este paso.
    
3. **Auditar lo que mergiraf resolvió** (recomendado, sobre todo al principio):
    
    ```bash
    mergiraf review archivo.py
    ```
    
4. **Para los conflictos reales que queden**, entender el contexto de cada lado si hace falta:
    
    ```bash
    git diff --ours     # cambios de tu rama vs ancestro común
    git diff --theirs   # cambios de la otra rama vs ancestro común
    git difftool <merge-base> HEAD -- archivo.py   # con difftastic, útil en Python
    ```
    
5. **Resolver**:
    
    - Archivos chicos: editar directo los marcadores `<<<<<<<` / `=======` / `>>>>>>>`.
    - Varios archivos o conflictos complejos: `git mergetool` (Meld) o el flujo integrado de lazygit.
6. **Confirmar y cerrar**:
    
    ```bash
    git add archivo.py
    git status            # debe quedar sin "unmerged paths"
    git commit            # si era un merge
    git rebase --continue # si era un rebase
    ```
    

### Tabla resumen

|Paso|Herramienta|
|---|---|
|Ver panorama|`git status` / lazygit (panel Files)|
|Contexto de 3 vías|`merge.conflictStyle = zdiff3`|
|Resolución automática de falsos conflictos|mergiraf (driver)|
|Auditar qué resolvió mergiraf|`mergiraf review`|
|Entender diffs de cada lado (Python)|`git diff --ours/--theirs`, difftastic|
|Resolver conflictos reales|Meld (`git mergetool`) o lazygit|
|Cerrar|`git add` → `git commit` / `rebase --continue`|

---