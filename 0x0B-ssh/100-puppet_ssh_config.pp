# set up your client SSH configuration file so that you 
# can connect to a server without typing a password.

augeas { 'ssh_config':
  context => '/etc/ssh/ssh_config',
  changes => [
    'set PasswordAuthentication no',
    'set IdentityFile ~/.ssh/school',
  ],
  notify  => Service['ssh'], # Restart SSH service after making changes
}

service { 'ssh':
  ensure    => 'running',
  enable    => true,
  subscribe => Augeas['ssh_config'], # Restart service when config changes  
}
