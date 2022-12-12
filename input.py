import sys
import re

print("Enter numbers: ")

numbers = [int(x) for x in re.split(
    r'[\s]+|[\t]+|,', sys.stdin.read().strip()) if len(x) != 0]
print(numbers)
