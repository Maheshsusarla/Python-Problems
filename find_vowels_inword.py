# Find Vowels in a Word Using Python
# Overview

# This Python program identifies and prints all vowels present in a given word. 
# It also demonstrates basic string traversal, conditional statements, and case-insensitive comparison.

# Objective
# To practice Python string handling and improve logical thinking by detecting vowels from user input.

#code 
text="mahesh"
count=0
for ch in text:
    if ch in 'aeiouAEIOU':
        count+=1
print(count)