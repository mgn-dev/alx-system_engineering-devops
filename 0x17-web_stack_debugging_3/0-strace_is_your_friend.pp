# debugs by changing bad php extensions 
# to php in WordPress file wp-settings.php

exec { 'debug-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
