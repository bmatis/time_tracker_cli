from datetime import datetime, timedelta
import common_functions as cf

class Goals():
    """A class for defining and managing a goal."""
    def __init__(self):
        # Hardcoding some values for now. Will eventually read these from
        # a save file.
        self.target_time = timedelta(hours=100)

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
        goal_time = self.target_time
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
