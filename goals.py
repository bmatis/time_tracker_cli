from datetime import datetime, timedelta
import common_functions as cf

class Goals():
    """A class for defining and managing a goal."""
    def __init__(self):
        # Hardcoding some values for now. Will eventually read these from
        # a save file.
        self.target_time = timedelta(hours=10)

    def progress(self, log, category):
        current_time = log.get_category_time_sum(category)
        progress = current_time / self.target_time * 100
        return progress
