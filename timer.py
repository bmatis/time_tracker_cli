from datetime import datetime

class Timer():
    """A class to represent a timer."""

    def __init__(self):
        self.start_time = ""
        self.end_time = ""
        self.duration = ""

    def set_category(self, category):
        """Set a category for the timer."""
        self.category = category
        print("Time will be tracked for category: " + self.category)

    def start(self):
        """Start the timer."""
        self.start_time = datetime.now()
        print("Timer started at: " + str(self.start_time))

    def stop(self):
        """End the timer."""
        self.end_time = datetime.now()
        self.duration = self.end_time - self.start_time
        print("Timer stopped at: " + str(self.end_time))

    def show_duration(self):
        """Display the duration."""
        print("\nTotal time elapsed: " + str(self.duration) + "\n")
