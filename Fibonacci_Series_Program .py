# Fibonacci Series Program in Python

# This project demonstrates how to generate the Fibonacci series using Python and loops.

# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding numbers, starting from 0 and 1.



# Example Sequence
# 0 1 1 2 3 5 8 13 ...
# n=10
# a=0
# b=1
# for i in range(n):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c


n=int(input("Enter a number :"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
