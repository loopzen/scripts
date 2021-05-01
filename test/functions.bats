#!/usr/bin/env bats
# Testing "functions"

source /home/loopzen/src/scripts/functions.sh

load 'test_helpers/bats-support/load'
load 'test_helpers/bats-assert'
load 'test_helpers/bats-file'
load 'test_helpers/loopzen-helper'

setup () {
    DIR_TESTING=$(temp_dir_make)
    echo "Hola Mundo" > "${DIR_TESTING}/test.txt"
}

teardown () {
    rm -r "$DIR_TESTING"
}

@test "'functions' - filetype - text/plain" {
    run filetype "${DIR_TESTING}/test.txt"
    assert_success
    assert_output "text/plain"
}

@test "'functions' - check_execution - active process" {
    run check_execution "tmux"
    assert_success
    [[ "$output" -gt 1 ]]
}

@test "'functions' - check_execution - fake process" {
    run check_execution "fake_proccess"
    assert_success
    [[ "$output" -eq 0 ]]
}

@test "'functions' - create_year_month_directory_structure" {
    run create_year_month_directory_structure $DIR_TESTING
    YEAR=
    YEAR=$(date +%Y)
    MONTH=$(date +%m)
    assert_file_exist "$DIR_TESTING/${YEAR}/${MONTH}"
}
