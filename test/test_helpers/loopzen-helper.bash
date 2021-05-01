#!/bin/bash
# My helper functions to test

temp_dir_make () {
    DIR_TESTING=$HOME/src/scripts/test/tmp
    mkdir "${DIR_TESTING}"
    echo "${DIR_TESTING}"
}

remove_last_inserted_lines () {
    number_of_lines=$1
    file=$2
    head -n -${number_of_lines} ${file} > ${file}.tmp && mv ${file}.tmp ${file}
}
