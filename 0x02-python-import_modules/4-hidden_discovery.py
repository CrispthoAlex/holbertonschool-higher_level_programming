#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for i in dir(hidden_4) and not i[0] != "__":
        print("{}".format(i))
