#! /bin/bash

ps aux | grep app.py | grep -v color | awk '{print $2}' | xargs kill
