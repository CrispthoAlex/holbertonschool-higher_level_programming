#!/bin/bash
# Script that ends a JSON POST request to a URL passed as the first argument
curl -s  "$1" -d @"$2" -H "Content-Type: application/json"
