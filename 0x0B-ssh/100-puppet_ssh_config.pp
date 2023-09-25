# changes to the configuration file ssh_config

file {'~/.ssh/ssh_config':

  content => 'PasswordAuthentication no\nIdentityFile ~/.ssh/school'
}

