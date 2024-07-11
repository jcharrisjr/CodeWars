# Author: jcharrisjr
# Date: 2024-03-10
# License: MIT
# Exercise: Twice Linear (https://www.codewars.com/kata/5672682212c8ecf83e000050)
#
# This script provides a solution to the Twice Linear exercise on Codewars.
# The TwiceLinear function calculates the nth element in a sequence defined by
# specific rules, involving generating numbers based on the previous ones.
# The approach ensures efficiency in computing the sequence for large values of n.

def dbl_linear(n):
    u = [1]  # Initialize the sequence with the first element 1
    x_index, y_index = 0, 0  # Index pointers for 2 * x + 1 and 3 * x + 1 respectively

    for _ in range(n):
        next_x = 2 * u[x_index] + 1
        next_y = 3 * u[y_index] + 1

        if next_x <= next_y:
            u.append(next_x)
            x_index += 1
            if next_x == next_y:  # Avoid duplicate values
                y_index += 1
        else:
            u.append(next_y)
            y_index += 1

    return u[n]
