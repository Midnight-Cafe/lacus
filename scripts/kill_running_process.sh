#! /bin/bash

ps aux | grep app.py | grep -v color | awk '{print $2}' | xargs kill > /dev/null 2>&1
