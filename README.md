# Lab 1: Grade Evaluator & Archiver

## Overview
This project is part of the African Leadership University Introduction to Python Programming and Databases lab.

It consists of:
- A Python program (`grade-evaluator.py`) that processes a CSV file of grades, validates inputs, calculates final scores, GPA, and determines pass/fail status.
- A Bash script (`organizer.sh`) that archives grade reports and maintains logs.

---

## Repository Contents
- `grade-evaluator.py` – Python script for processing grades
- `organizer.sh` – Bash script for archiving CSV files
- `README.md` – Documentation and usage instructions
- `grades.csv` – Input data file (used during execution)
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
Reads assignment data from a CSV file
Validates scores (must be between 0 and 100)
Validates weights (must total 100)
Ensures:
Formative assignments total 60%
Summative assignments total 40%
Calculates weighted total grade
Computes GPA using the formula:

 GPA = (Total Grade / 100) * 5.0


Determines pass/fail status:
A student must score at least 50% in BOTH Formative and Summative categories
Identifies failed formative assignments and suggests those eligible for resubmission (highest weight among failed items)

Evaluation Criteria Alignment
Robust Error Handling
The program gracefully handles:
Missing grades.csv file by displaying an error message and exiting without crashing.
Empty CSV files (such as those created by the organizer script) by detecting the absence of data and terminating gracefully with an error message.

Formula Accuracy
GPA is calculated using the correct formula:

 GPA = (Total Grade / 100) * 5.0


Pass/Fail logic strictly follows the requirement:
Passing requires at least 50% in Formative AND 50% in Summative categories.
Total grade alone is not sufficient to pass.
Weighted averages are correctly computed using assignment weights.

Correct Weight Tracking
The program enforces strict validation that:
Total weights across all assignments equal 100
Formative assignments sum to exactly 60
Summative assignments sum to exactly 40
If these conditions are not met, the program stops execution and displays an error.

Archival & Logging Implementation
The organizer.sh script correctly implements the archival process:
Creates an archive/ directory if it does not already exist
Generates a timestamp for file naming
Renames grades.csv using the timestamp format:
 grades_YYYYMMDD-HHMMSS.csv
Moves the renamed file into the archive/ directory
Creates a fresh empty grades.csv for future use
Logs each operation in organizer.log, including:
Timestamp
Original filename
Archived filename

Running the Organizer Script
Make the script executable:
chmod +x organizer.sh
Run the script:
./organizer.sh

Suggested Workflow
Enter or update grades in grades.csv
Run the Python evaluator to compute results
Run the organizer script to archive results
Repeat for new grading sessions

Notes
Ensure grades.csv is always in the project root directory
Do not manually modify files inside the archive/ folder
Use organizer.log to track all archival history 



