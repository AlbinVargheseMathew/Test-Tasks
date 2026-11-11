# Student Marks Management System
# Create a function called student_report() that:
# 1. Stores student names and their marks in a dictionary.
# 2. Calculates the average mark of each student.
# 3. Finds the student with the highest total marks.
# 4. Returns the topper's name and total marks as a tuple.
# 5. Displays students who scored above 80.

# Albin Average: 84.33
# John Average: 71.67
# Anu Average: 95.00
# David Average: 83.00

# Topper: Anu
# Total Marks: 285

# Students scoring above 80:
# Albin
# Anu
# David

students = {
    "Albin": [85, 90, 78],
    "John": [70, 65, 80],
    "Anu": [95, 92, 98],
    "David": [88, 76, 85]
}

def student_report(n)