# Membership:
# in       = inside
# not in   = not inside
#
# Identity:
# is       = same exact object
# is not   = not the same exact object

names = ["Kevin", "Maria"]
print("Kevin" in names)       # True
print("John" not in names)    # True

a = [1, 2]
b = [1, 2]
print(a == b)   # True  (same values)
print(a is b)   # False (different objects)
print(a is a)   # True
