# An anagram problem means checking whether two words or strings contain the same
#  letters with the same frequency, but possibly in a different order.

# Example
# listen  -> silent

# Both contain:

# l → 1
# i → 1
# s → 1
# t → 1
# e → 1
# n → 1

# So they are anagrams.

# Examples
# Anagram
# "eat" and "tea"

# Both use same letters → ✅ Anagram

# Not Anagram
# "rat" and "car"

# Different letters → ❌ Not Anagram

s="listen"
t="silent"
if sorted(s)==sorted(t):
    print("this is a anagram ")
else:
    print("not an anagram")


s="listen"
t="silent"
f1={}
f2={}
for ch in s:
    f1[ch]=f1.get(ch,0)+1
for ch in t:
    f2[ch]=f2.get(ch,0)+1
if f1==f2:
    print("this is a anagram")
else:
    print("Not a anagram")




s=input("Enter a first name :").lower()
t=input("Enter a last name : ").lower()
f1={}
f2={}
for ch in s:
    f1[ch]=f1.get(ch,0)+1
for ch in t:
    f2[ch]=f2.get(ch,0)+1
if f1==f2:
    print("this is a anagram")
else:
    print("Not a anagram")