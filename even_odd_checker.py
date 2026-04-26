# This script demonstrates how to iterate through a list 
# and use conditional logic to identify even and odd numbers.

numbers = [10, 11, 15, 21]
for n in numbers:
    if n % 2 == 0:
        print("Even:", n)
    else:
        print("Odd:", n)
