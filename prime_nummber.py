# Prime Number Problem

# A prime number is a natural number greater than 1 that has exactly two distinct positive divisors:
#  1 and itself. In other words, it is only divisible by 1 and the number itself.

# Problem Statement

# The goal of this program is to determine whether a given number is a prime number or not. 
# The program takes an integer input and checks its divisibility by all numbers from 2 up to the square root of the number. 
# If the number is divisible by any of these values, it is not prime; otherwise, it is a prime number.

# Example
# Input: 7 → Output: Prime
# Input: 10 → Output: Not Prime

num=int(input("Enter a number : "))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("Its not a prime number ")
            break
    else:
        print("Prime number")
else:
    print("invalid number")