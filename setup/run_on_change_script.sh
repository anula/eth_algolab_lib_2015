#!/bin/bash

# Usage: ./this_script.sh source_code.cpp make_rule

### Set initial time of file
LTIME=`stat -c %Z $1`

while true    
do
    ATIME=`stat -c %Z $1`

    if [[ "$ATIME" != "$LTIME" ]]
    then    
        echo -e "\033[01;32m---------------\033[00;0m";
        make $2;
        LTIME=$ATIME
    fi
    sleep 5
done
