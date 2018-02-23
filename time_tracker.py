import sys

from timer import Timer
from log import Log
from settings import Settings

def select_category(settings):
    """Ask the user to select a category from a given list."""
    # Loop for asking user to select a valid option.
    while True:
        print("\nWhat category is this timer for?")
        print_menu(settings.categories)
        category = input("> ")

        try:
            category = settings.categories[int(category) - 1]
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

def run_timer(log, settings):
    """Run a timer."""
    # Create a new timer.
    timer = Timer()

    # Ask user for category to use and set timer to use it.
    category = select_category(settings)
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
            settings.save_categories()
            quit(log)
        elif prompt == 'y':
            run_timer(log, settings)
        else:
            print("Invalid input. Please respond with 'y' or 'n'.")

main_loop()
