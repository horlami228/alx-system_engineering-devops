# changes to the configuration file ssh_config

include stdlib


file_line {'No passpword auth':

  ensure  => present,
  path    => '~/.ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  replace => true,
}

file_line {'Use private key':

        ensure  => present,
        path    => '~/.ssh/ssh_config',
        line    => 'IdentityFile ~/.ssh/school',
        replace => true,
}


