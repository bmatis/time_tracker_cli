from datetime import datetime, timedelta
import common_functions as cf

class Goals():
    """A class for defining and managing a goal."""
    def __init__(self):
        # Hardcoding some values for now. Will eventually read these from
        # a save file.
        self.target_time = timedelta(hours=100)

    def progress(self, log, category):
        """Calculate and return the given categor's current goal progress."""
        current_time = log.get_category_time_sum(category)
        progress_percent = current_time / self.target_time * 100
        return progress_percent

    def show_progress_bar(self, progress_percent, total_width=50):
        # Calculate the filled-in portion of the progress bar.
        progress_bar_width = round(progress_percent / 100 * total_width)

        # If progress bar would be over 100%, set it to max of total width.
        if progress_bar_width > total_width:
            progress_bar_width = total_width

        # Calculate the empty portion of the progress bar.
        empty_width = total_width - progress_bar_width

        # Print out the progress bar.
        print("[" + "■" * progress_bar_width + "-" * empty_width + "]")
