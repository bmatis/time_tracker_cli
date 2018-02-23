import json

class Settings():
    """A class for storing common settings."""
    def __init__(self):
        """Initialize the settings."""

        # Save file locations
        self.log_file = 'log.csv'
        self.categories_file = 'categories.json'

        # Gets the saved category options.
        self.get_categories()

    def get_categories(self):
        """Get the saved categories from a file."""
        with open(self.categories_file) as f:
            self.categories = json.load(f)

    def save_categories(self):
        """Save the categories to a file."""
        with open(self.categories_file, 'w') as f:
            json.dump(self.categories, f)

    def add_a_category(self, category):
        """Add a category to the available options."""
        self.categories.append(category)
        print("Category '" + category + "' has been added.\n")
