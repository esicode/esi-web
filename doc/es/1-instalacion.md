Instalando el ambiente de desarrollo
====================================
Programas necesarios:
---------------------
###VirtualBox 
[Use este enlace para descargarlo][1]  (Versión 4.3.12 en adelante)
###Vagrant
[Use este enlace para descargarlo][2] (Versión 1.6.3 en adelante)
###Git
####En Windows
[Lea las siguientes instrucciones de instalacion][3] (Seccion 1.1 Git en Windows)
####En Linux
Lea instrucciones de instalación [aquí][4].

Obteniendo el código del proyecto
---------------------------------
Abrir una consola y moverse con el comando `cd` hasta la carpeta donde se
desee clonar. Luego ejecutar los siguientes comandos.
```bash
git clone http://github.com/esicode/esi-web
cd esi-web
git submodule init
git submodule update
```
Iniciando y probando el servidor web
------------------------------------
Es necesario descargar e iniciar la máquina. Utilice este comando.
```bash
$ vagrant up
```
Ahora se puede ingresar a la máquina y probar el servidor.

Al generar la base de datos por primera vez, `syncdb` le ofrecerá crear un superusuario. Se debe indicar un nombre de usuario, correo electrónico y contraseña válidos para luego acceder a la administración del sitio.

```bash
vagrant ssh
./manage.py syncdb
./manage.py runserver
```

  [1]: http://www.virtualbox.org/wiki/Downloads
  [2]: http://www.vagrantup.com/downloads.html
  [3]: 1.1-git-windows.md
  [4]: http://git-scm.com/download/linux
