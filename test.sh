#!/bin/bash

distro=$(lsb_release -i | awk '{print$3}')
if [ $distro == 'ManjaroLinux' ]; then
	alias iptool='ss'
  echo "Manjaro"
else
	alias iptool='netstat'
  echo "everything else"
fi
