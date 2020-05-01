#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys  # to use argv
    operator = '+-*/'
    nuargv = len(sys.argv) - 1
    errormsg = ["Usage: ./100-my_calculator.py <a> <operator> <b>",
                "Unknown operator. Available operators: +, -, * and /"]
    if nuargv == 3:
        if sys.argv[2] in operator:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            if sys.argv[2] == operator[0]:  # + add
                print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
            if sys.argv[2] == operator[1]:  # - sub
                print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
            if sys.argv[2] == operator[2]:  # * mul
                print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
            if sys.argv[2] == operator[3]:  # / div
                print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print("{}".format(errormsg[1]))
            exit(1)
    else:
        print("{}".format(errormsg[0]))
        exit(1)
