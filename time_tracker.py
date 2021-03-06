#!/usr/local/bin/python3

import sys
from datetime import datetime, timedelta

from timer import Timer
from log import Log
from settings import Settings
from goals import Goals
from progress_bar import Progress_Bar
import common_functions as cf
import levels as levels


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

def view_level(log, settings):
    # Ask user what category to use
    print()
    header = "Show level for which category?"
    print(header + "\n" + "-" * len(header))
    category = cf.select_category(settings, allow_all=False)

    # if not category:
    #     return

    # Get the total time spent for the category
    cat_time = log.get_category_time_sum(category)

    # Convert total category time to an numeric value of hours, rounded
    # to 2 decimal places (i.e. like 1.5 hours instead of 1:30:00)
    cat_time_num = round(cat_time / timedelta (hours=1), 2)

    # Get a friendly looking string value for the category time
    cat_time_str = cf.formatted_time(cat_time)


    cur_level = levels.get_level(cat_time_num)
    next_level = levels.get_level(cat_time_num) + 1
    percent = levels.level_progress_percent(cat_time_num)
    cur_level_time = levels.time_per_level(cur_level)
    next_level_time = levels.time_per_level(next_level)

    main_label = category + " - Level " + str(cur_level) + " - " + cat_time_str
    left_label = str(percent) + "% to next level"
    right_label = "Level " + str(next_level) + " [" + str(next_level_time) + " Hours]"

    pb = Progress_Bar(width=52)
    pb.draw_full_progress_display(
        main_label, percent, left_label, right_label)
    cf.press_enter_to_continue()

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
        "See category levels",
        "Quit",
        ]

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
            # For testing the levels system
            view_level(log, settings)

        elif prompt == '10':
            # Save and quit.
            quit(log, settings, goals)

        else:
            print("\nInvalid input. Please respond with a valid menu option.")

main_loop()