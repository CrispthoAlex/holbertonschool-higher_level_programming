#!/bin/bash
# This script sends a request to a URL passed as an argument, and displays only the status code
curl -sw "%{http_code}" "$1" -o /dev/null
