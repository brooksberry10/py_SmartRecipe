import csv

def reset_ingredient_availability(filename):
    try:
        # Open the CSV file in read mode
        with open(filename, mode='r', newline='') as infile:
            reader = csv.reader(infile)
            header = next(reader)  # Read header row
            rows = [row for row in reader if len(row) == 7]  # Only keep rows with 7 columns

        # Reset availability to 0 for all ingredients
        for row in rows:
            row[6] = '0'  # Reset availability to 0

        # Save the updated data back to the CSV
        with open(filename, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)  # Write header row
            writer.writerows(rows)   # Write the reset ingredient rows
            
        print("All ingredients have been reset to unavailable (0).")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Define the CSV filename
filename = 'ingredients.csv'

# Call the function to reset ingredient availability
reset_ingredient_availability(filename)