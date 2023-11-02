#!/usr/bin/python3
if __name__ == "__main__":

    import calculator_1 as cl

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, cl.add(a, b)))
    print("{} - {} = {}".format(a, b, cl.sub(a, b)))
    print("{} * {} = {}".format(a, b, cl.mul(a, b)))
    print("{} / {} = {}".format(a, b, cl.div(a, b)))
