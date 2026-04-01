name = "Kevin"

if name == "Kevin":
    print("This is Kevin")
elif name == "Kev":
    print("This is only Kev")
else:
    print("This is not Kevin")


name01 = "Kevin"
age = 17

if name01 == "Kevin" and age >= 18:
    print("Kevin is an adult")
elif name01 == "Kevin" and age < 18:
    print("Kevin is not an adult")
elif name01 != "Kevin" and age >= 18:
    print("Not Kevin, but an adult")
else:
    print("Not Kevin and not an adult")
