import json

# Function to load the data from the JSON file
def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None

# Function to save the updated data back to the JSON file
def save_data(filename, data):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print("Changes have been saved.")
    except Exception as e:
        print(f"Error saving data: {e}")

# Function to display dietary preferences
def display_dietary_preferences(data):
    print("\nAvailable Dietary Preferences:")
    for index, pref in enumerate(data["dietary_preferences"]["restrictions/preferences"], 1):
        print(f"{index}. {pref}")
    
# Function to display nutritional goals
def display_nutritional_goals(data):
    print("\nAvailable Nutritional Goals:")
    print(f"1. Daily Calorie Goals: {data['nutritional_goals']['daily_calorie_goals']}")
    print(f"2. Protein Goals: {data['nutritional_goals']['protein_goals']}")
    print(f"3. Carb Goals: {data['nutritional_goals']['carb_goals']}")
    print(f"4. Fat Goals: {data['nutritional_goals']['fat_goals']}")

# Function to display meal calorie range
def display_meal_calorie_range(data):
    print("\nAvailable Meal Calorie Range:")
    print(f"1. Min Calories Options: {data['meal_calorie_range']['min_calories_options']}")
    print(f"2. Max Calories Options: {data['meal_calorie_range']['max_calories_options']}")

# Function to update the dietary preference
def update_dietary_preference(data):
    display_dietary_preferences(data)
    try:
        choice = int(input("\nEnter the number of the dietary preference you want to choose: "))
        if 1 <= choice <= len(data["dietary_preferences"]["restrictions/preferences"]):
            selected_preference = data["dietary_preferences"]["restrictions/preferences"][choice - 1]
            print(f"You selected: {selected_preference}")
        else:
            print("Invalid choice. Please select a valid option.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to update nutritional goals
def update_nutritional_goals(data):
    display_nutritional_goals(data)
    try:
        choice = int(input("\nEnter the number of the nutritional goal you want to update: "))
        if choice == 1:
            new_goal = int(input("Enter your new daily calorie goal: "))
            data["nutritional_goals"]["daily_calorie_goals"] = [new_goal]
            print(f"Updated daily calorie goal to: {new_goal}")
        elif choice == 2:
            new_goal = int(input("Enter your new protein goal: "))
            data["nutritional_goals"]["protein_goals"] = [new_goal]
            print(f"Updated protein goal to: {new_goal}")
        elif choice == 3:
            new_goal = int(input("Enter your new carb goal: "))
            data["nutritional_goals"]["carb_goals"] = [new_goal]
            print(f"Updated carb goal to: {new_goal}")
        elif choice == 4:
            new_goal = int(input("Enter your new fat goal: "))
            data["nutritional_goals"]["fat_goals"] = [new_goal]
            print(f"Updated fat goal to: {new_goal}")
        else:
            print("Invalid choice. Please select a valid option.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Function to update meal calorie range
def update_meal_calorie_range(data):
    display_meal_calorie_range(data)
    try:
        choice = int(input("\nEnter the number of the meal calorie range you want to update: "))
        if choice == 1:
            new_min_calories = int(input("Enter your new minimum calorie option: "))
            data["meal_calorie_range"]["min_calories_options"] = [new_min_calories]
            print(f"Updated minimum calorie option to: {new_min_calories}")
        elif choice == 2:
            new_max_calories = int(input("Enter your new maximum calorie option: "))
            data["meal_calorie_range"]["max_calories_options"] = [new_max_calories]
            print(f"Updated maximum calorie option to: {new_max_calories}")
        else:
            print("Invalid choice. Please select a valid option.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Function to display the menu and handle user input
def display_menu():
    data = load_data('userConfigTemplate.json')  # Load data from the JSON file
    
    if not data:
        return  # If there's an issue loading the data, stop the function
    
    while True:
        print("\n--- Menu ---")
        print("1. Update Dietary Preference")
        print("2. Update Nutritional Goals")
        print("3. Update Meal Calorie Range")
        print("4. Exit")
        
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                update_dietary_preference(data)
            elif choice == 2:
                update_nutritional_goals(data)
            elif choice == 3:
                update_meal_calorie_range(data)
            elif choice == 4:
                save_data('userConfigTemplate.json', data)  # Save changes before exiting
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

display_menu()
