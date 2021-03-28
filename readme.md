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

* fdb selects a connection of a file like this and connects with the appropiate database cli

~~~txt
NAME              | CONNECTION
mysql_clients     | --host=localhost --port=3306 --protocol=TCP --user=user --password=pass --database=database
oracle_workers    | USER/mypass3@server:port/sid
sqlite_configs    | /home/loopzen/src/configs/configs.db
~~~
