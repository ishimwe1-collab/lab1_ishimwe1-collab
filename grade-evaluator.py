import csv
import sys
import os


def load_csv_data():
    """
    Prompts the user for a filename, validates it, and loads CSV data.
    Includes robust error handling and Ctrl+C handling.
    """

    while True:
        try:
            filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ").strip()

            # Ensure file extension is included
            if not filename.endswith(".csv"):
                print("⚠️ Please include the file extension (e.g., grades.csv).")
                continue

            # Check if file exists
            if not os.path.exists(filename):
                print(f"❌ Error: The file '{filename}' was not found.")
                continue

            assignments = []

            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                # Handle empty file
                if reader.fieldnames is None:
                    print("❌ Error: The CSV file is empty.")
                    sys.exit(1)

                for row in reader:
                    try:
                        assignments.append({
                            'assignment': row['assignment'],
                            'group': row['group'],
                            'score': float(row['score']),
                            'weight': float(row['weight'])
                        })
                    except (TypeError, ValueError):
                        print("❌ Error: Invalid data in CSV file.")
                        sys.exit(1)

            return assignments

        except KeyboardInterrupt:
            print("\n⚠️ Ctrl + C detected.")
            choice = input("Do you really want to quit? (y/n): ").strip().lower()

            if choice == 'y':
                print("Exiting safely...")
                sys.exit(0)
            else:
                print("Resuming...\n")
                continue

        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            continue


def evaluate_grades(data):
    print("\n--- Processing Grades ---")

    formative_total_weight = 0
    summative_total_weight = 0

    formative_scores = []
    summative_scores = []

    formative_failed = []

    # Validate scores and split data
    for item in data:
        score = item['score']
        weight = item['weight']
        group = item['group']

        # Validate score range
        if score < 0 or score > 100:
            print(f"❌ Invalid score for {item['assignment']}: {score}")
            sys.exit(1)

        if group.lower() == "formative":
            formative_total_weight += weight
            formative_scores.append((score, weight))

            if score < 50:
                formative_failed.append(item)

        elif group.lower() == "summative":
            summative_total_weight += weight
            summative_scores.append((score, weight))

    # Validate weights
    total_weight = formative_total_weight + summative_total_weight

    if total_weight != 100:
        print(f"❌ Total weight must equal 100. Current total: {total_weight}")
        sys.exit(1)

    if formative_total_weight != 60:
        print(f"❌ Formative weights must total 60. Current: {formative_total_weight}")
        sys.exit(1)

    if summative_total_weight != 40:
        print(f"❌ Summative weights must total 40. Current: {summative_total_weight}")
        sys.exit(1)

    # Calculate weighted averages
    formative_grade = sum(score * weight for score, weight in formative_scores) / formative_total_weight
    summative_grade = sum(score * weight for score, weight in summative_scores) / summative_total_weight

    total_grade = (formative_grade * 0.6) + (summative_grade * 0.4)

    # GPA calculation
    gpa = (total_grade / 100) * 5.0

    # Pass/Fail
    formative_pass = formative_grade >= 50
    summative_pass = summative_grade >= 50

    status = "PASSED" if formative_pass and summative_pass else "FAILED"

    # Resubmission logic
    resubmissions = []
    if not formative_pass:
        if formative_failed:
            max_weight = max(item['weight'] for item in formative_failed)
            resubmissions = [item for item in formative_failed if item['weight'] == max_weight]

    # Output results
    print(f"\nFormative Average: {formative_grade:.2f}%")
    print(f"Summative Average: {summative_grade:.2f}%")
    print(f"Total Grade: {total_grade:.2f}%")
    print(f"GPA: {gpa:.2f}")
    print(f"Status: {status}")

    if resubmissions:
        print("\nAssignments eligible for resubmission:")
        for item in resubmissions:
            print(f"- {item['assignment']} (Weight: {item['weight']}, Score: {item['score']})")


if __name__ == "__main__":
    course_data = load_csv_data()
    evaluate_grades(course_data)
