# Student Information System (SIS)

A modular command-line based Student Information System written in Python.

This project is being developed as a learning project to practice:

* modular programming
* software architecture
* CLI application design
* incremental software development

---

# Current Version

v0.0.1

---

# Features

Current system capabilities:

* Add Student
* Find Student
* Quit Application

Students are currently stored in memory using a Python dictionary.

---

# Project Structure

```
SIS-PROJECT/

core/
data/
models/
services/
ui/

docs/
tests/

main.py
README.md
requirements.txt
.gitignore
```

### Folder Description

**core/**
Core utilities and system-level modules.

**ui/**
User interface components such as CLI menus.

**services/**
Business logic for student operations.

**models/**
Data models used by the system.

**data/**
Storage layer for persistence (JSON will be added in future versions).

**docs/**
Project documentation including roadmap, devlog and known issues.

**tests/**
Unit tests (planned for future versions).

---

# Documentation

Additional documentation can be found in the `docs` folder:

* `docs/roadmap.md`
* `docs/devlog.md`
* `docs/known_issues.md`

---

# Roadmap

Future versions will include:

* student listing
* student deletion
* input validation
* JSON data persistence
* object-oriented data models
* automated tests

See the full roadmap in:

docs/roadmap.md

---

# Requirements

Python 3.x

No external libraries are required at this stage.

---

# Project Status

This project is under active development and is being expanded step-by-step as part of a learning process.
