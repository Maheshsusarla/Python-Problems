
# This project implements a program to check whether a given number
#  is a palindrome or not using pure integer logic (without converting the number into a string).

# A palindrome number is a number that remains the same when its digits are reversed.
# Examples:

# 121 → Palindrome ✅
# 123 → Not a palindrome ❌


word=input("Enter a any name :")
rev=""
for ch in word:
    rev=ch+rev
if word==rev:
    print(f" {rev} its a palindrome ")
else:
    print("I'ts not a palindrome")









# 📌 Palindrome Number Checker
# 📖 Description
# 🚀 Approach

# The program reverses the given number using mathematical operations:

# Extract the last digit using modulus %
# Build the reversed number by multiplying and adding digits
# Compare the reversed number with the original number
# 🧠 Algorithm
# Take an integer input from the user
# Store the original number in a temporary variable
# Initialize rev = 0
# Repeat until the number becomes 0:
# Extract last digit → digit = num % 10
# Update reversed number → rev = rev * 10 + digit
# Remove last digit → num = num // 10
# Compare original number with reversed number
# If equal → Palindrome, else → Not Palindrome
# num = 121
# temp = num
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10
# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not palindrome")