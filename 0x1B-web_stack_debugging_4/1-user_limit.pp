# puupet script to change OS configuration so 
# that it is possible to login with the holberton 
# user and open a file without any error message.

exec {'OS config':
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}
