#!/bin/bash

while true; do
    read -p "Do you wish to install vimrc for this system?[y/n]" yn
    case $yn in
        [Yy]* ) git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime
                sh ~/.vim_runtime/install_awesome_vimrc.sh
                ln -s `pwd`/vim_files/my_configs.vim ~/.vim_runtime/my_configs.vim
                break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no";;
    esac
done

while true; do
    read -p "Do you wish to install google Chrome for this system?[y/n]" yn
    case $yn in
        [Yy]* ) cd ~/Downloads;
                wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
                sudo dpkg -i google-chrome-stable_current_amd64.deb
                break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no";;
    esac
done
