#A program to print put the corresponding letter grade to their score.

def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

students = {}

while True:
    input_str = input("Type [name] [score] (press 'n' to quit): \n")
    if input_str == 'n':
        break
    name, score_str = input_str.split()
    score = int(score_str)
    letter_grade = get_letter_grade(score)
    students[name] = letter_grade

for name, letter_grade in students.items():
    print(name + "'s letter grade is:", letter_grade)
