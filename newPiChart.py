import csv
import matplotlib.pyplot as plt
from collections import Counter

def load_csv(filename):
    """Load the CSV and extract tags from the 'Tags' column."""
    tags = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Split tags by semicolon and add to the list
                recipe_tags = row['Tags'].lower().split('; ')
                tags.extend(recipe_tags)
        return tags
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

def count_tags(tags):
    """Count the frequency of each tag from the list."""
    return Counter(tags)

def plot_pie_chart(tag_counts):
    """Create a pie chart based on tag counts."""
    labels = tag_counts.keys()
    sizes = tag_counts.values()
    
    # Create the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Dietary Preferences Distribution")
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is drawn as a circle.
    plt.show()