#! /bin/bash

process_line=`ps aux | grep app.py | grep -v color`

if [ $? -eq 0 ]; then
  echo $process_line | awk '{print $2}' | xargs kill
fi

exit 0
