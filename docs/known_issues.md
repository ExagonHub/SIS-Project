# Known Issues

This document lists currently known limitations or problems in the SIS project.

These issues are expected to be addressed in future versions.

---

## Current Issues

### Duplicate Student ID

The system currently allows adding multiple students with the same `student_id`.

Result:

* Existing student data may be overwritten.

Planned Fix:

* Add a validation check before inserting a new student.

Target Version:
v0.0.3

---

### Age Input Validation

The system does not currently validate the `age` field.

Possible Problems:

* Non-numeric values can be entered.
* Unrealistic age values may be stored.

Planned Fix:

* Ensure age input is numeric.
* Add basic range validation.

Target Version:
v0.0.3

---

### Empty Input Handling

The system does not prevent empty inputs for:

* student name
* department
* student ID

Planned Fix:

* Prevent empty strings during input.

Target Version:
v0.0.3

---

### Delete Confirmation Missing

The system allows direct deletion of students without any confirmation step.

Possible Problems:

* Users may accidentally delete the wrong student.
* Data loss risk increases.

Planned Fix:

* Add a confirmation step before deletion (e.g. "Are you sure?").

Target Version:
v0.0.3


