# Development Log

## v0.0.1

Initial working CLI version.

Features implemented:

- Add Student
- Find Student
- Quit Menu

Architecture:

- Modular folder structure
- Service layer for student operations
- CLI menu system
- In-memory dictionary storage

Notes:

- No persistence yet
- Validation system not implemented

## v0.0.2

Feature expansion version.

Features implemented:

- List Students
- Delete Student

Architecture:

- Modular folder structure preserved
- Service layer extended with new operations (list, delete)
- CLI menu system expanded with new options
- In-memory dictionary storage continues to be used

Notes:

- Data type inconsistency issue encountered during delete operation (string vs integer)
- Issue resolved by standardizing student IDs as strings
- No validation system implemented yet
- No persistence yet
