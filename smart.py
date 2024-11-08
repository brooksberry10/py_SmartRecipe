# smart.py
from ingredients import load_ingredients, display_ingredients, update_availability, save_ingredients

def main():
    filename = 'ingredients.csv'
    header, rows = load_ingredients(filename)
    
    if rows is None:
        return  # Exit if the file wasn't loaded correctly

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
                
        except ValueError:
            print("Please enter a valid number.")
        
        # Ask again
        user_input = input("\nEnter the number of the ingredient you have, or 'q' to quit: ")

    save_ingredients(filename, header, rows)

if __name__ == '__main__':
    main()