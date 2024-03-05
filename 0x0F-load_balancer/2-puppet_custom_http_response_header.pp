# Puppet manifest to configure NGINX redirect on Ubuntu server

# Install NGINX package
package { 'nginx':
  ensure => installed,
}

# Allow directory ownership for the current user
file { '/var/www/html':
  ensure  => directory,
  owner   => $user,
  group   => $user,
  recurse => true,
}

file { '/etc/nginx':
  ensure  => directory,
  owner   => $user,
  group   => $user,
  recurse => true,
}

# Create index.html file
file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
}

# Create error_404.html file
file { '/var/www/html/error_404.html':
  ensure  => file,
  content => "Ceci n'est pas une page\n",
}

# Add new location directive
$redirect = 'https://www.youtube.com/watch?v=QH2-TGUlwu4'
$directive = "location /redirect { return 301 $redirect; }"
$nginx_conf_file = '/etc/nginx/sites-available/default'

exec { 'add_location_directive':
  command => "/bin/bash -c 'if ! grep -q \"$directive\" \"$nginx_conf_file\"; then sed -i \"/^\t*location \\/ {/ { :1; /}/!{N;b1}; s|}|&\\n\\t$directive| }\" \"$nginx_conf_file\"; fi'",
  path    => '/usr/bin:/bin',
}

# Add error directive
$directive = 'error_page 404 /error_404.html;'
$nginx_conf_file = '/etc/nginx/sites-available/default'

exec { 'add_error_directive':
  command => "/bin/bash -c 'if ! grep -q \"$directive\" \"$nginx_conf_file\"; then sed -i \"/^\t*location \\/ {/ { :1; /}/!{N;b1}; s|}|&\\n\\t$directive| }\" \"$nginx_conf_file\"; fi'",
  path    => '/usr/bin:/bin',
}

# Add header directive
$directive = 'add_header X-Served-By $hostname;'
$nginx_conf_file = '/etc/nginx/sites-available/default'

exec { 'add_header_directive':
  command => "/bin/bash -c 'if ! grep -q \"$directive\" \"$nginx_conf_file\"; then sed -i \"/^\tlocation \\/ {/a\\ \\t\\t$directive\" \"$nginx_conf_file\"; fi'",
  path    => '/usr/bin:/bin',
}

# Restart NGINX
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Exec['add_location_directive', 'add_error_directive', 'add_header_directive'],
  notify  => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command     => 'sudo service nginx restart',
  refreshonly => true,
}
