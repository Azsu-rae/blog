#! /bin/bash

chromium http://localhost:8000/ > /dev/null 2>&1 & disown
