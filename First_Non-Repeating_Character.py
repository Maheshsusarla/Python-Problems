# First Non-Repeating Character

# This problem is used to find the first character that appears only one time in a string.

# We check every character and count how many times it occurs.
# Then we traverse the string again to find the first character whose frequency is 1.

# This problem helps in understanding:

# Dictionaries (dict)
# Frequency counting
# Loops
# String traversal
# Conditional statements
# Example
# Input:  "aabbcdde"

# Output: "c"
# Explanation
# a appears 2 times
# b appears 2 times
# c appears 1 time ✅
# d appears 2 times
# e appears 1 time

# Even though e also appears once, c comes first in the string.
# So the output is:

# c


s="aabbcdde"
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
for ch in s:
    if d[ch]==1:
        print("First Non-Repeating Character:",ch)
        break
