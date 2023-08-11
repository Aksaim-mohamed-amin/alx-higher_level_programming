#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def calculate():
    argv = sys.argv
    argc = len(sys.argv)

    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return (1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    if op == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif op == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif op == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif op == '/':
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")


if __name__ == "__main__":
    calculate()
