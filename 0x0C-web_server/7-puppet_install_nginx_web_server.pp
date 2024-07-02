# puppet script to configure ubuntu server

package {'nginx':
  ensure => 'installed',
}

service {'nginx':
  ensure  => running,
  require => Package['nginx'],
}

file {'/var/www/html/index.html':
  content => 'Hello World!',
}

exec { 'redirect_me':
  command  => "sudo sed -i '53i\\tlocation /redirect_me { return 301 \$REDIRECT_URL; }' /etc/nginx/sites-available/default",
  provider => 'shell',
  before   => Exec['restart'],
}

exec {'restart':
  command  => 'sudo service nginx restart',
  provider => 'shell',
}
