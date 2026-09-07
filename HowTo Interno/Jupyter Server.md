[the littlest Jupyter Hub](https://github.com/jupyterhub/the-littlest-jupyterhub)
# Instalación

```bash
# Funciona en Ubuntu
curl -L https://tljh.jupyter.org/bootstrap.py | sudo python3 - --admin tu_usuario
```
```bash
# En Pop_OS
sudo cp /etc/os-release /etc/os-release.bak
sudo sed -i 's/^ID=pop/ID=ubuntu/' /etc/os-release

curl -L https://tljh.jupyter.org/bootstrap.py | sudo python3 - --admin tu_usuario

# después de instalar, restaurar el original:
sudo cp /etc/os-release.bak /etc/os-release
```

Verificar
```bash
sudo systemctl status jupyterhub
```

Conectar _(entra por el puerto 80)_
```
http://IP_DEL_SERVIDOR
```

# Autentificación

Lo confguramos para que no pida password. Cualquier error de tipeo genera un nuevo usuario:

```bash
sudo tljh-config set auth.type dummyauthenticator.DummyAuthenticator 
sudo tljh-config set auth.type dummy
sudo tljh-config reload
```

Si queremos, más adelante, bloquear el registro de usuarios a los ya existentes:

```bash
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
  ```bash
    sudo userdel -r nombre_usuario
  ```

# Instalar Librerías

```bash
sudo -E conda install -c conda-forge numpy scipy matplotlib -y
```

o con `pip`:

```bash
sudo /opt/tljh/user/bin/python -m pip install numpy scipy matplotlib
```
# Trabajos prácticos

