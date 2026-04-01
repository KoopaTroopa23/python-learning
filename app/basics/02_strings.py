# Arithmetic: + - * / % ** //
# Comparison: == != > < >= <=
# Logical: and or not
# Assignment: = += -= *= /=
# Membership: in, not in
# Identity: is, is not

# Strings are sequences of characters
# They support indexing and slicing

# Indexing
word = "hello"

# Forward indexing (left to right)
# Index positions start at 0
print(word[0])  # h → first character
print(word[1])  # e
print(word[2])  # l
print(word[3])  # l
print(word[4])  # o → last character

print("-----")  # just prints a separator line

# Reverse indexing (right to left)
# -1 always means the LAST character
print(word[-1])  # o
print(word[-2])  # l
print(word[-3])  # l
print(word[-4])  # e
print(word[-5])  # h


# =========================
# SLICING
# =========================

# Slicing extracts a portion of a string
# Syntax: word[start : stop : step]
# stop index is NOT included

word = "hello"
print(word[1:4])   # starts at index 1, stops before index 4 → "ell"

print(word[:4])    # start defaults to 0 → "hell"
print(word[2:])    # goes from index 2 to the end → "llo"
print(word[:])     # entire string → "hello"


# =========================
# LENGTH OF STRING
# =========================

print(len('hello'))  # len() returns the number of characters → 5


# =========================
# STRINGS WITH QUOTES
# =========================

# Use double quotes if the string contains a single quote
print(" I'm going on a run ")


# =========================
# ESCAPE CHARACTERS
# =========================

# \n → newline (moves text to the next line)
print(' hello \n world ')

# \t → tab (adds horizontal spacing)
print(' hello \t world ')


# String Properties and Method
# Immutability

name = "Kevin"
#  name[1] = 'P'  # This will raise an error because strings are immutable

#String Concatenation

last_letters = name[1:]
print('P' + last_letters)  # 'P' + last_letters  # Concatenation to create a new string

x = "Hello World"
print(x + ', It is beutiful outside')
x = (x + ', It is beutiful outside')
print(x)

print(x.upper())  # Converts to uppercase

# x.   (tab produces a list of available methods in some IDEs)

print(x.split())  # Splits the string into a list of words

print(x.split('i'))

# String Interpolation    f-strings   String formatting

my_name = 'Kevin'
age = 45
print(f"My name is {my_name} and I am {age} yeard old.")
     
a = 24
b = 39
print(f"{a} + {b} = {a + b}")     
print(f"{a} sqaured {a ** 2}")

price = 20.23423
tax_rate = 0.04 
print(f"Price: ${price}")
print(f"The tax rate is 4% = {tax_rate} ")

##################################################################################################################

