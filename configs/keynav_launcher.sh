#!/bin/zsh
##############################
# Call with i3 to starter command in keynav
##############################

if ! pgrep --exact "keynav" > /dev/null ; then
    keynav &
    sleep 0.1
fi

sleep 0.1
xdotool key --clearmodifiers ctrl+comma &
