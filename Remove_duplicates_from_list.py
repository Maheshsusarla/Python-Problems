# 📌 Problem Description: Remove Duplicates from a List

# In this problem, you are given a list of elements (numbers, strings, etc.), 
# and the goal is to remove all duplicate values so that each element appears only once in the final list.

# 🎯 Objective
# Take a list as input
# Return a new list (or modify the same list)
# Ensure no repeated elements




l=[10,20,30,40,50,10,20,30,40,50]
new=[]
for num in l:
    if num not in new:
        new.append(num)
print(new)