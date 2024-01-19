#!/usr/bin/pup
#Installing flask from pip3
package { 'python3-pip':
  ensure   => installed,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => package['python3-pip'],
}

package { 'werkzeug':
  ensure   => '2.0.1',
  provider => 'pip',
  require  => package['python3-pip'],
}
