# set up your client SSH configuration file so that you 
# can connect to a server without typing a password.

file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/sshd_config',
  line  => 'PasswordAuthentication no',
  match => '^#?PasswordAuthentication.*',
}

file_line { 'Declare identity file':
  path  => '/etc/ssh/sshd_config',
  line  => 'PermitRootLogin without-password',
  match => '^#?PermitRootLogin.*',
}

service { 'sshd':
  ensure    => 'running',
  enable    => true,
  subscribe => File_line['Turn off passwd auth', 'Declare identity file'],
}
