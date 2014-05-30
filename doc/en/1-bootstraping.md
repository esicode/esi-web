Installing the development environment
======================================
Requirements
------------
###VirtualBox
[Use this download link][4] (4.3.12 or later)
###Vagrant
[Use this download link][2] (1.6.3 or later)
###Git
#### On Windows
[Use this download link][3] (1.9.3 or later)

When installing git from the setup wizard ensure to use the option "Use Git from the Windows Command Prompt" Which is the 2nd option in the chapter "Adjusting your PATH environment"
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
$ ./manage.py syncdb
$ ./manage.py runserver
```


  [1]: http://www.virtualbox.org/wiki/Downloads
  [2]: http://www.vagrantup.com/downloads.html
  [3]: http://git-scm.com/download
  [4]: http://git-scm.com/download/linux
