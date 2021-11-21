import os.path
from pathlib import Path
import subprocess
import datetime
import socket
import getpass

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def maybe_complete_command(cmd, valid_input, prompt):
  while True:
    user_input = input(bcolors.OKGREEN + prompt + bcolors.ENDC)
    for i in range(len(valid_input)):
      if valid_input[i] == user_input :
        process = subprocess.Popen(cmd[i].split())
        return_code = process.wait()
        return

def add_symlink(src_file, target_file):
  src = Path(src_file)
  if src.is_file():
    cmd = ["rm " + src_file, 'head ' + src_file]
    valid_input = ["y", "n"]
    prompt = src_file + " exists. Do you want to delete it?[y/n]"
    maybe_complete_command(cmd, valid_input, prompt)
    if src.is_file():
      return
  subprocess.Popen(['ln', '-s', target_file, src_file])

def complete_fpath(fname):
  return os.path.expanduser(fname)

def add_ssh_keys():
  src = Path(complete_fpath('~/.ssh/id_rsa'))
  if src.is_file():
    print(bcolors.OKGREEN + "Existing ssh key found. existing....." + bcolors.ENDC)
    return
  hostname = socket.gethostname()
  username = getpass.getuser()
  date = datetime.date.today().strftime("-%d-%m-%Y")
  process = subprocess.Popen(['ssh-keygen', '-t', 'rsa', '-b', '4096', '-C', username + '@' + hostname + date])
  return_code = process.wait()

def install_pkgs():
  pkg_list = [
    ["vimrc",
      complete_fpath('~/My_custom_setup/bash_scripts/install_vimrc.sh'),
      "Do you wish to install vimrc for this system?[y/n]",
    ],
    ["Chrome",
      complete_fpath('~/My_custom_setup/bash_scripts/install_chrome.sh'),
      "Do you wish to install google Chrome for this system?[y/n]",
    ],
              ]
  for pkg in pkg_list:
    pkg_name = pkg[0]
    pkg_install_cmd = pkg[1]
    pkg_prompt = pkg[2]
    maybe_complete_command([pkg_install_cmd, 'echo ' + 'Skipping pkg: ' + pkg_name ], ['y', 'n'], pkg_prompt)

def main():
  # Adding symlinks for .gitconfig and .gitignore
  print("Adding symlinks for global .gitconfig and .gitignore")
  add_symlink(complete_fpath("~/.gitconfig"),
              complete_fpath("~/My_custom_setup/git_files/.gitconfig"))
  add_symlink(complete_fpath("~/.gitignore"),
              complete_fpath("~/My_custom_setup/git_files/.gitignore"))
  add_symlink(complete_fpath("~/.bashrc"),
              complete_fpath("~/My_custom_setup/bash_scripts/bashrc"))
  # Add ssh keys if not present
  add_ssh_keys()

  # Install Different Pkgs
  install_pkgs()

if __name__== "__main__":
  main()