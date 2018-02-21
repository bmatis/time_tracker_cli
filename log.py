from datetime import datetime
from datetime import timedelta

class Log():
    """A class for modeling an ongoing log of results."""

    def __init__(self):
        """Initialize the log."""
        self.entries = []

    def add_to_log(self, timer):
        """Add a timer's results to the ongoing log."""
        entry = {'start_time': timer.start_time,
                 'end_time': timer.end_time,
                 'duration': timer.duration,
                 'category': timer.category}
        self.entries.append(entry)

    def display(self):
        """Print the log to the terminal."""
        print(self.entries)

    def get_category_time_sum(self, category):
        """Adds up the sum of all time for a given category."""
        sum = timedelta(0)
        for entry in self.entries:
            if entry['category'] == category:
                sum += entry['duration']
        return sum
