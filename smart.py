from ingredients import load_ingredients, display_ingredients, update_availability, save_ingredients
from showConfigMenu import load_user_preferences, save_user_preferences, select_preferences, reset_preferences
from displayFilterReipe import load_recipes, filter_recipes, display_filtered_recipes, MakeWeeklyPlan, displayWeeklyPlan
from resetIngredients import reset_ingredient_availability
from resetJson import reset_preferences_to_zero
from shoppingList import generate_shopping_list, display_shopping_list, save_shopping_list
import time

def main():
    filename = 'ingredients.csv'
    header, rows = load_ingredients(filename)
    
    if rows is None:
        return  # Exit if the file wasn't loaded correctly

    print("\nLoading ingredients...")
    time_control = 2
    time.sleep(time_control)
    # Display the ingredients list initially1
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



    # user preference configuration
    json_file = 'userConfigTemplate.json'
    preferences = load_user_preferences(json_file)
    if preferences is not None:
        # Allow user to select preferences
        proceed_to_pref = input("\nWould you like to select dietary preferences? (selecting n will skip and display all recipes) (y/n):")
        if proceed_to_pref.lower() == 'y':
            print("\nLoading user preferences...")
            time.sleep(time_control)

            user_pref = select_preferences(preferences)
            # Save updated preferences after selection
            save_user_preferences(json_file, user_pref)
            # Ask if they want to reset their selections
            # reset_choice = input("Do you want to reset your dietary preferences? (y/n): ")
            # if reset_choice.lower() == 'y':
            #     reset_preferences(preferences)
            #     save_user_preferences(json_file, preferences)
            # else:
            print('\nloading filtered recipe meal plan and shopping list...\n')
        else:
           # print('User selected to skip preferences. Loading full recipe list...\n')
            print("\nYou selected n. Meal plan will generate from full recipe list.")
            print("\nLoading meal plan and shopping list...\n")

    time.sleep(time_control)
    # Load the recipes from 'recipeDataBase.csv' and filter them based on the user's preferences
    recipes = load_recipes('recipeDataBase.csv')  # load from recipeDataBase.csv
    filtered_recipes = filter_recipes(preferences, recipes)  #filter recipes based on user preferences

    if not filtered_recipes:
        filtered_recipes = recipes

    weekPlan = MakeWeeklyPlan(filtered_recipes)
    displayWeeklyPlan(weekPlan)  # Display meal plan

    # Generate the shopping list
    shopping_list = generate_shopping_list(weekPlan, 'ingredients.csv')
    display_shopping_list(shopping_list)
    # Optionally save the shopping list to a file
    save_shopping_list(shopping_list)


# TO DO ####################chart####################################################################################
    #menu for nutritional goals
    #make weekly meal plan, accounting for nutritional goals, and using only filtered recipes
    #shopping lsit based on recipes used in meal plan and ingredients in inventory
    #pie chartchart


    reset_ingredient_availability(filename)
    reset_preferences_to_zero("userConfigTemplate.json")

if __name__ == '__main__':
    main()