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

    def display(self, pretty=False):
        """Print the log to the terminal."""
        print("\nLog:")
        print("-" * 50)
        if pretty == False:
            print(self.entries)
        elif pretty == True:
            i = 1
            for entry in self.entries:
                print(str(i) + ". Start:    " + str(entry['start_time']) +
                    "\n   End:      " + str(entry['end_time']) +
                    "\n   Duration: " + str(entry['duration']) +
                    "\n   Category: " + entry['category'] + "\n")
                i += 1

    def get_category_time_sum(self, category):
        """Adds up the sum of all time for a given category."""
        sum = timedelta(0)
        for entry in self.entries:
            if entry['category'] == category:
                sum += entry['duration']
        return sum
