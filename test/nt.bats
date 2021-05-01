#!/usr/bin/env bats
# Testing "nt" permanent notification script

load 'test_helpers/bats-support/load'
load 'test_helpers/bats-assert'
load 'test_helpers/bats-file'
load 'test_helpers/loopzen-helper'

@test "'nt' - with parmas" {
    msg="Test notification"
    run nt "${msg}"
    assert_success
    assert_output --partial "${msg}"
}

@test "'nt' - without parmas" {
    run nt
    assert_success
    assert_output --partial "Empty notification"
}
