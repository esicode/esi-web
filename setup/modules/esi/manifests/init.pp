include python
include postgresql

class esi {
  package {'python-setuptools':
    ensure => "installed",
    provider => "yum"
  }

  Exec { path => "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" }
  exec {"easy_install virtualenv":
    user => "root",
    unless => "which virtualenv"
  }

  user { "esi":
    name => "esi",
    ensure => "present",
    home => "/srv/esi",
    managehome => true
  }
  file { '/srv/esi':
    ensure => directory,
    owner => "esi"
  }
  file {
    '/home/vagrant/.bashrc':
      ensure => file,
      source => "puppet:///modules/esi/bashrc-vagrant.sh",
      owner => "vagrant",
      mode => 0755
  }

  file {
    '/srv/esi/.bashrc':
      ensure => file,
      source => "puppet:///modules/esi/bashrc-esi.sh",
      owner => "vagrant",
      mode => 0755
  }

  class { "python": 
    dev => true
  }

  class { 'postgresql::server': }
  class { "postgresql::lib::devel": }
  postgresql::server::role { 'esi':
    password_hash => postgresql_password('esi', 'esi-buceo'),
  }
  postgresql::server::db { 'esi':
    user     => 'esi',
    password => postgresql_password('esi', 'esi-buceo'),
  }

  python::virtualenv { '/srv/esi/venv':
    ensure => present,
    timeout => 0,
    require => Exec["easy_install virtualenv"],
    owner => "esi"
  }
  file {
    '/srv/esi/requirements.pip':
      ensure => file,
      source => "puppet:///modules/esi/requirements.pip",
      owner => "esi"
  }
  python::requirements {
    "/srv/esi/requirements.pip" :
      virtualenv => "/srv/esi/venv",
      owner => "esi",
      require => Python::Virtualenv["/srv/esi/venv"]
  }
}
