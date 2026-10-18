employees = [
    {"name": "Kevin", "role": "developer", "salary": 95000},
    {"name": "Maria", "role": "tester", "salary": 75000},
    {"name": "John", "role": "developer", "salary": 98000},
    {"name": "Ashley", "role": "manager", "salary": 110000},
    {"name": "Chloe", "role": "tester", "salary": 72000},
]


# Return the names of everyone whose role matches.
# employee["role"] reads a value from a dictionary by its key.
def get_names_by_role(employees, role):
    return [employee["name"] for employee in employees if employee["role"] == role]


# Look up one employee's role by name. Returns None if not found.
def get_role(employees, name):
    for employee in employees:
        if employee["name"] == name:
            return employee["role"]
    return None


print(get_names_by_role(employees, "developer"))  # ['Kevin', 'John']
print(get_role(employees, "Kevin"))               # developer
print(get_role(employees, "Ashley"))              # manager
print(get_role(employees, "John"))                # developer
