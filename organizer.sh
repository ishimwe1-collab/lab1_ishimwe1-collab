#!/bin/bash

ARCHIVE_DIR="archive"
LOG_FILE="organizer.log"
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
SOURCE_FILE="grades.csv"

# Create archive directory if it doesn't exist
if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir "$ARCHIVE_DIR"
fi

# Check if grades.csv exists
if [ ! -f "$SOURCE_FILE" ]; then
    echo "No grades.csv file found to archive."
    exit 1
fi

# New archived filename
NEW_NAME="grades_${TIMESTAMP}.csv"

# Move and rename file into archive
mv "$SOURCE_FILE" "$ARCHIVE_DIR/$NEW_NAME"

# Create a new empty grades.csv
 touch "$SOURCE_FILE"

# Log the operation
echo "[$TIMESTAMP] Archived $SOURCE_FILE as $NEW_NAME" >> "$LOG_FILE"

echo ""
echo "Done"
