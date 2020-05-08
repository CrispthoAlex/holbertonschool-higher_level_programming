#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        maxval = [(value, key) for key, value in a_dictionary.items()]
        return (max(maxval)[1])
    return(None)
