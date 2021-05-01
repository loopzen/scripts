#!/usr/bin/env bats
# Testing "ex" extractor

load 'test_helpers/bats-support/load'
load 'test_helpers/bats-assert'
load 'test_helpers/bats-file'
load 'test_helpers/loopzen-helper'

setup () {
    DIR_TESTING=$(temp_dir_make)
    touch "$DIR_TESTING/test.hhhh"
    testfile=$DIR_TESTING/test.hhhh
}

teardown () {
    rm -r "$DIR_TESTING"
}

@test "'ex' - no exits file type" {
    run ex "noexistsfile.txt"
    assert_file_not_exist "noexistsfile.txt"
    assert_output "File not exists"
}

@test "'ex' - invalid filetype" {
    run ex "$testfile"
    assert_success
    assert_output "Cannot be extracted via ex"
}
