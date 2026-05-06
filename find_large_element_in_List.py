#  Find Largest Element in a List (Python)
#   Problem Statement

# Write a Python program to find the largest element
#  in a list without using built-in functions.

# 📊 Example

# Input:
# [10, 80, 70, 90, 20]
# Output:
# Largest element: 90

# ⚠️ Edge Case
# If the list is empty, 
# the program avoids errors using if arr: check.

# 🎯 Key Concepts
# Loops (for)
# Conditional statements (if)
# List handling
# Edge case handling

arr=[10,80,70,90,20]
largest=arr[0]
for num in arr:
   if num>largest:
      largest=num
print("Largest number :",largest)

#or 
# print(max(arr))

# arr = [10, 80, 70, 90, 20] 
# if arr: 
#    largest = arr[0] 
# for num in arr: 
#    if num > largest: 
#       largest = num 
#       print("Largest element:", largest) 
# else: print("List is empty")