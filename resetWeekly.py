def reset_csv(filename):
    """Reset the CSV file by clearing its contents."""
    try:
        with open(filename, mode='w', newline='') as file:
            pass  # Just open and close the file to clear it
        print(f"The file '{filename}' has been reset.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")