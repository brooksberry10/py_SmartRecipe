import json


def load_user_preferences(filename):
    """Load user preferences from a JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None


def save_user_preferences(filename, preferences):
    """Save user preferences back to the JSON file."""
    with open(filename, 'w') as file:
        json.dump(preferences, file, indent=4)
    print("User preferences saved successfully.")


def select_preferences(preferences):
    """Display dietary preferences to the user and allow them to select options."""
    print("Select your dietary preferences:")
    for index, option in enumerate(preferences['dietary_preferences']['restrictions/preferences'], start=1):
        print(f"{index}. {option['name']}")

    user_selections = [0] * len(preferences['dietary_preferences']['restrictions/preferences'])

    while True:
        user_input = input("Enter the number of the preference you want to select (or 'q' to finish): ")
        if user_input.lower() == 'q':
            break
        try:
            choice = int(user_input) - 1
            if 0 <= choice < len(user_selections):
                user_selections[choice] = 1  # Set the flag to 1 for selected preference
                print(f"You selected: {preferences['dietary_preferences']['restrictions/preferences'][choice]['name']}")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    # Update preferences with user selections
    for i, flag in enumerate(user_selections):
        preferences['dietary_preferences']['restrictions/preferences'][i]['selected'] = flag

    return preferences


def reset_preferences(preferences):
    """Reset all dietary preferences to not selected."""
    for preference in preferences['dietary_preferences']['restrictions/preferences']:
        preference['selected'] = 0  # Reset selected flag to 0
    print("All dietary preferences have been reset to not selected.")



