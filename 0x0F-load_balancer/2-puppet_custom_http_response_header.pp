# Puppet manifest to configure NGINX redirect on Ubuntu server

exec { 'update system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update system'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

# Add new location directive
$redirect = 'https://www.youtube.com/watch?v=QH2-TGUlwu4'
$directive = "location /redirect { return 301 ${redirect}; }"
$nginx_conf_file = '/etc/nginx/sites-available/default'

exec { 'add_location_directive':
  command => "/bin/bash -c 'if ! grep -q \"${directive}\" \"${nginx_conf_file}\"; then sed -i \"/^\\s*location \\/ {/ { :1; /}/!{N;b1}; s|}|&\\n\\t${directive}|\" \"${nginx_conf_file}\"; fi'",
  path    => ['/bin', '/usr/bin'],
}

# Add error directive
$directive = 'error_page 404 /error_404.html;'
$nginx_conf_file = '/etc/nginx/sites-available/default'

exec { 'add_error_directive':
  command => "/bin/bash -c 'if ! grep -q \"${directive}\" \"${nginx_conf_file}\"; then sed -i \"/^\\s*location \\/ {/ { :1; /}/!{N;b1}; s|}|&\\n\\t${directive}|\" \"${nginx_conf_file}\"; fi'",
  path    => ['/bin', '/usr/bin'],
}

# Add header directive
$directive = 'add_header X-Served-By $hostname;'
$nginx_conf_file = '/etc/nginx/sites-available/default'

exec { 'add_header_directive':
  command => "/bin/bash -c 'if ! grep -q \"${directive}\" \"${nginx_conf_file}\"; then sed -i \"/^\\s*location \\/ {/a\\ \\t\\t${directive}\" \"${nginx_conf_file}\"; fi'",
  path    => ['/bin', '/usr/bin'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
