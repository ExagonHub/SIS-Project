from ui.menu import show_menu
from services.student_service import add_student, find_student

students = {}

def main():

    while True:
        
        show_menu()

        choice = input('Select Option:')

        if choice == '1':
            add_student(students)

        elif choice == '2':
            find_student(students)

        elif choice == '3':
            print('Exiting program..')
            break

        else:
            print('Invalid option')

if __name__ == '__main__':
    main()
