import json

class Settings():
    """A class for storing common settings."""
    def __init__(self):
        """Initialize the settings."""

        # Save file locations
        self.log_file = 'log.csv'
        self.categories_file = 'categories.json'
        self.goals_file = 'goals.json'

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
        print("Examples: Cooking, Programming, Knife Throwing...\n\n")

        category = self.ask_user_for_category()
        self.add_a_category(category)

    def ask_user_for_category(self):
        """
        Ask user for a category. Provide error and try again if left blank.
        """
        print("What category would you like to add?")
        while True:
            category = input("> ")
            if category == "":
                print("Invalid category, please try again...\n")
            else:
                return category

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

    def delete_category(self, category):
        """Delete a category from the list."""
        if category in self.categories:
            print("Please confirm that you wish to delete category: " +
                category + " (y/n)")
            while True:
                confirm = input("> ")
                if confirm.lower() == 'y':
                    self.categories.remove(category)
                    print("Category: " + category + " has been removed.\n")
                    break
                elif confirm.lower() == 'n':
                    print("Ok, leaving it alone.\n")
                    break
                else:
                    print("Please provide a valid y/n response.")
        else:
            print("Error: that category is not available...")
