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