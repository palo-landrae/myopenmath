import re
import sys
import numpy as np


def main():
    a = user_input('Enter First matrix: ')
    b = user_input('Enter Second Matrix: ')

    c = np.array(a * b)
    display(c)


def user_input(message):
    print(message)
    lines = [x for x in sys.stdin.read().splitlines(True)]
    list_str = [re.split(r'[\s]+', x)[:-1] for x in lines]
    mtx = np.matrix([list(map(int, x)) for x in list_str])
    return mtx


def display(mtx):
    print('The result is: ')
    for line in mtx:
        print('  '.join(map(str, line)))


if __name__ == "__main__":
    main()
