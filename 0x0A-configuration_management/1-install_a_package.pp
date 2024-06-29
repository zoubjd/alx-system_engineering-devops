# install flask from pip

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
  require => Package['python3-pip'],
}

