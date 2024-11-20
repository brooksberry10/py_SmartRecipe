import csv
import random

def load_recipes(filename):
    """Load the recipes from a specified CSV file."""
    recipes = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                recipes.append(row)
        return recipes
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

def filter_recipes(preferences, recipes):
    """Filter the recipes based on the selected preferences."""
    selected_tags = []

    # Collect selected tags from preferences
    for pref in preferences['dietary_preferences']['restrictions/preferences']:
        if pref['selected'] == 1:
            selected_tags.append(pref['name'].lower())

    if not selected_tags:
        print("\nNo preference selected. Meal plan will generate from full recipe list.")
        return recipes

    # Filter recipes based on selected tags
    filtered_recipes = []
    for recipe in recipes:
        recipe_tags = recipe['Dietary Tags'].lower().split('; ')  # Split tags by semicolon
        if any(tag in recipe_tags for tag in selected_tags):
            filtered_recipes.append(recipe)

    return filtered_recipes

def display_filtered_recipes(filtered_recipes):
    """Display the filtered recipes."""
    if filtered_recipes:
        print("\nFiltered Recipes:")
        for recipe in filtered_recipes:
            print(f"- {recipe['Name']} (Calories: {recipe['Total Calories']}, Tags: {recipe['Dietary Tags']})")
            print(f"        Ingredients: {recipe['Ingredients']}\n")
    else:
        print("\nNo recipes found that match your preferences.")

def MakeWeeklyPlan(filtered_recipes):
    mealPlan = []
    if filtered_recipes:
        filteredCount = len(filtered_recipes) - 1
        for i in range(21):
            mealPlan.append(filtered_recipes[random.randint(0, filteredCount)])
    else:
        print("\nNo recipes in file.")
    return mealPlan

#THIS IS NEW
def save_weekly_plan_to_csv(mealPlan, filename="weekly_plan.csv"):
    """Save the weekly plan to a CSV file."""
    if mealPlan:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Day', 'Recipe Name', 'Calories', 'Tags'])  # CSV header

            days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            meal_count = 0

            for i, recipe in enumerate(mealPlan):
                day = days_of_week[meal_count % 7]  # Loop through the days of the week
                writer.writerow([day, recipe['Name'], recipe['Total Calories'], recipe['Dietary Tags']])
                meal_count += 1

        print(f"Weekly plan saved to '{filename}'")




def displayWeeklyPlan(mealPlan):
    """Display the meal plan."""
    if mealPlan:
        print("\nWeekly Plan:")
        count = 0
        mealFile = 'mealPlan.txt'
        with open(mealFile, 'w') as file:
            file.write("Weekly Plan:\n\n")  # Add a header to the file

            for recipe in mealPlan:
                count += 1
                if count == 1:
                    day_header = "\nSunday's meals:\n"
                elif count == 4:
                    day_header = "\nMonday's meals:\n"
                elif count == 7:
                    day_header = "\nTuesday's meals:\n"
                elif count == 10:
                    day_header = "\nWednesday's meals:\n"
                elif count == 13:
                    day_header = "\nThursday's meals:\n"
                elif count == 16:
                    day_header = "\nFriday's meals:\n"
                elif count == 19:
                    day_header = "\nSaturday's meals:\n"
                else:
                    day_header = None

                if day_header:
                    print(day_header)
                    file.write(day_header + "\n")  # Write day header to file

                meal_info = (
                    f"- {recipe['Name']} (Calories: {recipe['Total Calories']}, Tags: {recipe['Dietary Tags']})\n"
                    f"        Ingredients: {recipe['Ingredients']}\n")
                print(meal_info)
                file.write(meal_info + "\n")  # Write meal info to file


    else:
        print("\nNo recipes found that match your preferences.")