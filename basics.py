# Datatypes

name = "Dhanusya"
age = 22
height = 5.4
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

# String

department = "Artificial Intelligence & Data Science"

print(department.upper())
print(department.lower())
print(len(department))

# If Condition

attendance = 78

if attendance >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")

# For Loop

print("For Loop")

for i in range(1, 6):
    print("Semester", i)

# While Loop

print("While Loop")

week = 1

while week <= 5:
    print("Week", week)
    week += 1

# Function

def welcome():
    print("Welcome to Programming")

welcome()

# List

subjects = ["Python", "Java", "Database"]

for subject in subjects:
    print(subject)