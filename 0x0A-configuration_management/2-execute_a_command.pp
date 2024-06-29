# create a manifest that kills a process named killmenow

exec { 'pkill_killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
  refreshonly => true,
}

