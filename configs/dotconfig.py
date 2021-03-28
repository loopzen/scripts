#!/usr/bin/python3
# DESCRIPTION: pyton script to create symbolic links and another system configs
import os
import shutil
from os.path import expanduser

# PATHS
home_folder = expanduser("~")

cron_file_home = home_folder + "/src/conf/crontab_jobs"
cron_file_work = home_folder + "/src/conf/work_crontab_jobs"
cron_file_raspberry = home_folder + "/src/conf/raspberry_crontab_jobs"

dot_path = home_folder + "/dot"

files_directories = [
    "/.xinitrc",
    "/.tmux.conf",
    "/.config/davmail",
    "/.config/khal",
    "/.config/vdirsyncer",
    "/.config/sounds",
    "/.config/eslint",
    "/.config/vifm",
    "/.config/X11",
    "/.config/gnupg",
    "/.config/urxvt",
    "/.config/pass",
    "/.config/zsh",
    "/.config/mutt",
    "/.config/git",
    "/.config/tmux",
    "/.config/tmuxp",
    "/.config/abook",
    "/.config/mysql",
    "/.config/proxychains",
    "/.config/notmuch",
    "/.config/newsboat",
    "/.config/keynav",
    "/.config/screenlayout",
    "/.config/pomobar.conf",
    "/.config/greenclip.cfg",
    "/.config/locale.conf",
    "/.config/picom",
    "/.config/wallpaper.jpg",  # wallpaper
    "/.config/wallpaper.png",  # wallpaper
    "/.config/grub.png",  # grub background
    "/.config/flake8",
    "/.config/zathura",
    "/.config/UltiSnips",
    "/.config/polybar",
    "/.config/pyradio",
    "/.config/i3",
    "/.config/snippet",
    "/.config/zsh_plugins",
    "/.config/ranger",
    "/.config/exports",
    "/.config/sxiv",
    "/.config/qutebrowser",
    "/.config/mimeapps.list",
    "/.config/dunst",
    "/.config/cmus/rc",
    "/.config/cmus/playlists",
    "/.config/gtk-3.0",
    "/.config/gtk-2.0",
    "/.config/bat",
    "/.config/homepage",
    "/.config/nvim/init.vim", # vim config
    "/.config/nvim/plugged/vim-airline/autoload/airline/themes/loopzen.vim", # vim custom airline theme
    "/.config/nvim/coc-settings.json", # coc plugin - settings
    "/.config/nvim/syntax", # custom syntax
    "/.config/nvim/spell", # custom dictionaries
    "/.config/nvim/readme.md",
    "/.config/nvim/after", # custom configs to specific filetypes
    "/.config/nvim/cfg", # custom configs to specific filetypes
    "/.config/nvim/layouts", # layouts
    "/.config/nvim/autoload", # autoload functions
    "/.config/nvim/plugged/vimspector/configurations", # vimspector
    "/.config/coc/ultisnips", # custom snippets
    "/.config/sqlite3", # init config sqlite to fdb script
    "/.config/sqlplus", # init config sqlplus
    "/.config/bookmarks", # personal bookmarks
    "/.config/pandoc", # pandoc metadata
    # $XDG_DATA_HOME
    "/.local/share/applications",   # custom .desktop files
    "/.local/share/fonts",   # custom fonts
    "/.local/share/DBeaverData/workspace6/General/.dbeaver/credentials-config.json", #dbeaver
    "/.local/share/DBeaverData/workspace6/General/.dbeaver/data-sources.json",  # dbeaver
    # OTHER
    "/.ssh/config",
    "/.ssh/autologins",
    "/.ssh/vifm_sshfs",
    "/.ssh/init_login_paths",
    "/.w3m/config",
    "/.w3m/keymap",
    "/.w3m/mailcap",
    # HOME
    "/.icons",   # # cursor themes
    "/.zshenv",
    "/.urlview",
    "/.vrapperrc",
    "/.profile",
]

folders = [
    "bck",  # backup
    "syn",  # sync folder
    "doc",  # documentation
    "dot",  # dot files
    "mtm",  # multimedia
    "rep",  # public repos
    "src",  # source code
    "tmp",  # temporal files
    "pro",  # current projects
]


all_services_to_enable = [
    "cronie.service",  # cronjobs service
    "geoclue.service",  # geolocation service
    "ufw.service",  # uncomplicated firewall service
    "nordvpnd.service",  # vpn
]

def create_my_folder_structure():
    """
    Create folders
    """
    print("INFO: CREANDO ESTRUCTURA DE CARPETAS")
    for folder in folders:
        if not os.path.exists(home_folder + '/{}'.format(folder)):
            os.makedirs(home_folder + '/{}'.format(folder))
            print("INFO: La carpeta {} se creó con éxito.".format(folder))
        else:
            print("INFO: La carpeta {} ya existe.".format(folder))



def clean_path(destiny):
    """Limpiamos la ruta de destino antes de crear los enlaces simbolicos"""
    try:
        if os.path.islink(destiny):
            os.remove(destiny)
            print("El archivo " + destiny + " se borra")
        elif os.path.isfile(destiny):
            os.remove(destiny)
            print("El archivo " + destiny + " se borra")
        elif os.path.isdir(destiny):
            shutil.rmtree(destiny)
    except FileNotFoundError:
        print("El archivo " + destiny + " NO se borra porque no exite")


def create_symlink(relative_path_to_file_to_link):
    source = dot_path + relative_path_to_file_to_link
    destiny = home_folder + relative_path_to_file_to_link
    clean_path(destiny)
    try:
        if os.path.isfile(source) or os.path.isdir(source):
            os.symlink(source, destiny)
            print("Symlink to " + relative_path_to_file_to_link + " creado")
        else:
            print("No existe el fichero o directorio: " + source)
    except Exception as e:
        print(e)


def load_cron_jobs(cron_file):
    """
    Load crontab with cronjobs of the file
    """
    try:
        os.system("crontab {}".format(cron_file))
        print("CRONTAB ACTUALIZADO CON EL ARCHIVO: {}".format(cron_file))
    except Exception as e:
        print("ERROR Problema al actualizar los cron jobs")
        print(e)


def setLocalTime():
    """
    Set machine time
    """
    try:
        os.system("sudo cp /usr/share/zoneinfo/Europe/Madrid /etc/localtime")
        print("[INFO] -  LOCALTIME establecido")
    except Exception as e:
        print("[ERROR] - Problema al establecer el LOCALTIME")
        print(e)


def enable_services(services):
    """
    Enable services
    """
    for service in services:
        try:
            command = "sudo systemctl enable --now {}".format(service)
            os.system(command)
            print("INFO - COMANDO: " + command)
        except Exception:
            print("ERROR habilitando el servicio: " + service)


def config_firewall():
    os.system("sudo ufw enable")


def grub_config():
    """
    Function to change grub configs
    """
    try:
        file = "/etc/default/grub"
        print("Changing grub config...")
        # Change boot timeout
        os.system("sed -i 's/GRUB_TIMEOUT=5/GRUB_TIMEOUT=2/g' {}".format(file))
        # Chang background TEXT INITIAL -> #GRUB_BACKGROUND="/path/to/wallpaper"
        os.system(
            'sed -i \'s|\#GRUB_BACKGROUND="/path/to/wallpaper"|GRUB_BACKGROUND="/home/loopzen/.config/grub.png"|g\' {}'.format(
                file
            )
        )
        # Load new config
        os.system("grub-mkconfig > /boot/grub/grub.cfg")
    except Exception as e:
        print(e)
        print("Error al camibar la configuracion de grub")


def change_default_shell(user_name):
    try:
        os.system("sudo chsh -s $(which zsh) {}".format(user_name))
        print("ZSH like default shell")
    except Exception as e:
        print(e)
        print("Error al camibar la shell por defecto")


def main():
    # FOLDER STRUCTURE
    create_my_folder_structure()
    # SET TIME
    setLocalTime()
    # SYMLINKS
    for file_directorie in files_directories:
        create_symlink(file_directorie)
    # CRON JOBS
    if "archwork" == os.uname()[1]:
        load_cron_jobs(cron_file_work)
    elif "loopzenmachine" == os.uname()[1]:
        load_cron_jobs(cron_file_home)
    elif "archpi" == os.uname()[1]:
        load_cron_jobs(cron_file_raspberry)
    enable_services(all_services_to_enable)
    config_firewall()
    grub_config()
    user_name = os.getlogin()
    change_default_shell(user_name)


if __name__ == '__main__':
    main()
