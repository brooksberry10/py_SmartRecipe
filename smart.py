from ingredients import load_ingredients, display_ingredients, update_availability, save_ingredients

def main():
    filename = 'ingredients.csv'
    header, rows = load_ingredients(filename)
    
    if rows is None:
        return  # Exit if the file wasn't loaded correctly

    # Display the ingredients list initially
    display_ingredients(rows)

    # Ask the user to input the ingredient number they have
    user_input = input("\nEnter the number of the ingredient you have, or 'q' to quit: ")

    while user_input.lower() != 'q':
        try:
            # Convert the input to an integer (index of the ingredient)
            ingredient_number = int(user_input)
            
            if ingredient_number < 1 or ingredient_number > len(rows):
                print(f"Invalid number. Please enter a number between 1 and {len(rows)}.")
            else:
                # Update the ingredient availability
                update_availability(rows, ingredient_number)
                
                # Reprint the updated list
                display_ingredients(rows)
                
        except ValueError:
            print("Please enter a valid number.")
        
        # Ask again
        user_input = input("\nEnter the number of the ingredient you have, or 'q' to quit: ")

    # Save the updated ingredients back to the CSV file
    save_ingredients(filename, header, rows)

if __name__ == '__main__':
    main()