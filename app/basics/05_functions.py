def greet(name):
    return f"Hello {name}"

def add(a, b):
    return a + b

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

def check_user(name, age):
    if name == "kevin" and age >= 18:
        return "Welcome Kevin, you are an adult"
    elif name == "kevin" and age < 18:
        return "Welcome Kevin, you are not an adult yet"
    else:
        return "Access denied"





# Test all functions above 

# greet function
print(greet("Kevin"))
print(greet("kevin"))

# add function
print(add(10, 5))

# is_adult function
print(is_adult(17))
print(is_adult(21))

# check_user function
name = input("Please enter your name: ").strip().lower()
age = int(input("Please enter your age: "))
print(check_user(name, age))