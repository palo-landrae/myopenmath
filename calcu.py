import numpy as np
import statistics as st
import re
import sys
from colorama import init, Fore, Back, Style


def main():
    init()

    numbers = []

    if (menu() == 1):
        # numbers = [eval(i) for i in re.split(
        #   r'[\s]+|[\t]+|,', input("Enter Array: "))]
        print("\nEnter array: ")
        numbers = [eval(x) for x in re.split(
            r'[\s]+|[\t]+|,', sys.stdin.read().strip()) if len(x) != 0]
    elif (menu() == 2):
        numberOfElements = int(input("\nEnter number of elements: "))
        for _ in range(0, numberOfElements):
            number = int(input("\nEnter the number: "))
            frequency = int(input("Enter the frequency of %d: " % number))
            for _ in range(0, frequency):
                numbers.append(number)

    # convert to numpy array
    np_numbers = np.array(numbers)

    print_colorama(Fore.RED, "Sorted array:", sorted(numbers))
    print_colorama(Fore.GREEN, "\nMean:", np_numbers.mean())
    print_colorama(Fore.GREEN, "Median:", np.median(np_numbers))
    print_colorama(Fore.GREEN, "Mode:", st.multimode(np_numbers))
    print_colorama(Fore.GREEN, "Range:", find_range(numbers))

    print_colorama(Fore.MAGENTA, "\nSample Standard Deviation:",
                   np_numbers.std(ddof=1))
    print_colorama(Fore.MAGENTA, "Sample Variance:", np_numbers.var(ddof=1))
    print_colorama(Fore.CYAN, "Population Standard Deviation:",
                   np.std(np_numbers))
    print_colorama(Fore.CYAN, "Population Variance:", np.var(np_numbers))


def menu():
    print("1. Array: [0, 1, 2, 3, ...]")
    print("2. Individual numbers: 1x3, 2x4, 3x1, ...")
    choice = int(input("Enter input data structure: "))
    return choice


def print_colorama(color, message, value):
    #n_tabs = str(len(message) // 12)
    n_tabs = "\t" * (3 - len(message) // 12)
    value_to_print = "%0.3f" % value if type(
        value) != list else str(value)[1:-1]
    print(color + message + Style.RESET_ALL + n_tabs + value_to_print)


def find_range(numbers):
    range = max(numbers) - min(numbers)
    return range


if __name__ == "__main__":
    main()
