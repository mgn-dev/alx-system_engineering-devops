# Allow login and file access for the holberton user without errors.

exec {'allow user file access':
  command => 'awk \'/holberton/ {gsub("holberton", "foo")}1\' /etc/security/limits.conf | \
              sudo tee /etc/security/limits.conf > /dev/null',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/:/usr/local/bin'
}
