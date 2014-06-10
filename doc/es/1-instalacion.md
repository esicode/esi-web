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
[Use este enlace para descargarlo][3] (Versión 1.9.3 en adelante)
####En Linux
Lea instrucciones de instalación [aquí][4].
###PuTTY (Solo en Windows)
[Use este enlace para descargarlo][5]

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
> Si está utilizando Windows deberá abrir el PuTTY e ingresar los datos que le solicita (los encontrará en la consola misma).

Al generar la base de datos por primera vez, `syncdb` le ofrecerá crear un superusuario. Se debe indicar un nombre de usuario, correo electrónico y contraseña válidos para luego acceder a la administración del sitio.
```bash
vagrant ssh
./manage.py syncdb
./manage.py runserver
```


  [1]: http://www.virtualbox.org/wiki/Downloads
  [2]: http://www.vagrantup.com/downloads.html
  [3]: http://git-scm.com/download
  [4]: http://git-scm.com/download/linux
  [5]: http://the.earth.li/~sgtatham/putty/latest/x86/putty.exe
  

##Importante

El archivo Vagrantfile esta configurado para descargar CentOS de 64 bits. Si estas usando un sistema operativo de 32 bits tendras que abrir el archivo Vagrantfile ubicado en el directorio principal del proyecto con un editor de codigo y remplazar la linea 17 del mismo por la siguiente linea:

```ruby
  #config.vm.box_url = "http://puppet-vagrant-boxes.puppetlabs.com/centos-64-x86-vbox4210.box"
```
