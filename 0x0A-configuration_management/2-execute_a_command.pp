# a puppet resource that executes a command.

exec { 'kill_killmenow_process':
  command     => 'pkill killmenow',
  refreshonly => true,
  onlyif      => 'pgrep killmenow',
}
