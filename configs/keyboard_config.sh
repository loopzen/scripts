#!/usr/bin/bash
# keyboard configs

KEYBOARD_FILE=/etc/X11/xorg.conf.d/00-keyboard.conf

if ! [ -f $KEYBOARD_FILE ]; then
    touch $KEYBOARD_FILE
fi

cat <<-EOF > $KEYBOARD_FILE
Section "InputClass"
        Identifier "system-keyboard"
        MatchIsKeyboard "on"
        Option "XkbLayout" "es"
        Option "XkbOptions" "caps:none"
EndSection
EOF
