#!/usr/bin/env bats
# Testing "in" script

load 'test_helpers/bats-support/load'
load 'test_helpers/bats-assert'
load 'test_helpers/bats-file'
load 'test_helpers/loopzen-helper'

@test "'in' - without parmas" {
    run in
    assert_failure
    assert_output "Insert text"
}

@test "'in' - with serveral params" {
    run in HOLA MUNDO
    assert_success
    assert_output --partial "HOLA MUNDO"
    GTD_INBOX=/home/loopzen/doc/gtd/1_in.md
    assert_file_exist $GTD_INBOX
    remove_last_inserted_lines "2" "$GTD_INBOX"
}
