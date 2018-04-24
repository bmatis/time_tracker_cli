from datetime import datetime, timedelta
import json
import csv

import common_functions as cf

class Log():
    """A class for handling the ongoing log of results."""

    def __init__(self, settings):
        """Initialize the log."""
        self.entries = []
        self.settings = settings
        self.log_file = settings.log_file
        self.get_log()

    def get_log(self):
        """Get the log entries from the saved log file."""
        try:
            with open(self.log_file) as f:
                reader = csv.reader(f)
                header_row = next(reader)

                for row in reader:
                    entry = self.get_log_entry(row)
                    self.entries.append(entry)
        except FileNotFoundError:
            # print("No log... Making a new one...\n")
            self.initialize_log()

    def initialize_log(self):
        """Create a new empty log file."""
        with open(self.log_file, 'w') as f:
            f.write("Start,End,Duration,Category\n")

    def get_log_entry(self, row):
        """Parse details from a row in the saved log file."""
        # Get the start time.
        start_time = cf.convert_str_to_datetime(row[0])

        # Get the end time. End time may be blank (for manual entries).
        if row[1] != "":
            end_time = cf.convert_str_to_datetime(row[1])
        else:
            end_time = ""

        # Get the duration
        duration = cf.convert_str_to_timedelta(row[2])

        # Get the category
        category = row[3]

        # Create dictionary for the log entry and return it.
        entry = self.create_entry(start_time, end_time, duration, category)
        return entry

    def create_entry(self, start_time, end_time, duration, category):
        """Create a dictionary object for an entry."""
        entry = {'start_time': start_time,
                 'end_time': end_time,
                 'duration': duration,
                 'category': category}
        return entry

    def add_to_log(self, timer):
        """Add a timer's results to the log."""
        # Get info from the timer and create a log entry dict.
        entry = self.create_entry(timer.start_time, timer.end_time,
            timer.duration, timer.category)

        # Append the log entry to the local entries list.
        self.entries.append(entry)

        # Save the log entry to the log file.
        self.save_entry(entry)

    def save_entry(self, entry):
        """Save an entry to the log file."""
        with open(self.log_file, 'a') as f:
            f.write(str(entry['start_time']) + "," +
                    str(entry['end_time']) + "," +
                    str(entry['duration']) + "," +
                    str(entry['category']) + "\n")

    def manual_entry(self):
        print("\nWhat category is this log for? ")
        category = cf.select_category(self.settings)

        # Get the date for the entry. Use this as the start time.
        start_time = cf.provide_date()

        # Have a blank end time, since we aren't really tracking a timer.
        end_time = ""

        # Get the duration for the entry.
        duration = cf.provide_time()

        entry = self.create_entry(start_time, end_time, duration, category)

        self.entries.append(entry)
        self.save_entry(entry)

    def display(self, pretty=False):
        """Print the log to the terminal."""
        print("\nLog:")
        print("-" * 30)

        if self.entries == []:
            print("Log is empty...")

        if pretty == False:
            print(self.entries)
        elif pretty == True:
            i = 1
            for entry in self.entries:
                print(str(i) + ". Start:    " + str(entry['start_time']) +
                    "\n   End:      " + str(entry['end_time']) +
                    "\n   Duration: " + str(entry['duration']) +
                    "\n   Category: " + entry['category'])
                i += 1

    def get_category_time_sum(self, category):
        """Adds up the sum of all time for a given category."""
        sum = timedelta(0)
        for entry in self.entries:
            if entry['category'] == category:
                sum += entry['duration']
        return sum

    def get_total_time_sum(self):
        """Adds up the sum of all time for everything in log."""
        sum = timedelta(0)
        for entry in self.entries:
            sum += entry['duration']
        return sum

    def save_log(self):
        """Save the entire log to a file."""
        with open(self.log_file, 'a') as f:
            for entry in self.entries:
                f.write(str(entry['start_time']) + "," +
                        str(entry['end_time']) + "," +
                        str(entry['duration']) + "," +
                        str(entry['category']) + "\n")
