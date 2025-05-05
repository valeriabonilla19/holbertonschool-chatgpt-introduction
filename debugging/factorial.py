#!/usr/bin/python3
import sys

#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # FIX: Decrement n to eventually exit loop
    return result

f = factorial(int(sys.argv[1]))
print(f)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <number>")
        sys.exit(1)
    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Factorial is not defined for negative numbers.")
            sys.exit(1)
        f = factorial(num)
        print(f)
    except ValueError:
        print("Please provide a valid integer.")
        sys.exit(1)
