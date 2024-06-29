# install flask from pip3
include python

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

