# Lab 1: Grade Evaluator & Archiver

## Overview
This project is part of the African Leadership University Introduction to Python Programming and Databases lab. It consists of:

- A Python program (`grade-evaluator.py`) that processes a CSV file of grades, validates inputs, calculates final scores, GPA, and determines pass/fail status.
- A Bash script (`organizer.sh`) that archives grade reports and maintains logs.

---

## Repository Contents
- `grade-evaluator.py` – Python script for processing grades
- `organizer.sh` – Bash script for archiving CSV files
- `grades.csv` – Input data file (generated/used by the program)
- `archive/` – Folder where archived CSV files are stored
- `organizer.log` – Log file tracking archive operations

---

## Requirements
- Python 3.8+
- Bash shell (Linux, macOS, or Git Bash on Windows)
- Write permissions in the project directory

---

## Running the Grade Evaluator
1. Open a terminal in the project directory.
2. Run the Python script:

```bash
python3 grade-evaluator.py

When prompted, enter the CSV filename (e.g., grades.csv).

What the Script Does
Validates that all scores are between 0 and 100
Ensures total weights equal 100
Ensures Formative = 60% and Summative = 40%
Calculates weighted total grade
Computes GPA using the formula:
GPA = (Total Grade / 100) * 5.0
Determines pass/fail status:
Must score at least 50% in both Formative and Summative
Suggests failed formative assignments eligible for resubmission

Running the Organizer Script
Make the script executable:
chmod +x organizer.sh

Run the script:
./organizer.sh


What the Organizer Does
Creates an archive/ directory if it does not exist
Renames grades.csv with a timestamp
Moves the renamed file into the archive folder
Creates a new empty grades.csv
Logs the operation in organizer.log

Suggested Workflow
Run grade-evaluator.py after entering or updating grades
Once done, run organizer.sh to archive the results
Repeat for new grading sessions

Notes
Ensure grades.csv is in the same directory as the scripts
Do not modify the archive manually
Always check organizer.log for archive history

