def greet(name):
    return f"Hello {name}"

print(greet("Kevin"))



def greet(name):
    return f"Hello {name}"

def add(a, b):
    return a + b

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

print(greet("Kevin"))
print(add(10, 5))
print(is_adult(17))
print(is_adult(21))