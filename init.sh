#!/bin/bash

while true; do
    read -p "Do you wish to install vimrc for this system?[y/n]" yn
    case $yn in
        [Yy]* ) cd ~/;
		git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime
		sh ~/.vim_runtime/install_awesome_vimrc.sh
        ln -s ~/My_custom_setup/vim_files/my_configs.vim ~/.vim_runtime/my_configs.vim
		break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no";;
    esac
done
