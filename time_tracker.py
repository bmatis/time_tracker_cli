import sys

from timer import Timer
from log import Log
from settings import Settings
from goals import Goals
import common_functions as cf

def quit(log, settings):
    """Quit the program."""

    # Save categories to the file.
    settings.save_categories()

    # Exit program.
    sys.exit()

def run_timer(log, settings, goals):
    """Run a timer."""
    # Create a new timer.
    timer = Timer()

    # Ask user for category to use and set timer to use it.
    print("\nWhat category is this timer for?")
    category = cf.select_category(settings)
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

    # Show the current progress for the category.
    goals.show_detailed_progress(log, category)
    cf.press_enter_to_continue()

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
        "Manually enter a new record",
        "See current categories",
        "Add a new category",
        "View timer logs",
        "Show goal progress",
        "Status report",
        "Quit"]

    while True:
        print("Please choose an option below:")
        print("-" * 30)
        cf.print_menu(main_menu)
        prompt = input("> ")

        if prompt == '1':
            # Start a new timer.
            run_timer(log, settings, goals)
        elif prompt == '2':
            # Manually enter a new record
            log.manual_entry()
        elif prompt == '3':
            # See current categories.
            print("\n")
            cf.print_menu(settings.categories)
            cf.press_enter_to_continue()
        elif prompt == '4':
            # Add new category.
            print("What category would you like to add?")
            category = input("> ")
            settings.add_a_category(category)
        elif prompt == '5':
            # View the log.
            log.display(pretty=True)
            cf.press_enter_to_continue()
        elif prompt == '6':
            # Show the current progress towards a goal in a category.
            print("Show progress for which category?")
            category = cf.select_category(settings)
            goals.show_detailed_progress(log, category)
            cf.press_enter_to_continue()
        elif prompt == '7':
            # Show status report: progress info for all categories.
            for category in settings.categories:
                goals.show_detailed_progress(log, category)
            cf.press_enter_to_continue()
        elif prompt == '8':
            # Save and quit.
            quit(log, settings)
        else:
            print("Invalid input. Please respond with a valid menu option.")

main_loop()
