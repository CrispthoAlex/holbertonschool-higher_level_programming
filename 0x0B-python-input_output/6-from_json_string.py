#!/usr/bin/python3
"""function: returns an object (data structure) represented by JSON string:"""
import json


def from_json_string(my_str):
    """
    Returns the JSON representation of an object (string)
    Args:
        @my_obj:
    """
    return json.loads(my_str)
