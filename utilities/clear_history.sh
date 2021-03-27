#!/usr/bin/bash
# CLEAR FIREFOX HISTORY
source $HOME/src/scripts/functions.sh

pgrep -u $USER firefox > /dev/null
if [[ $? -eq 0 ]]; then
    pkill firefox
fi

FIREFOX_USERS=$(ls $HOME/.mozilla/firefox 2>/dev/null | grep .default)
for firefox_user in $FIREFOX_USERS; do
    log_inf FIREFOX USER - $firefox_user
    # History
    sqlite3 ${HOME}/.mozilla/firefox/${firefox_user}/places.sqlite "delete from moz_historyvisits;" > /dev/null 2>&1
    sqlite3 ${HOME}/.mozilla/firefox/${firefox_user}/places.sqlite "delete from moz_inputhistory;" > /dev/null 2>&1
    sqlite3 ${HOME}/.mozilla/firefox/${firefox_user}/places.sqlite "delete from moz_places;" > /dev/null 2>&1
    sqlite3 ${HOME}/.mozilla/firefox/${firefox_user}/places.sqlite "delete from moz_origins;" > /dev/null 2>&1
    sqlite3 ${HOME}/.mozilla/firefox/${firefox_user}/places.sqlite "delete from moz_bookmarks;" > /dev/null 2>&1
    sqlite3 ${HOME}/.mozilla/firefox/${firefox_user}/places.sqlite "delete from moz_bookmarks_deleted;" > /dev/null 2>&1
    sqlite3 ${HOME}/.mozilla/firefox/${firefox_user}/formhistory.sqlite "delete from moz_formhistory;" > /dev/null 2>&1
    sqlite3 ${HOME}/.mozilla/firefox/${firefox_user}/formhistory.sqlite "delete from moz_sources;" > /dev/null 2>&1
    sqlite3 ${HOME}/.mozilla/firefox/${firefox_user}/formhistory.sqlite "delete from moz_history_to_sources;" > /dev/null 2>&1

    if [[ $? = 0 ]]; then
        log_inf History DELETED
        SIZ=$(du -sbh ${HOME}/.cache/mozilla/firefox/${firefox_user}/cache2/entries)
        SIZ=$(echo $SIZ | cut -d" " -f1)
        find ${HOME}/.cache/mozilla/firefox/${firefox_user}/cache2/entries -type f -delete 2>/dev/null && log_inf Cache DELETED - Size: $SIZ || log_warn Cant delete cache
     else
         log_warn Cant doit to the user - ${firefox_user}
    fi

    # echo "Deleting Firefox Cookies........"
    # sqlite3 ${HOME}/.mozilla/firefox/${FIREFOX}/cookies.sqlite "select datetime(creationTime/1000000,'unixepoch'),host from moz_cookies; delete from moz_cookies;"
    # echo "Deleting Firefox Site Data........"
    # ls ${HOME}/.mozilla/firefox/${FIREFOX}/storage/default/ | grep http
    # find ${HOME}/.mozilla/firefox/${FIREFOX}/storage/default -name "http*" -type d -exec rm -r "{}" \; -prune
done
