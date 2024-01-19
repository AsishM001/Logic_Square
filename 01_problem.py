

def generateStudentMarkSheets(students, details):
    studentsMarkSheets = []
    for i in students:
        roll_number = i['Roll']
        student_details = None

        for j in details:
            if j['Roll'] == roll_number:
                student_details = j
                break  

        if student_details:
            marks = student_details['subjects']
            total_marks = sum(marks.values())
            status = "pass" if total_marks >= 200 else "fail"

            mark_sheet = {
                'name': i['name'],
                'Roll': roll_number,
                'math': marks.get('math', 0),
                'english': marks.get('english', 0),
                'chemistry': marks.get('chemistry', 0),
                'computer': marks.get('computer', 0),
                'total': total_marks,
                'status': status
            }

            studentsMarkSheets.append(mark_sheet)
    # return studentsMarkSheets
    for i in studentsMarkSheets:
        print("\n")
        print(i)

# Input data
students = [
    {"name": "Dhishan Debnath", "Roll": 1},
    {"name": "Animesh Gupta", "Roll": 2},
    {"name": "Tapas Sen", "Roll": 3},
    {"name": "Misti Dutta", "Roll": 4},
    {"name": "Chini Misra", "Roll": 5}
]

details = [
    {"Roll": 5, "subjects": {"math": 35, "english": 56, "chemistry": 76, "computer": 68}},
    {"Roll": 3, "subjects": {"math": 33, "chemistry": 12, "computer": 50, "english": 35}},
    {"Roll": 1, "subjects": {"math": 55, "english": 75, "chemistry": 76, "computer": 94}},
    {"Roll": 4, "subjects": {"english": 12, "chemistry": 85, "computer": 68, "math": 45}},
    {"Roll": 2, "subjects": {"math": 55, "english": 56, "computer": 48, "chemistry": 12}}
]

# Generate mark sheets
studentsMarkSheets = generateStudentMarkSheets(students, details)

# Output
# print(studentsMarkSheets)