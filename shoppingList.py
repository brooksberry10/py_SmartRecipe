from ingredients import load_ingredients


def generate_shopping_list(mealPlan, ingredients_file):
    """
    Generate a shopping list of unavailable ingredients needed for the meal plan.

    Args:
        mealPlan (list): List of recipes in the weekly plan.
        ingredients_file (str): Path to the ingredients CSV file.

    Returns:
        set: A set of unavailable ingredients.
    """
    # Load ingredient availability from CSV
    _, ingredient_rows = load_ingredients(ingredients_file)

    # Create a dictionary for ingredient availability
    ingredient_availability = {row[0].strip().lower(): int(row[1]) for row in ingredient_rows}

    # Set to hold unique shopping list items
    shopping_list = set()

    # Extract ingredients from each recipe in the meal plan
    for recipe in mealPlan:
        recipe_ingredients = recipe['Ingredients'].split(', ')
        for ingredient in recipe_ingredients:
            # Add to shopping list if ingredient is unavailable
            if ingredient.strip().lower() in ingredient_availability and ingredient_availability[
                ingredient.strip().lower()] == 0:
                shopping_list.add(ingredient.strip())

    return shopping_list


def display_shopping_list(shopping_list):
    """
    Display the generated shopping list to the user.

    Args:
        shopping_list (set): Set of unavailable ingredients.
    """
    if shopping_list:
        print("\nShopping List:")
        for item in sorted(shopping_list):
            print(f"- {item}")
    else:
        print("\nAll ingredients for your meal plan are available!")


def save_shopping_list(shopping_list, filename='shopping_list.txt'):
    """
    Save the generated shopping list to a text file.

    Args:
        shopping_list (set): Set of unavailable ingredients.
        filename (str): Name of the file to save the shopping list.
    """
    with open(filename, 'w') as file:
        for item in sorted(shopping_list):
            file.write(f"{item}\n")
    print(f"\nShopping list saved to {filename}.")
