import csv

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
    else:
        print("\nNo recipes found that match your preferences.")
