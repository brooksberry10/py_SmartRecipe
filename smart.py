import csv

def update_ingredient_availability(filename):
    try:
        # Open the CSV file in read mode
        with open(filename, mode='r', newline='') as infile:
            reader = csv.reader(infile)
            header = next(reader)  # Read header row
            rows = [row for row in reader if len(row) == 7]  # Only keep rows with 7 columns

        # Print the list of ingredients for the user to choose from
        print("Ingredients List:")
        for index, row in enumerate(rows, start=1):
            print(f"{index}. {row[0]}")  # Print the ingredient name with its index
        
        # Ask the user to input the ingredient number they have
        user_input = input("\nEnter the number of the ingredient you have, or 'q' to quit: ")

        while user_input.lower() != 'q':
            try:
                # Convert the input to an integer (index of the ingredient)
                ingredient_number = int(user_input)
                
                if ingredient_number < 1 or ingredient_number > len(rows):
                    print(f"Invalid number. Please enter a number between 1 and {len(rows)}.")
                else:
                    # Mark the ingredient as available (1)
                    rows[ingredient_number - 1][6] = '1'  # Update the "Available" column

                    print(f"Updated {rows[ingredient_number - 1][0]} to available (1).")
                    
            except ValueError:
                print("Please enter a valid number.")
            
            # Ask again
            user_input = input("\nEnter the number of the ingredient you have, or 'q' to quit: ")

        # Save the updated data back to the CSV
        with open(filename, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)  # Write header row
            writer.writerows(rows)   # Write the updated ingredient rows
            
        print("CSV file updated successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Define the CSV filename
filename = 'ingredients.csv'

# Call the function to update ingredient availability
update_ingredient_availability(filename)
