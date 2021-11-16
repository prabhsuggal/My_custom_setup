# My custom setup
My custom scripts for bringing custom packages in case of a new installation

## Scripts Involved

`init.sh` : Runs the init.py script. It checks if python3 is installed or not

`init.py` : Runs installation for various packages. Things which it currrently does:

1. Add symlinks for global `.gitconfig` and `.gitignore`
2. Generate ssh keys if not present
3. Install custom `.vimrc` plugins
4. Install Google Chrome

A prompt is raised if user approval is needed. For installing pkgs, user approval is asked for.