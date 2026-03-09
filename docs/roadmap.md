# SIS Project Roadmap

## Project Goal

Build a modular CLI-based Student Information System while learning software architecture step by step.

---

# Phase 1 — Core CLI System

## v0.0.1 — Initial Working System

Goal: Create a working CLI application.

Features:

* Add Student
* Find Student
* Quit

Technical Components:

* CLI menu system
* main program loop
* service layer for student operations
* in-memory dictionary data storage

Status: Completed

---

# Phase 2 — Basic Student Management

## v0.0.2 — Student Management Expansion

Goal: Expand student management capabilities.

New Features:

* List Students
* Delete Student

Menu Structure:

1 - Add Student
2 - Find Student
3 - List Students
4 - Delete Student
5 - Quit

New Functions:

* list_students()
* delete_student()

Concepts Practiced:

* dictionary iteration
* safe deletion
* handling empty collections

---

# Phase 3 — Validation and Quality

## v0.0.3 — Input Validation and Fixes

Goal: Improve system robustness.

Improvements:

* duplicate student ID control
* age input validation
* empty input control
* clearer error messages

Examples:

* "Student ID already exists"
* "Age must be a number"
* "Input cannot be empty"

Concepts Practiced:

* input validation
* defensive programming
* error handling

---

# Phase 4 — Student Update System

## v0.0.4 — Update Student

Goal: Allow editing existing student records.

New Feature:

* update_student()

Menu Structure:

1 - Add Student
2 - Find Student
3 - List Students
4 - Delete Student
5 - Update Student
6 - Quit

Concepts Practiced:

* dictionary updates
* editing existing data
* nested menu interactions

---

# Phase 5 — Data Persistence

## v0.1.0 — JSON Storage

Goal: Preserve data after program exit.

New System:

students.json

New Functions:

* load_students()
* save_students()

Program Flow:

Program Start:
JSON → Memory

Program Exit:
Memory → JSON

Concepts Practiced:

* JSON handling
* file operations
* persistence layer

---

# Phase 6 — Data Model Upgrade

## v0.2.0 — Student Class

Goal: Introduce object-oriented structure.

Example Model:

class Student:

```
def __init__(self, student_id, name, age, department):
    self.student_id = student_id
    self.name = name
    self.age = age
    self.department = department
```

Concepts Practiced:

* object oriented programming
* data modeling
* class-based design

---

# Phase 7 — Testing

## v0.3.0 — Unit Testing

Introduce automated tests.

New Folder:

tests/

Example Test File:

test_student_service.py

Concepts Practiced:

* pytest
* unit testing
* code reliability

---

# Phase 8 — CLI Improvements

## v0.4.0 — Better Command Line Interface

Goal: Improve user experience.

Improvements:

* screen clearing
* improved menu layout
* formatted table output

Example Output:

ID      NAME      AGE      DEPARTMENT
1001    Ali       20       Computer Engineering

Concepts Practiced:

* terminal formatting
* CLI usability

---

# Phase 9 — Advanced Features

## v1.0.0 — Complete CLI System

Advanced Features:

* search by name
* search by department
* student statistics
* total student count
* improved filtering

Goal: Final complete CLI Student Information System.

---

# Version Evolution

v0.0.1  Core CLI system
v0.0.2  Student management features
v0.0.3  Validation and bug fixes
v0.0.4  Student update system
v0.1.0  JSON persistence
v0.2.0  Object-oriented model
v0.3.0  Unit testing
v0.4.0  CLI improvements
v1.0.0  Complete system
