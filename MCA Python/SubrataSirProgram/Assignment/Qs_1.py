class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.total_marks = sum(marks)  # Calculate the total marks as the sum of the marks list

# Input section
all_students = []  # List to store all student objects
n = int(input("Enter the number of students: "))
count = 0

while count < n:
    name = input("Enter the name of the student: ")
    marks = list(map(int, input("Enter the marks in 4 subjects separated by spaces: ").split()))
    all_students.append(Student(name, marks))  # Create a Student object and add to the list
    count += 1

# Display total marks for each student
print("\nTotal marks of each student:")
for st in all_students:  # Changed to 'st' instead of 'student'
    print(f"{st.name}: {st.total_marks}")

# Find the highest total marks
highest_total = max(st.total_marks for st in all_students)  # Changed to 'st'

# Find students with the highest total marks
top_students = [st.name for st in all_students if st.total_marks == highest_total]  # Changed to 'st'

# Output section
print("\nThe student(s) with the highest total marks:")
for name in top_students:
    print(name)
