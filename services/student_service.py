def add_student(students):

    student_id = input('Student ID:')
    name = input('Name:')
    last_name = input('Last name:')
    age = input('Age:')
    department = input('Department:')

    students[student_id] = {
        'name': name,
        'last_name': last_name,
        'age': age,
        'department': department
    }

    print('Student added successfully.')


def find_student(students):

    student_id = input('Enter Student ID:')

    if student_id in students:

        student = students[student_id]

        print('Student Found')
        print('Name:', student['name'])
        print('Last name:', student['last_name'])
        print('Age:', student['age'])
        print('Department:', student['department'])

    else:
        print('Student not found.')