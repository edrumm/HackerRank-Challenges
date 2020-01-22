def grading_students(grades):
    rounded_grades = []

    for grade in grades:
        if grade >= 38 and grade % 5 >= 3:
            grade = ((grade + 4) // 5) * 5
            rounded_grades.append(grade)
        else:
            rounded_grades.append(grade)

    return rounded_grades
