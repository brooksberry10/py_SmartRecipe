# ingredients.py
import csv

def load_ingredients(filename):
    """Loads ingredients from a CSV file and returns the header and list of rows."""
    try:
        with open(filename, mode='r', newline='') as infile:
            reader = csv.reader(infile)
            header = next(reader)  # Read header row
            rows = [row for row in reader if len(row) == 7]  # Only keep rows with 7 columns
        return header, rows
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None, None

def display_ingredients(rows):
    """Displays a list of ingredients to the user."""
    print("Ingredients List:")
    for index, row in enumerate(rows, start=1):
        print(f"{index}. {row[0]}")  # Print ingredient name with its index

def update_availability(rows, ingredient_number):
    """Marks the specified ingredient as available."""
    rows[ingredient_number - 1][6] = '1'  # Update the "Available" column
    print(f"Updated {rows[ingredient_number - 1][0]} to available (1).")

def save_ingredients(filename, header, rows):
    """Saves the updated ingredient list back to the CSV file."""
    with open(filename, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)  # Write header row
        writer.writerows(rows)   # Write the updated ingredient rows
    print("CSV file updated successfully.")