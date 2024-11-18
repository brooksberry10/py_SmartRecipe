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

def displayWeeklyPlan(mealPlan):
    """Display the meal plan."""
    if mealPlan:
        print("\nWeekly Plan:")
        count = 0
        for recipe in mealPlan:
            count+= 1
            if count == 1:
                 print("\nSunday's meals:\n")
            elif count == 4:
                print("\nMonday's meals:\n")
            elif count == 7:
                 print("\nTuesday's meals:\n")  
            elif count == 10:
                print("\nWednesday's meals:\n")
            elif count == 13:
                 print("\nThursday's meals:\n")    
            elif count == 16:
                print("\nFriday's meals:\n")
            elif count == 19:
                 print("\nSaturday's meals:\n")                 
            print(f"- {recipe['Name']} (Calories: {recipe['Total Calories']}, Tags: {recipe['Dietary Tags']})")
            print(f"        Ingredients: {recipe['Ingredients']}\n")
    else:
        print("\nNo recipes found that match your preferences.")

    def makeShoppingList(mealPlan):
        for recipe in mealPlan:
            for ingredient in recipe['ingre']
def check_recipes_availability(recipes_list):
    #here I am making a dictionary to store ingredient availability
    ingredients_availability = {}
    with open('ingredients.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Ingredient Name'].strip().lower()
            available = int(row['Available'])
            ingredients_availability[name] = available

    #Set to store ingredients that are not available
    not_available_set = set()

    #this processes each recipe
    for recipe in recipes_list:
        ingredients = recipe['Ingredients']

        #putting the ingredients string into a list
        ingredients_list = [ing.strip().lower() for ing in ingredients.split(',')]

        #Check each ingredient
        for ingredient in ingredients_list:
            if ingredients_availability[ingredient] == 0:
                not_available_set.add(ingredient)

    #Print out the ingredients that are not available
    if not_available_set:
        print("This is your full Shopping List: ")
        for ingredient in sorted(not_available_set):
            print(f"{ingredient}")
    else:
        print("All ingredients are available.")
