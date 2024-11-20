
import json

def reset_preferences_to_zero(filename):
    """
    Resets all 'selected' fields in the JSON file to 0.
    :param filename: The path to the JSON file to reset.
    """
    try:
        # Read the JSON file
        with open(filename, 'r') as file:
            data = json.load(file)

        # Reset all dietary preferences 'selected' fields to 0
        for preference in data['dietary_preferences']['restrictions/preferences']:
            preference['selected'] = 0

        # Reset nutritional goals 'selected_goals' fields to 0
        for key in data['nutritional_goals']['selected_goals']:
            data['nutritional_goals']['selected_goals'][key] = 0

        # Reset meal calorie range 'selected_calories' fields to 0
        for key in data['meal_calorie_range']['selected_calories']:
            data['meal_calorie_range']['selected_calories'][key] = 0

        # Write the changes back to the JSON file
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        
        print("All preferences have been reset to 0.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
reset_preferences_to_zero("userConfigTemplate.json")