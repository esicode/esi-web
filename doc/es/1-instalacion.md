**Instalando el ambiente de desarrollo**
------------------------------------

**Programas necesarios:**

 - VirtualBox
 - Vagrant
 - Git

**Pasos necesiarios para empezar:**
```
git clone http://github.com/esicode/esi-web
git submodule init
git submodule update
cd esi-web
vagrant up
vagrant ssh
./manage.py syncdb
./manage.py runserver

```
Clone el repositorio:
```
git clone http://github.com/esicode/esi-web

```
Inicie y actualice los submódulos de Git
```
git submodule init
git submodule update
```
Inicie Vagrant
```
vagrant up
```

Conéctese a la máquina virtual

```
vagrant ssh
```
Es necesaria la actualización de las bases de datos de Django.
```
./manage.py syncdb
```
Y por último inicie el servidor Django.
```
./manage.py runserver
```
