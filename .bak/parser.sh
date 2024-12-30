#!/bin/bash

#shopt -s extglob

#re="version=\"2.0\" uid=\"(UID-[0-9]{0,5})\".*time=\"(.{24})\" start=\"(.{24})\" stale=\"(.{24})\">"
re="<event(.*)"


echo "$re"
echo "UID TIME START STALE"
while read line; do
  if [[ "$line" =~ $re ]]; then
    echo "${BASH_REMATCH[1]} ${BASH_REMATCH[2]} ${BASH_REMATCH[3]} ${BASH_REMATCH[4]} ${BASH_REMATCH[5]}"
  #else
    #echo "$line"
  fi
done < $1
