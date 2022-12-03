#!/usr/bin/bash
for d in */ ; do
    if [ "$d" != "__pycache__/" ]; then
        cp *.py -r $d
        echo "$d"
    fi
done