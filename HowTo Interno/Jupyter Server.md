[the littlest Jupyter Hub](https://github.com/jupyterhub/the-littlest-jupyterhub)
# Instalación

```Bash
# Funciona en Ubuntu
curl -L https://tljh.jupyter.org/bootstrap.py | sudo python3 - --admin tu_usuario
```
```Bash
# En Pop_OS
sudo cp /etc/os-release /etc/os-release.bak
sudo sed -i 's/^ID=pop/ID=ubuntu/' /etc/os-release

curl -L https://tljh.jupyter.org/bootstrap.py | sudo python3 - --admin tu_usuario

# después de instalar, restaurar el original:
sudo cp /etc/os-release.bak /etc/os-release
```

Verificar
```Bash
sudo systemctl status jupyterhub
```

Conectar _(entra por el puerto 80)_
```
http://IP_DEL_SERVIDOR
```

# Autentificación

Lo confguramos para que no pida password. Cualquier error de tipeo genera un nuevo usuario:

```Bash
sudo tljh-config set auth.type dummyauthenticator.DummyAuthenticator 
sudo tljh-config set auth.type dummy
sudo tljh-config reload
```

Si queremos, más adelante, bloquear el registro de usuarios a los ya existentes:

```Bash
sudo tljh-config set auth.DummyAuthenticator.allow_all false
sudo tljh-config set auth.DummyAuthenticator.allow_existing_users true
sudo tljh-config reload
```

# Usuarios

Los crea como usuarios del sistema con directorios:

`/home/jupyter-<user>` 

Todos pertenecen al grupo `jupyterhub-users`

Para borrarlos:

* Primero lo borramos del panel de administrador http://python.local/hub/admin
* Después del sistema:
  ```Bash
    sudo userdel -r nombre_usuario
  ```

# Instalar Librerías

Con `pip`:

```Bash
sudo /opt/tljh/user/bin/python -m pip install numpy scipy matplotlib
```
# Trabajos prácticos

Hay un directorio que sólo puede escribir el grupo docentes que está en   
`/opt/tljh/shared/tps` y creé un link simbólico al directorio `TPs` en la raíz de cada docente. 

Basta escribir ahí para que aparezca un TP. 

Eso está contruido de esta manera:

>[!note]- `/opt/tljh/config/jupyterhub_config.d/shared_tps.py`
>```Python
> import os
> import pwd
> 
> # Carpetas compartidas: (directorio destino, nombre del symlink en el home)
> SHARED_FOLDERS = [
>     ("/opt/tljh/shared/tps", "TPs"),
>     ("/opt/tljh/shared/compartidos", "Compartidos"),
> ]
> 
> def link_shared_folders(spawner):
>     username = spawner.user.name
>     home = f"/home/jupyter-{username}"
>     pw = pwd.getpwnam(username)
> 
>     for shared_dir, link_name in SHARED_FOLDERS:
>         link_path = os.path.join(home, link_name)
> 
>         if os.path.exists(link_path) or os.path.islink(link_path):
>             continue  # ya existe, no tocar (evita pisar algo del usuario)
> 
>         os.symlink(shared_dir, link_path)
> 
>         # el symlink en sí queda de propiedad del usuario (no cambia nada del target)
>         os.lchown(link_path, pw.pw_uid, pw.pw_gid)
> 
> c.Spawner.pre_spawn_hook = link_shared_folders
> ```

---