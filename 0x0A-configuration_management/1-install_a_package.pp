# puppet resources that install flask from pip3

package { 'python-pip':
  ensure => installed,
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python-pip'],
}
