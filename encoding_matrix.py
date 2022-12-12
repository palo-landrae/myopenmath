import re
import sys
import numpy as np


def main():
    plaintext = input("Enter the sentence: ")
    n_rows = int(input("Enter number of rows: "))
    n_col = int(input("Enter number of columns: "))

    conversion = convert_to_numbers(plaintext)
    print('Step 1: ', ', '.join(str(x) for x in conversion))

    mtx = []
    for row in range(0, n_rows):
        to_add = conversion[row*n_col:(row*n_col)+n_col]
        for _ in range(0, n_col-len(to_add)):
            to_add.append(0)
        mtx.append(to_add)
    display('Step 2: ', mtx)

    np_mtx = np.matrix(mtx)
    e_mtx = encoding_matrix()

    result = np.array(np_mtx * e_mtx)
    display('Step 3: ', result)


def encoding_matrix():
    print('Enter encoding matrix: ')
    lines = [x for x in sys.stdin.read().splitlines(True)]
    list_str = [re.split(r'[\s]+', x)[:-1] for x in lines]
    mtx = np.matrix([list(map(int, x)) for x in list_str])
    return mtx


def display(message, mtx):
    print(message)
    for line in mtx:
        print('\t'.join(map(str, line)))


def convert_to_numbers(plaintext):
    alphabet_lower = ''.join([chr(ascii) for ascii in range(97, 123)])
    numbers = dict([(i, ord(i)-96) for i in alphabet_lower])
    conversion = [numbers.get(c) if c != ' ' else 0 for c in plaintext]
    return conversion


if __name__ == '__main__':
    main()
