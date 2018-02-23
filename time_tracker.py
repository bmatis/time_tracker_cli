import sys

from timer import Timer
from log import Log
from settings import Settings

def select_category():
    """Ask the user to select a category from a given list."""

    # Hardcoding a list of categories for now.
    categories = ['Programming', 'Reading', 'Running', 'Cooking']

    # Loop for asking user to select a valid option.
    while True:
        print("\nWhat category is this timer for?")
        print_menu(categories)
        category = input("> ")

        try:
            category = categories[int(category) - 1]
            return category
        except IndexError:
            print("Please select a valid number.")
        except ValueError:
            print("Please select a valid number.")

def print_menu(options):
    """Prints a numbered list of menu options."""
    i = 1
    for option in options:
        print(str(i) + ". " + option)
        i += 1

def quit(log):
    """Quit the program."""

    # For testing reasons, display the log and also a total summary of all
    # time spent on programming.
    log.display(pretty=True)
    print(log.get_category_time_sum('Programming'))

    # Append all results to the log file.
    log.save_log()

    # Make main loop inactive.
    sys.exit()

def main_loop():
    """Main application loop."""

    print("\nWelcome to Time Tracker\n")

    # Create settings object.
    settings = Settings()

    # Create object for the ongoing logging of results.
    log = Log(settings)

    while True:
        prompt = input("Would you like to start a new timer? (y/n) ").lower()

        if prompt == 'n':
            quit(log)
        elif prompt == 'y':
            # Create a new timer.
            timer = Timer()

            # Ask user for category to use and set timer to use it.
            category = select_category()
            timer.set_category(category)

            # Prompt for starting the timer.
            input("\nPress enter to start timer. ")
            timer.start()

            # Prompt for stopping the timer.
            input("\nPress enter to stop timer. ")
            timer.stop()
            timer.show_duration()

            # Add timer results to the ongoing log.
            log.add_to_log(timer)
        else:
            print("Invalid input. Please respond with 'y' or 'n'.")

main_loop()
