# a puppet resource that executes a command.

exec { 'kill_killmenow':
  command => '/usr/bin/pkill killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'pgrep killmenow',
}
