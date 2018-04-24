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
        try:
            with open(self.categories_file) as f:
                self.categories = json.load(f)
        except FileNotFoundError:
            self.categories = []
            self.initialize_categories()

    def initialize_categories(self):
        """Create categories save file and ask user to make their first one."""
        print("Looks like this is your first time using Time Tracker.")
        print("To get started, please create the first category you'd like to track.")
        print("Examples: Cooking, Programming, Knife Throwing...")
        while True:
            category = input("> ")
            if category == "":
                print("Invalid category, please try again...\n")
            else:
                break

        self.add_a_category(category)

    def save_categories(self):
        """Save the categories to a file."""
        with open(self.categories_file, 'w') as f:
            json.dump(self.categories, f)

    def add_a_category(self, category):
        """Add a category to the available options."""

        # Check if category already exists. Convert everything to lower
        # case to be case insensitive.
        if category.lower() not in (c.lower() for c in self.categories):
            self.categories.append(category)
            print("Category '" + category + "' has been added.\n")
        else:
            print("Category '" + category + "' already exists.\n")
