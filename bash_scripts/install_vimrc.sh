#!/usr/bin/env bash

git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime
sh ~/.vim_runtime/install_awesome_vimrc.sh
ln -s `pwd`/vim_files/my_configs.vim ~/.vim_runtime/my_configs.vim