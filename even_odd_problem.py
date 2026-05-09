# Even or Odd Problem
# The Even or Odd problem is one of the basic programming problems used to determine whether a given number is even or odd.

# A number is called:
# Even if it is completely divisible by 2.
# Odd if it is not completely divisible by 2.

# To check this, we use the modulus operator %, which returns the remainder after division.
# If n % 2 == 0, the number is even.
# Otherwise, the number is odd.


num=int(input("Enter a number :"))
if num%2==0:
    print("Even")
else:
    print("Odd")


# def iseven(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# print(iseven(2))
# print(iseven(9))
# print(iseven(5))