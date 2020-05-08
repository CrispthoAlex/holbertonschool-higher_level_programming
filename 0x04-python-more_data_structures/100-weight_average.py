#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sumdiv = sumprod = multiaxb = average = 0
        for tuple in my_list:
            sumdiv += tuple[1]
            multiaxb = tuple[0] * tuple[1]  # sum tuple index
            sumprod += multiaxb
            average = sumprod / sumdiv
        return average
    return 0
