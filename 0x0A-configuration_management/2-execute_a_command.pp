#A manifest that kills a process named killmenow.
exec { 'kilmenow':
  command   => '/usr/bin/pkill -TERM killmenow',
}
