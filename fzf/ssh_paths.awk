#!/bin/awk -f
BEGIN {
    FS=" "
    ssh_init_path="/home/loopzen/.ssh/init_login_paths"
}

/^Host/ && ! /^Host \*/ {
    print $2 " | default | default" | "tee -a " ssh_init_path
}

