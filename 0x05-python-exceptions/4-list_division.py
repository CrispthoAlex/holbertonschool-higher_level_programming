#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_div = []
    for i in range(list_length):
        list_div.append(0)  # first item = 0, later can be change
        try:
            list_div[i] = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")  # it's no integer or float
        except ZeroDivisionError:
            print("division by 0")  # division can't be done
        except LookupError:
            print("out of range")  # one list is too short
        finally:
            pass
    return (list_div)
