Installing the development environment
======================================
Requirements
------------
 - VirtualBox
 - Vagrant
 - Git

### Tips for running on Windows
When installing git from the setup wizard ensure to use the option "Use Git from the Windows Command Prompt" Which is the 2nd option in the chapter "Adjusting your PATH environment"

Cloning the sources
-------------------
```
git clone http://github.com/esicode/esi-web
git submodule init
git submodule update
```
Now, install and bootstrap a virtual machine
```
$ vagrant up
$ vagrant ssh
$ ./manage.py syncdb
$ ./manage.py runserver
```
