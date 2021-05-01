#!/usr/bin/env bats
# Testing "opener" validations

load 'test_helpers/bats-support/load'
load 'test_helpers/bats-assert'
load 'test_helpers/bats-file'
load 'test_helpers/loopzen-helper'

@test "'opener' - without parmas" {
    run opener
    assert_failure
    assert_output "Select a file"
}

@test "'opener' - file not exists" {
    run opener fakefile.txt
    assert_failure
    assert_output "File not exists"
}
