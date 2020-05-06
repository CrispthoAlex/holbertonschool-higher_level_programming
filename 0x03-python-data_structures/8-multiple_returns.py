#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        a = None
    else:
        a = sentence[0]
    newtuple = (len(sentence), a)
    return (newtuple)

#  return(tuple(sum(i) for i in zip(tuple_a, tuple_b))) <-- remember

#  zip() https://realpython.com/python-zip-function/
#  /understanding-the-python-zip-function
