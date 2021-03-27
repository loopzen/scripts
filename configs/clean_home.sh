#!/bin/bash
# Clean $HOME directory

# autogenerate with charge wallapaper
[ -f $HOME/.fehbg ] && rm .fehbg && echo -e "${CYAN}[INFO]${RESET} .fehbg borrado"

# autogenerate when you use sqlplus
[ -d $HOME/oradiag_${USER} ] && rm -r $HOME/oradiag_${USER} && echo -e "${CYAN}[INFO]${RESET} .oradiag_${USER} borrado"

# log from selenium
[ -f $HOME/geckodriver.log ] && rm $HOME/geckodriver.log && echo -e "${CYAN}[INFO]${RESET} geckodriver.log borrado"

# python history and caches
[ -f $HOME/.python_history ] && rm $HOME/.python_history && echo -e "${CYAN}[INFO]${RESET} .pytho_history borrado"

# Some app creates these folders
[ -d $HOME/Desktop ] && rm -r $HOME/Desktop && echo -e "${CYAN}[INFO]${RESET} Desktop borrado"
[ -d $HOME/Downloads ] && rm -r $HOME/Downloads && echo -e "${CYAN}[INFO]${RESET} Downloads borrado"

# bash files
[ -f $HOME/.bash_history ] && rm  $HOME/.bash_history  && echo -e "${CYAN}[INFO]${RESET} .bash_history borrado"
[ -f $HOME/.bash_profile ] && rm  $HOME/.bash_logout  && echo -e "${CYAN}[INFO]${RESET} .bash_profile borrado"
[ -f $HOME/.bash_logout ] && rm $HOME/.bash_logout  && echo -e "${CYAN}[INFO]${RESET} .bash_logout borrado"
[ -f $HOME/.bashrc ] && rm $HOME/.bashrc && echo -e "${CYAN}[INFO]${RESET} .bashrc borrado"

# others
[ -f $HOME/.zshrc.zwc ] && rm -f $HOME/.zshrc.zwc && echo -e "${CYAN}[INFO]${RESET} .zshrc.zwd borrado" ||  echo -e "${CYAN}[INFO]${RESET} .zshrc.zwd no existe"
