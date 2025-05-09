#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise ValueError("Missing argument. Usage: ./factorial.py <non-negative integer>")

        n = int(sys.argv[1])
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")

        print(factorial(n))

    except ValueError as e:
        print("Error:", e)
    except IndexError:
        print("Error: No input provided.")
