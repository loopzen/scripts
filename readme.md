# USEFUL SCRIPTS

## CONTENT
~~~txt
loopzen/scripts
├── configs                    (system configurations)
│   ├── autoinstallation       (Install all your packages after Linux installation)
│   ├── autologin              (Set autologin in your $USER session)
│   ├── clean_home.sh          (Clean junk file form $HOME directory)
│   ├── dotconfig.py           (Link your dotfiles, enable services, activate your shell...)
│   ├── keyboard_config.sh     (Config your keyboard, solve plug bugs)
│   └── keynav_launcher.sh     (Script to may keynav to any key. Useful with i3)
├── dmenus                     (dmenus scripts)
│   ├── dmenu_executor         (Run any command with dmenu)
│   └── dmenu_tmux             (Dmenu tmux windows selector)
├── fzf                        (Fuzzy Finder scripts)
│   ├── fcfg                   (Choose dotfile to edit)
│   ├── ff                     (Find file and open it with programmand defined in opener script)
│   ├── opener                 (Called by ff)
│   ├── fdb                    (See [fdb](#fdb section)
│   ├── fssh                   (See [fssh](#fssh) section)
│   ├── ssh_paths.awk          (See [fssh](#fssh) section)
│   └── ssh_paths.sh           (See [fssh](#fssh) section)
└── utilities
    ├── clear_history.sh       (Clear Firefox history, cache...)
    ├── clip                   (Copy to clipboard)
    ├── in                     (Copy to inbox file (GTD method))
    ├── nt                     (Set Notification Permanent. It is like a post_it)
    ├── send_mail_gmail.py     (Send mail)
    └── trello_extractor.py    (Extract notes from Trello)
~~~

## fssh

> fssh lets you connect server quickly

When you run fssh this happen:
1. You have to choose between ssh or sftp connection
2. You have to choose the Host and the paths (local and remote)
    * The hosts to choose are defined into a file like next
    * With ssh_paths.sh you can load your Hosts defined into .ssh/config with
      "default" init paths. If you want define more paths, you have to add them
      manually.

~~~txt
init_login_paths
host1 | default | default
host2 | default | default
host2 | /home/user/path/to/local/directory | /home/user/path/to/remote/directory
~~~

3. Connect
    * If you have a ssh-key shared with the host, fssh connects directly
    * If you don't have ssh-key, it connect with sshpass
    * fssh decides how to connect reading a file like this. If the Host is not
      in this file, it try to connect directly

~~~txt
autologins
CONNECTION                       | PASSWORD
server1                          | superpass
server2                          | easyhackeablepass
~~~

## fdb


* fdb selects a connection of a file like this and connects with the appropriate database CLI

~~~txt
NAME              | CONNECTION
mysql_clients     | --host=localhost --port=3306 --protocol=TCP --user=user --password=pass --database=database
oracle_workers    | USER/mypass3@server:port/sid
sqlite_configs    | /home/loopzen/src/configs/configs.db
~~~

* Once the connection is choosen, you can use Vim and Slime to send your queries
  to this connection

~~~vim
sql.vim
" ENVIAR COSAS POR SLIME WITH PREIX AND SUFIX iintentar enteder este de la selcitno visuatl.
" - Requier C-U para quitar lo del rango '<'>
" - http://vim.1045645.n5.nabble.com/Is-there-any-way-to-get-visual-selected-text-in-VIM-script-td1171241.html#a1171243
" - El texto selecionado se envia con un prefijo (spool) y sufijo (spool) para que el contendio dela query de oracle se envie al panel de tmux. El resto de clientes de base de datos no erquieren hacer esto. Su propia configuaracion lo permiten
" - Mandar comando a Slime con prefjo y sufijo puede ser muy intersante para otro tipo de cosas
function! s:GetVisual() range
    let reg_save = getreg('"')
    let regtype_save = getregtype('"')
    let cb_save = &clipboard
    set clipboard&
    silent normal! ""gvy
    let selection = getreg('"')
    call setreg('"', reg_save, regtype_save)
    let &clipboard = cb_save
    return selection
endfunction

function! SendOracle(text)
    " prefix
    call slime#send("SPOOL /tmp/sql.out REPLACE" . "\r")
    " content
    call slime#send(a:text . "\r")
    " postfix
    call slime#send("SPOOL OFF" . "\r")
endfunction

function! SendSQLite(text)
    " prefix
    call slime#send(".output '/tmp/sql.out'" . "\r")
    " content
    call slime#send(a:text . "\r")
    " postfix
    call slime#send(".output stdout" . "\r")
endfunction

command! OracleSpool call SendOracle(s:GetVisual())
command! SQLiteSpool call SendSQLite(s:GetVisual())
~~~
