#!/bin/bash
# General utils functions

### DATES ###
now(){
   date '+%Y%m%d %H%M%S'
}
nowYYYYMMDD(){
   date '+%Y%m%d'
}
nowDD_MM_YYYY(){
   date '+%d/%m/%Y'
}


### LOGS ###
log_inf(){
    echo -e "${CYAN}[INFO]${RESET} - $*"
}
log_warn(){
    echo -e "${ORANGE}[WARN]${RESET} - $*"
}
log_error(){
    echo -e "${RED}[ERROR]${RESET} - $*"
}

### PROCESS ###
check_execution(){
    proccess_name="$1"
	counter=$(ps -ef | grep "$1" | grep -v grep | grep -v vi  | wc -l )
    echo "${counter}"
}


### FILES ###
filetype (){
    echo $(file --mime-type -b "$*")
}

create_year_month_directory_structure () {
    INIT_FOLDER="$1"
    YEAR=$(date +%Y)
    MONTH=$(date +%m)
    mkdir -p "${INIT_FOLDER}"/"${YEAR}"/"${MONTH}"
}
