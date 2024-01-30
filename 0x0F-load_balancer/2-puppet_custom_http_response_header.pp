# script to install and configure nginx
exec { 'update':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell'
}
-> package { 'nginx':
  ensure => 'installed'
}
-> file_line { 'header_served_by':
  path  => '/etc/nginx/sites-available/default',
  match => '^server {',
  line  => "server {\n\tadd_header X-Served-By \"${hostname}";",
  multiple => false
}
-> exec { 'run'
  command  => '/usr/sbin/service nginx restart'
}
-> service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}
