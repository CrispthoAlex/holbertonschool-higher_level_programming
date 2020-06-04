#!/usr/bin/python3
"""
script that adds all arguments to a Python list, and then save them to a file
"""
from sys import argv
from os import path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


file = "add_item.json"

new_list = []

if not path.exists(file):
    save_to_json_file(new_list, file)

new_list = list(load_from_json_file(file))

for idx in argv[1:]:
    new_list.append(idx)

save_to_json_file(new_list, file)
