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

    def manual_entry(self, goals):
        print("\nWhat category is this log for? ")
        category = cf.select_category(self.settings)

        if category:
            # Get the date for the entry. Use this as the start time.
            start_time = cf.provide_date()

            # Have a blank end time, since we aren't really tracking a timer.
            end_time = ""

            # Get the duration for the entry.
            duration = cf.provide_time()

            entry = self.create_entry(start_time, end_time, duration, category)

            self.entries.append(entry)
            self.save_entry(entry)

            print("\nAdded " + str(duration) + " to category: " + category)
            goals.show_detailed_progress(self, category)

            # Check if goal completed. If so, congratulate user and prompt for
            # new goal.
            if goals.check_for_goal_completion(self, category) == True:
                goals.goal_completion(self, category)
        else:
            print("Ok, cancelling.")

    def display(self, category='All', pretty=False):
        """Print the log to the terminal."""
        header = "Log | " + category
        print("\n" + header)
        print("-" * len(header))

        # Filter the entries based on the category provided.
        entries = []
        if category == 'All':
            entries = self.entries
        else:
            for entry in self.entries:
                if entry['category'] == category:
                    entries.append(entry)

        # Get the total count of entries and figure out the character length
        # of that number so we can leave the right amount of padding for it.
        entry_count = len(entries)
        padding = len(str(entry_count)) + 2

        if entries == []:
            print("Log is empty for category " + category + "...")

        if pretty == False:
            print(entries)
        elif pretty == True:
            i = 1
            for entry in entries:
                self.display_entry(entry, i, padding)
                i += 1

    def display_entry(self, entry, index, padding):
        index_str = (str(index) + ". ").rjust(padding)
        print(index_str + "Start:".ljust(10) +
            str(entry['start_time']))
        print(" " * padding + "End:".ljust(10) +
            str(entry['end_time']))
        print(" " * padding + "Duration:".ljust(10) +
            str(entry['duration']))
        print(" " * padding + "Category:".ljust(10) +
            str(entry['category']) + '\n')

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
        # for entry in self.entries:
        #     sum += entry['duration']
        for category in self.settings.categories:
            sum += self.get_category_time_sum(category)
        return sum

    def save_log(self):
        """Save the entire log to a file."""
        with open(self.log_file, 'a') as f:
            for entry in self.entries:
                f.write(str(entry['start_time']) + "," +
                        str(entry['end_time']) + "," +
                        str(entry['duration']) + "," +
                        str(entry['category']) + "\n")
