# Add Student

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

# Find Student

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

# List Student

def list_student(students):
    if not students:
        print('No students found.')
        return
    
    print('\n--- Student List ---')

    for student_id, student_info in students.items():
        print('Student ID: ',student_id)
        print('Student name: ',student_info['name'])
        print('Student Last Name: ',student_info['last_name'])
        print('Age: ',student_info['age'])
        print('Department: ',student_info['department'])
        print('----------------------')

# Delete Student

def delete_student(students):
    student_id = (input('Enter Student ID: '))

    if student_id in students:
        del students[student_id]
        print('Student deleted successfully.')
    else:
        print('Student not found.')