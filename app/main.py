# Define a function named greet.
# A function is a reusable block of code.
def greet(name):
    # return sends a value back to whoever called the function.
    # f"..." is an f-string, which lets you insert variables directly into text.
    # Here, {name} gets replaced with the actual value passed in.
    return f"Hello, {name}"


# Define another function named main.
# main is often used as the program's starting function.
def main():
    # Call the greet function and pass in the string "Kevin".
    # greet("Kevin") returns "Hello, Kevin"
    # print(...) displays that returned value in the terminal.
    user_name = "Kevin"
    print(greet(user_name))


# __name__ is a special Python variable.
# When you run this file directly, Python sets __name__ to "__main__".
# This if statement checks whether this file is being run directly.
if __name__ == "__main__":
    # If true, call the main() function to start the program.
    main()