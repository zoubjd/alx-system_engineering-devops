# 0-strace_is_your_friend.pp

# Example: Ensure a directory has correct permissions
file { '/path/to/directory':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

# Example: Ensure a configuration file is correct
file { '/etc/apache2/apache2.conf':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('my_module/apache2.conf.erb'),
  notify  => Service['apache2'],
}

# Example: Restart Apache service
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/apache2/apache2.conf'],
}

