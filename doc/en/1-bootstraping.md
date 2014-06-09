Installing the development environment
======================================
Requirements
------------
###VirtualBox
[Use this download link][1] (4.3.12 or later)
###Vagrant
[Use this download link][2] (1.6.3 or later)
###Git
#### On Windows
[Read this instructions][3] (Section 1.1 Git on Windows)
#### On Linux
[Check this link][4] for download instructions

Cloning the sources
-------------------
```bash
git clone http://github.com/esicode/esi-web
cd esi-web
git submodule init
git submodule update
```
Now, install and bootstrap a virtual machine
```bash
$ vagrant up
$ vagrant ssh
```
Now you can access to the machine and test it.

In the first time the database will be generated, It will request to create a superuser, 
For that you will need to enter a valid username, password and e-mail address which
will be asked when accessing the administration panel of the website.
```
$ ./manage.py syncdb
$ ./manage.py runserver 0.0.0.0:8000
```
You can access the server using
```
localhost:8000 
```


  [1]: http://www.virtualbox.org/wiki/Downloads
  [2]: http://www.vagrantup.com/downloads.html
  [3]: 1.1-git-windows.md
  [4]: http://git-scm.com/download/linux
