import csv


# EXTRACT
# This function reads data from a CSV file.
# file_path = where the CSV file lives
# return = gives back all rows from the CSV as a list of dictionaries
def extract(file_path):
    # Open the CSV file in read mode
    # newline="" prevents blank lines on Windows
    with open(file_path, "r", newline="") as file:
        # DictReader reads each row as a dictionary
        # Example:
        # {"name": "Kevin", "access": "granted"}
        reader = csv.DictReader(file)

        # Convert all rows into a list and return it
        return list(reader)


# TRANSFORM
# This function cleans or changes the data.
# rows = the raw rows read from the CSV
# return = cleaned rows
def transform(rows):
    # Create an empty list to hold cleaned rows
    cleaned_rows = []

    # Loop through every row from the CSV
    for row in rows:
        # Get the access value from the row
        # .strip() removes extra spaces
        # .lower() makes it lowercase
        access_value = row["access"].strip().lower()

        # Convert text to a cleaner standard value
        # If access says "granted", store True
        # If not, store False
        has_access = access_value == "granted"

        # Build a new cleaned row dictionary
        cleaned_row = {
            # Keep the name, but remove extra spaces
            "name": row["name"].strip(),

            # Keep original access text in clean lowercase form
            "access": access_value,

            # Add a new boolean-style field
            "has_access": has_access
        }

        # Add the cleaned row to the cleaned list
        cleaned_rows.append(cleaned_row)

    # Return all cleaned rows
    return cleaned_rows


# LOAD
# This function writes cleaned data into a new CSV file.
# file_path = where to save the new file
# data = cleaned rows to write
def load(file_path, data):
    # Open output CSV in write mode
    with open(file_path, "w", newline="") as file:
        # These are the column names for the new file
        fieldnames = ["name", "access", "has_access"]

        # DictWriter writes dictionaries into CSV rows
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header row first
        writer.writeheader()

        # Write all cleaned rows
        writer.writerows(data)


# MAIN
# This is the program starting point.
def main():
    # Input file = raw data
    input_file = "app/etl/input_access.csv"

    # Output file = cleaned data
    output_file = "app/etl/output_access.csv"

    # Step 1: Extract raw rows from CSV
    raw_rows = extract(input_file)

    # Step 2: Transform raw rows into cleaned rows
    cleaned_rows = transform(raw_rows)

    # Step 3: Load cleaned rows into a new CSV file
    load(output_file, cleaned_rows)

    # Print message so you know script finished
    print("ETL complete")


# Only run main() if this file is executed directly
if __name__ == "__main__":
    main()