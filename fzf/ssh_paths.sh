#!/bin/bash
# Extract configured Host of .ssh/config
ssh_paths.awk $HOME/.ssh/config
sort -u --field-separator='|' -o "$HOME"/.ssh/init_login_paths "$HOME"/.ssh/init_login_paths
