import csv

def load_ingredients(filename):
    """Loads ingredients from a CSV file and returns the header and list of rows."""
    try:
        with open(filename, mode='r', newline='') as infile:
            reader = csv.reader(infile)
            header = next(reader)  # Read header row
            rows = [row for row in reader]  # Read all rows (no filtering needed)
        return header, rows
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None, None

def display_ingredients(rows):
    """Displays a list of ingredients to the user, including availability status."""
    print("\nIngredients List:")
    for index, row in enumerate(rows, start=1):
        availability = "Available" if row[1] == '1' else "Unavailable"
        print(f"{index}. {row[0]} - {availability}")  # Print ingredient name and its availability

def update_availability(rows, ingredient_number):
    """Marks the specified ingredient as available."""
    rows[ingredient_number - 1][1] = '1'  # Update the "Available" column to 1
    print(f"Updated {rows[ingredient_number - 1][0]} to available (1).")

def save_ingredients(filename, header, rows):
    """Saves the updated ingredient list back to the CSV file."""
    with open(filename, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)  # Write header row
        writer.writerows(rows)   # Write the updated ingredient rows
    print("CSV file updated successfully.")

def reset_ingredient_availability(filename):
    """Resets availability to 0 for all ingredients."""
    try:
        # Open the CSV file in read mode
        with open(filename, mode='r', newline='') as infile:
            reader = csv.reader(infile)
            header = next(reader)  # Read header row
            rows = [row for row in reader]  # Read all rows (no filtering needed)

        # Reset availability to 0 for all ingredients
        for row in rows:
            row[1] = '0'  # Reset availability to 0 (assuming availability is the second column)

        # Save the updated data back to the CSV
        with open(filename, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)  # Write header row
            writer.writerows(rows)   # Write the reset ingredient rows
            
        print("All ingredients have been reset to unavailable (0).")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")