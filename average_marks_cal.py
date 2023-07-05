
n = int(input("Enter the number of students' records: "))
student_marks = {}

# Get student records
for _ in range(n):
    name, *line = input("Enter name and marks separated by space: ").split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input("Enter the name of the student to query: ")

# Calculate average marks for the query_name
if query_name in student_marks:
    marks = student_marks[query_name]
    average_marks = sum(marks) / len(marks)
    average_marks = round(average_marks, 2)  # Round to 2 decimal places
    print('{:.2f}'.format(average_marks))
else:
    print("No records found for the student:", query_name)


    
