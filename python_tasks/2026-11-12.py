# Employee Management System
# use **kargs
# Requirements:
# Create an employee profile with dynamically provided details. 
# Employee details can include ID, name, age, department, salary, 
# 7 designation, and joining date.
# 1. Create an employee profile. (unique id)
# 2. Display all employee profiles.
# 3. Search and display an employee using their name.
# 4. Display employees department-wise.
# 5. Display employees with their ID.
# 6. Update using ID
# 7. Remove an employee profile using employee ID.  
# Store all employee profiles using a dictionary.


employee_details = {}
def employee_profile(id, **kwargs): #why can't I place id after **
    # **kwargs must come last because it collects the remaining keyword arguments.
    if id in employee_details:
        print("Employee ID already exists")
        return
    
    employee_details[id] = kwargs
    print("Employee Profile created Successfully")

def employee_display():
    if not employee_details:
        print("No Employees Found")
        return
    
    for eid,edetails in employee_details.items():
        print(eid, edetails)

def esearch_name(name):
    found=False
    for eid,edetails in employee_details.items():
        if edetails["name"].lower() == name.lower():
            print(eid, edetails)
            found=True
    if not found:
        print("Employee not found")

def display_dept(department):
    found = False
    for eid,edept in employee_details.items():
        if edept["department"].lower() == department.lower():
            print(eid, edept)
            found=True
    if not found:
        print("Employee not found")

def update_emp(id, **kwargs):
    if id not in employee_details:
        print("Employee doesn't exist")
        return

    if not kwargs:
        print(" No details provided")
        return

    employee_details[id].update(kwargs)

def remove_emp(id):
    if id in employee_details:
        del employee_details[id]
        print(f"Employee {id} details have been removed")
    else:
        print("Employee is not found")

employee_profile(101, name="Albin", age=23, department="IT", salary=25000)
employee_profile(102, name="Arun", age=25, department="HR", salary=30000)
employee_display()
print("\n")
esearch_name("Albin")
display_dept("HR")
print("\n")
update_emp(101, department="ISI")
employee_display()
print("\n")
remove_emp(102)
employee_display()

    