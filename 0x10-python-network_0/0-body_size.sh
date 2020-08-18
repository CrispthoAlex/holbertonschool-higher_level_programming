#!/bin/bash
# Script displays the size of the body of the response
curl -sI "$1" | grep Length | cut -d ' ' -f2
