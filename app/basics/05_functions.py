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

def check_access (access):
    result = "Access Granted" if access == "granted" else "Access Denied"
    return result

def check_age (age):
    result = "Adult" if age >= 18 else "Minor"
    return result

def check_school (month) :
    result = "School is in session" if month in [9, 10, 11, 12, 1, 2, 3, 4, 5] else "School is out"
    return result

def call_name (name):
    return f"Hello {name}"

def add_numbers (c, d):
    return c + d

def even_odd (number):
   result = "Even" if number % 2 == 0 else "Odd"
   return result

def check_temperature (temp) :
    if (temp >= 80) :
        return "Hot"
    elif (temp <= 50) :
        return "Cold"
    else:
        return "Comfortable"



def get_letter_grade (score) :
    if (score >= 90) :
        return "A"
    elif (score >= 80) :
        return "B"
    elif (score >= 70) :
        return "C"
    elif (score >= 60) :
        return "D"
    else :
        return "F"







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

# check_access function
print(check_access("granted"))
print(check_access("denied"))
print(check_access("GRANTED"))
print(check_access("Granted"))

# check_age funciton
print(check_age(18))

# check_school function
print(check_school(1))

# call_name function
print(call_name("Kevin"))    

# add_numbers function
print(add_numbers(5, 10))

# even_odd function
print(even_odd(5))
print(even_odd(6))

# check_temperature
print(check_temperature(81))
print(check_temperature(49))
print(check_temperature(60))


# get_letter_grade
print(f"You grade is: {get_letter_grade(85)}")