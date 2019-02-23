#!/usr/local/bin/python3

import sys

from timer import Timer
from log import Log
from settings import Settings
from goals import Goals
from progress_bar import Progress_Bar
import common_functions as cf

def quit(log, settings, goals):
    """Quit the program."""

    # Save categories to the file.
    settings.save_categories()
    goals.save_goals()

    # Exit program.
    sys.exit()

def run_timer(log, settings, goals):
    """Run a timer."""
    # Create a new timer.
    timer = Timer()

    # Ask user for category to use and set timer to use it.
    print("\nWhat category is this timer for?")
    print("Select a number or 'c' to cancel.")
    category = cf.select_category(settings)
    if category:
        timer.set_category(category)

        # Prompt for starting the timer.
        response = input("\nPress enter to start timer, or 'c' to cancel. ")
        if response == 'c':
            print("Ok, timer cancelled.")
            return
        timer.start()

        # Prompt for stopping the timer.
        response = input("\nPress enter to stop timer, or 'c' to cancel. ")
        if response == 'c':
            print("Ok, timer cancelled.")
            return
        timer.stop()
        timer.show_duration()

        # Add timer results to the ongoing log.
        log.add_to_log(timer)

        # Show the current progress for the category.
        goals.show_detailed_progress(log, category)

        # Check if the goal was completed and prompt for new goal if so.
        if goals.check_for_goal_completion(log, category) == True:
            goals.goal_completion(log, category)
        cf.press_enter_to_continue()
    else:
        print("Ok, timer cancelled.")
        return

def category_menu(settings):
    """Display menu for handling category related features."""
    menu = ["See current categories",
            "Add a new category",
            "Delete a category",
            "Back to main menu",
            ]

    while True:
        print()
        header = "Category Manager | Please type a number:"
        cf.print_menu(menu, header)
        prompt = input("> ")

        if prompt == '1':
            # See current categories.
            print("\n")
            cf.print_menu(settings.categories, "Categories:")
            cf.press_enter_to_continue()

        elif prompt == '2':
            # Add new category.
            category = settings.ask_user_for_category()
            settings.add_a_category(category)

        elif prompt == '3':
            # Delete a category.
            print("\nWhich category do you want to delete?")
            print("Please type a number or 'c' to cancel.")
            category = cf.select_category(settings)
            if category:
                settings.delete_category(category)
            else:
                print("Ok, cancelled.")

        elif prompt == '4':
            break

        else:
            print("Invalid input. Please respond with a valid menu option.")

def view_log(log, settings):
    """
    Allow user to view the logs. Can select a specific category, or choose
    to show all of them.
    """
    print()
    header = "Show logs for which category?"
    print(header + "\n" + "-" * len(header))
    category = cf.select_category(settings, allow_all=True)

    if category:
        log.display(category=category, pretty=True)
        cf.press_enter_to_continue()
    else:
        return

def main_loop():
    """Main application loop."""

    print("\nWelcome to Time Tracker\n")

    # Create settings, log, and goal objects.
    settings = Settings()
    log = Log(settings)
    goals = Goals(settings)

    # Manu menu options
    main_menu = [
        "Start a new timer",
        "Manually enter a new record",
        "Manage categories",
        "View timer logs",
        "Show goal progress",
        "Status report",
        "Category breakdown",
        "Set a goal",
        "Quit",
        "TESTING: Generate Progress Bar"]

    while True:
        print()
        header = "Main Menu | Please type a number:"
        cf.print_menu(main_menu, header)
        prompt = input("> ")

        if prompt == '1':
            # Start a new timer.
            run_timer(log, settings, goals)

        elif prompt == '2':
            # Manually enter a new record
            log.manual_entry(goals)
            cf.press_enter_to_continue()

        elif prompt == '3':
            # Go to category submenu.
            category_menu(settings)

        elif prompt == '4':
            # View the log.
            view_log(log, settings)

        elif prompt == '5':
            # Show the current progress towards a goal in a category.
            print("\nShow progress for which category?")
            category = cf.select_category(settings)
            if category:
                goals.show_detailed_progress(log, category)
                cf.press_enter_to_continue()
            else:
                pass

        elif prompt == '6':
            # Show status report: progress info for all categories.
            for category in settings.categories:
                goals.show_detailed_progress(log, category)
            cf.press_enter_to_continue()

        elif prompt == '7':
            # Show category breakdown: time spent as % of total.
            for category in settings.categories:
                goals.show_percent_of_total(log, category)
            cf.press_enter_to_continue()

        elif prompt == '8':
            # Set a goal.
            print("\nSet a goal for which category?")
            category = cf.select_category(settings)
            if category:
                print("How many hours? Please provide an integer value.")
                hours = input("> ")
                goals.set_category_goal(category, hours)
                print("The %s category has now been set to a %s hour goal." %
                    (category, hours))

        elif prompt == '9':
            # Save and quit.
            quit(log, settings, goals)

        elif prompt == '10':
            # For testing the progress bar generation
            progress_bar = Progress_Bar(width=52)
            progress_bar.draw_full_progress_display(
                "Programming - Level 2",
                37,
                "2 hours 15 minutes ",
                "Level 3: 5 hours")

        else:
            print("Invalid input. Please respond with a valid menu option.")

main_loop()
