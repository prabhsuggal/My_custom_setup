""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"customs vim files for personal use
"
"By: Prabhsimrandeep Singh
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Enabling numbering in vim
set nu

" Autofill some files with a given template
if has("win32") || has ('win64')
    let $VIMHOME = $HOME."/vimfiles/"
else
    let $VIMHOME = $HOME."/.vim/"
endif

" add templates in templates/ using filetype as file name
au BufNewFile * :silent! exec ":0r ".$VIMHOME."templates/".&ft
