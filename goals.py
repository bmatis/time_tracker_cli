from datetime import datetime, timedelta
import common_functions as cf
import json


class Goals():
    """A class for defining and managing a goal."""
    def __init__(self, settings):
        # Get location of save file for the goals and then load the values.
        self.goals_file = settings.goals_file
        self.load_goals()

    def load_goals(self):
        """
        Loads the goals from the save file.
        """
        try:
            with open(self.goals_file) as f:
                self.goals = json.load(f)
        except FileNotFoundError:
            self.goals = {}
            self.save_goals()

    def get_category_goal(self, category):
        """
        Gets a goal time for a given category.
        """
        try:
            goal = timedelta(hours=self.goals[category])
        except:
            # If no goal value is set, set a default.
            goal = timedelta(hours=1)
        return goal

    def set_category_goal(self, category, goal):
        """
        Sets a goal time for a given category.
        """
        self.goals[category] = int(goal)
        self.save_goals()

    def save_goals(self):
        """
        Saves the goals to a file.
        """
        with open(self.goals_file, 'w') as f:
            json.dump(self.goals, f)

    def show_progress_bar(self, progress_percent, total_width=52):
        # Calculate the filled-in portion of the progress bar.
        bar_width = total_width - 2
        progress_width = round(progress_percent / 100 * bar_width)

        # If progress bar would be over 100%, set it to max of total width.
        if progress_width > bar_width:
            progress_width = bar_width

        # Calculate the empty portion of the progress bar.
        empty_width = bar_width - progress_width

        # Print out the progress bar.
        print("[" + "■" * progress_width + "-" * empty_width + "]")

    def show_detailed_progress(self, log, category):
        """
        Show a detailed progress bar for a given category's progress towards
        its goal.
        """
        time_spent = log.get_category_time_sum(category)
        goal_time = self.get_category_goal(category)
        self.draw_progress_display(category, time_spent, goal_time)

    def show_percent_of_total(self, log, category):
        """
        Show a detailed percentage bar for time in category compared to
        total of all time tracked.
        """
        category_time = log.get_category_time_sum(category)
        total_time = log.get_total_time_sum()
        self.draw_progress_display(category, category_time, total_time)

    def draw_progress_display(self, category, progress_time, end_time,
        width=52):
        try:
            progress_percent = progress_time / end_time * 100
        except ZeroDivisionError:
            progress_percent = 0

        # Print the category and its percent completion.
        print("\n" + category + ": %.2f%%" % progress_percent)

        # Generate and display the progress bar.
        self.show_progress_bar(progress_percent, width)

        # Show detailed breakdown of current time spent on goal and the
        # total time.
        time_spent_str = self.formatted_time(progress_time)
        total_time_str = self.formatted_time(end_time)
        padding = int(width/2)
        print(time_spent_str.ljust(padding) + total_time_str.rjust(padding))

    def formatted_time(self, time):
        """
        Present a timedelta in the format of "X hours Y minutes"
        """
        time_hours = int(time.total_seconds() // 3600)
        time_minutes = int(time.total_seconds() // 60 % 60)
        time_str = str(time_hours) + " hours"
        if time_minutes != 0:
            time_str += " " + str(time_minutes) + " minutes"
        return time_str

    def check_for_goal_completion(self, log, category):
        """
        Check if goal was met for a given category.
        """
        goal_time = self.get_category_goal(category)
        time_spent = log.get_category_time_sum(category)
        if (time_spent > goal_time):
            return True
        else:
            return False

    def goal_completion(self, log, category):
        """
        Handle goal completion.
        """
        goal_time = self.get_category_goal(category)

        print("\nCONGRATULATIONS!!!")
        print("*" * 18)
        print("You've hit your goal of %s spent on %s." %
            (self.formatted_time(goal_time), category))
        print("\nWould you like to provide a new goal? (y/n)")
        prompt = input("> ")
        if prompt == 'y':
            print("How many hours? Please provide an integer value.")
            hours = input("> ")
            self.set_category_goal(category, hours)
            print("The %s category has now been set to a %s hour goal." %
                (category, hours))
            self.show_detailed_progress(log, category)
        elif prompt == 'n':
            pass
