#🟢 Problem 4: Grade Calculator using Function 🎓
def calculate_grade(marks):
    if marks > 100:
        return "invalid input"
    elif marks <= 100 and marks >= 80:
        return "A+"
    elif marks < 80 and marks >= 70:
        return "A"
    elif marks < 70 and marks >= 60:
        return "A-"
    elif marks < 60 and marks >= 50:
        return "B"
    elif marks < 50 and marks >= 40:
        return "C"
    else:
        return "F"
    

mark = int(input("Enter your marks: "))
grade = calculate_grade(mark)
print("Your grade is:", grade)