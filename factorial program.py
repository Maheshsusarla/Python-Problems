# 📄 Factorial of a Number (Description)

# A factorial of a number is the product of all positive integers starting from that number down to 1. It is represented using an exclamation mark (!).

# For example, the factorial of a number n is written as n!

# 🔹 Definition:
# n!=n×(n−1)×(n−2)×...×2×1
# 🔹 Examples:

# 3! (3 factorial)
# = 3 × 2 × 1
# = 6

# 6! (6 factorial)
# = 6 × 5 × 4 × 3 × 2 × 1
# = 720

# 🔹 Special Case:
# 0! = 1 (by definition)


num=int(input("enter a number "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)