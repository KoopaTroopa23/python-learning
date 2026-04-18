# range() — built in function

for i in range (1, 6):
    print("Number:", 1)


#        start at 1,  stop at 6,  go up by 1   
for i in range(1, 6, 1):
    print("Number:", i)  


hours = [35, 42, 45, 38, 50]
hourly_rate = 23
overtime_rate = hourly_rate * 1.5

def calculate_pay(h):
    if h <= 40:
        return h * hourly_rate
    else:
        regular = 40 * hourly_rate
        overtime = (h - 40) * overtime_rate
        return regular + overtime

for h in hours:
    print(f"{h} hours worked — Total pay: ${calculate_pay(h)}")




# for - starts the loop
# hours - variable that holds each item
# in - membership operator - go through each item
# names the list we looping through

for hours in hours:
    print(hours) 


users = [
    {"name": "Kevin", "role": "developer", "active": True},
    {"name": "Maria", "role": "tester", "active": False},
    {"name": "John", "role": "developer", "active": True},
    {"name": "Ashley", "role": "manager", "active": True},
    {"name": "Chloe", "role": "tester", "active": False}
]

def get_active_developers (users) :
    result = []                                     # empty list to collect results
    for user in users:                            # loop through each user
        if  user["role"] == "developer" and user["active"] == True:
            result.append(user)                       # add matching user to result
    return result 
print(get_active_developers(users))     




numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_even_numbers(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result

print(get_even_numbers(numbers))




x