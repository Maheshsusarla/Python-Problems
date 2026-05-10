# Swapping Two Variables

# Description

# A beginner-friendly Python program that swaps the values of two variables using multiple approaches. 
# This project demonstrates core programming concepts such as variable assignment, data manipulation, 
# and logic building. It includes methods with and without using a temporary variable, helping learners 
# understand efficient swapping techniques used in programming interviews and real-world applications.

# Input

# Two integer values provided by the user.


# Swapping Without Third Variable:

a = 10
b = 20
a, b = b, a
print("a =", a)
print("b =", b)


# Swapping Using Third Variable: 
a = 10
b = 20
temp = a
a = b
b = temp
print("a =", a)
print("b =", b)



# Swapping Using Addition and Subtraction

a = 10
b = 20
a = a + b
b = a - b
a = a - b
print(a)
print(b)

