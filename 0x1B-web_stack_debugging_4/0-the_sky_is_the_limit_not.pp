# puppet script that updates nginx number of open files

exec {'update open files limit':
  command => 'awk \'/15/ {gsub("15", "10000")}1\' /etc/default/nginx > /tmp/nginx.tmp && \
              mv /tmp/nginx.tmp /etc/default/nginx && \
              sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}
