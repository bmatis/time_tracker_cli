import sys

from timer import Timer
from log import Log
from settings import Settings
from goals import Goals
import common_functions as cf


def select_category(settings):
    """Ask the user to select a category from a given list."""
    # Loop for asking user to select a valid option.
    while True:
        cf.print_menu(settings.categories)
        selection = input("> ")

        try:
            category = settings.categories[int(selection) - 1]
            return category
        except IndexError:
            print("Please select a valid number.")
        except ValueError:
            print("Please select a valid number.")

def quit(log, settings):
    """Quit the program."""

    # Save categories to the file.
    settings.save_categories()

    # Exit program.
    sys.exit()

def run_timer(log, settings):
    """Run a timer."""
    # Create a new timer.
    timer = Timer()

    # Ask user for category to use and set timer to use it.
    print("\nWhat category is this timer for?")
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

    # Create settings, log, and goal objects.
    settings = Settings()
    log = Log(settings)
    goals = Goals()

    # Manu menu options
    main_menu = [
        "Start a new timer",
        "See current categories",
        "Add a new category",
        "View timer logs",
        "Show goal progress",
        "Quit"]

    while True:
        print("Please choose an option below:")
        print("-" * 30)
        cf.print_menu(main_menu)
        prompt = input("> ")

        if prompt == '1':
            # Start a new timer.
            run_timer(log, settings)
        elif prompt == '2':
            # See current categories.
            print("\n")
            cf.print_menu(settings.categories)
            cf.press_enter_to_continue()
        elif prompt == '3':
            # Add new category.
            print("What category would you like to add?")
            category = input("> ")
            settings.add_a_category(category)
        elif prompt == '4':
            # View the log.
            log.display(pretty=True)
            cf.press_enter_to_continue()
        elif prompt == '5':
            # Show the current progress towards programming goal.
            # Is only for testing purposes now. In future, change
            # to goal system.
            print("What category would you like to see the progress for?")
            category = select_category(settings)
            goal_progress_percent = goals.progress(log, category)
            print(category + ": %.2f percent" % goal_progress_percent)
            cf.press_enter_to_continue()
        elif prompt == '6':
            # Save and quit.
            quit(log, settings)
        else:
            print("Invalid input. Please respond with a valid menu option.")

main_loop()
