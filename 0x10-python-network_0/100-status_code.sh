#!/bin/bash
# This script sends a request to a URL passed as an argument, and displays only the status code
curl -sX  POST "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
