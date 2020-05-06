#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list != []:
        div2 = [True, False]
        listdiv = my_list.copy()
        for i in range(len(my_list)):
            if listdiv[i] % 2 == 0:
                listdiv[i] = div2[0]
            else:
                listdiv[i] = div2[1]
        return(listdiv)

#  return(tuple(sum(i) for i in zip(tuple_a, tuple_b))) <-- remember

#  zip() https://realpython.com/python-zip-function/
#  /understanding-the-python-zip-function
