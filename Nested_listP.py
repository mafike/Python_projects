# printing the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

if __name__ == '__main__':
    rec = []
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        name = input("Enter the name of the student: ")
        score = float(input("Enter the score of the student: "))
        rec.append([name, score])

    # Find the second lowest score 
    scores = set([student[1] for student in rec]) 
    # which is same to as: 
    # scores = []
    # for student in rec:
    #   scores.append[1]
    #  scores = set(scores)

    second_lowest_score = sorted(scores)[1]  
    #Get the names of students with the second lowest score
    students_with_second_lowest_score = [student[0] for student in rec if student[1] == second_lowest_score]  
    #sort the names alphabetically
    students_with_second_lowest_score.sort()
    #print the names on new lines
    for student_name in students_with_second_lowest_score:
        print(student_name)





        