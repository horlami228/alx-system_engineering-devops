# This is a manifest that kills a process
# process name is killmenow

exec {'kill_process':
  command => 'pkill killmenow',
  path    => '/usr/bin/',
}
