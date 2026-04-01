import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists,
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")

    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    assignments = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })

        return assignments

    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)


def evaluate_grades(data):
    print("\n--- Processing Grades ---")

    if not data:
        print("Error: CSV file is empty.")
        sys.exit(1)

    total_weight = 0
    formative_weight = 0
    summative_weight = 0

    formative_score_total = 0
    summative_score_total = 0

    failed_formative = []

    for item in data:
        score = item['score']
        weight = item['weight']
        group = item['group']

        # Grade validation
        if score < 0 or score > 100:
            print(f"Invalid score detected: {score}")
            sys.exit(1)

        total_weight += weight

        if group.lower() == "formative":
            formative_weight += weight
            formative_score_total += (score * weight / 100)

            if score < 50:
                failed_formative.append(item)

        elif group.lower() == "summative":
            summative_weight += weight
            summative_score_total += (score * weight / 100)

    # Weight validation
    if total_weight != 100:
        print("Error: Total weight is not equal to 100.")
        sys.exit(1)

    if formative_weight != 60 or summative_weight != 40:
        print("Error: Formative must total 60 and Summative must total 40.")
        sys.exit(1)

    total_grade = formative_score_total + summative_score_total

    gpa = (total_grade / 100) * 5.0

    print(f"Formative Score: {formative_score_total:.2f}")
    print(f"Summative Score: {summative_score_total:.2f}")
    print(f"Total Grade: {total_grade:.2f}")
    print(f"GPA: {gpa:.2f}")

    # Pass/Fail decision
    formative_pass = formative_score_total >= 50
    summative_pass = summative_score_total >= 50

    if formative_pass and summative_pass:
        status = "PASSED"
    else:
        status = "FAILED"

    print(f"Final Status: {status}")

    # Resubmission logic
    if failed_formative:
        max_weight = max(item['weight'] for item in failed_formative)
        resubmissions = [item for item in failed_formative if item['weight'] == max_weight]

        print("\nResubmission Suggestions:")
        for item in resubmissions:
            print(f"- {item['assignment']} (Weight: {item['weight']}, Score: {item['score']})")


if __name__ == "__main__":
    course_data = load_csv_data()
    evaluate_grades(course_data)


