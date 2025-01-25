def calculate_sum(marks):
    return sum(marks)

def calculate_percentage(total_marks, max_marks):
    return (total_marks / max_marks) * 100

def determine_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    elif percentage >= 50:
        return 'E'
    else:
        return 'F'

def main():
    subjects = ['Computer Science', 'Maths', 'Physics', 'Sanskrit', 'Hindi']
    marks = []
    for subject in subjects:
        mark = float(input(f"Enter marks for {subject}: "))
        marks.append(mark)
    
    total_marks = calculate_sum(marks)
    max_marks = len(subjects) * 100
    percentage = calculate_percentage(total_marks, max_marks)
    grade = determine_grade(percentage)
    
    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

main()