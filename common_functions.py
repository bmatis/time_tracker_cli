from datetime import datetime, timedelta

def print_menu(options, header=""):
    """Prints a numbered list of menu options."""
    if header != "":
        print(header)
        print("-" * len(header))
    i = 1
    for option in options:
        print(str(i) + ". " + option)
        i += 1

def convert_str_to_timedelta(time_str):
    """
    Take a string formatted timedelta and convert to timedelta object.
    Must be in format: 01:25:45.562416
    """
    # Get a datetime object from parsing the time string.
    try:
        t = datetime.strptime(time_str, "%H:%M:%S.%f")
    except ValueError:
        t = datetime.strptime(time_str, "%H:%M:%S")

    # Get a timedelta object from parsing the datetime object.
    td = timedelta(hours=t.hour, minutes=t.minute,
        seconds=t.second, microseconds=t.microsecond)
    return td

def convert_str_to_datetime(time_str):
    """
    Take a string formatted datetime and convert to datetime object.
    Must be in format: 2018-02-22 22:13:14.562416
    """
    # Get a datetime object from parsing the time string.
    try:
        t = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")
    except ValueError:
        t = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    return t

def formatted_time(time):
    """
    Present a timedelta in the format of "X hours Y minutes"
    """
    time_hours = int(time.total_seconds() // 3600)
    time_minutes = int(time.total_seconds() // 60 % 60)
    time_str = str(time_hours) + " hours"
    if time_minutes != 0:
        time_str += " " + str(time_minutes) + " mins"
    return time_str

def press_enter_to_continue():
    """Wait for the user to press enter to continue and tell them this."""
    input("\nPress enter to continue...")
    print("\n")

def select_category(settings, allow_all=False):
    """Ask the user to select a category from a given list."""

    while True:
        # Make a copy of the categories list so we can display it without
        # modifying it accidentally.
        categories = settings.categories[:]

        # Add an 'all' option if requested.
        if allow_all == True:
            categories.append("All")

        # Print the menu and wait for user response.
        print_menu(categories)
        selection = input("> ")

        # If user enters 'c', cancels the selection.
        if selection.lower() == 'c':
            return False

        # Check if user provided a valid response.
        # Provide error and try again if not.
        try:
            # Subtract one from user provided number, since menu starts at 1,
            # but the list index starts at 0.
            category = categories[int(selection) - 1]
            return category
        except IndexError:
            print("Please select a valid number.\n")
        except ValueError:
            print("Please select a valid number.\n")

def provide_date():
    """Ask the user to provide a date and convert it to a datetime object."""
    while True:
        date = input("Provide the date in format YYYY-MM-DD: ")
        try:
            date = datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid format, please try again.")
    return date

def provide_time():
    """Ask the user to provide a time (H:MM) and convert to a timedelta object."""
    while True:
        time = input("Provide the time in format HH:MM: ")
        try:
            time = datetime.strptime(time, "%H:%M")
            time = timedelta(hours=time.hour, minutes=time.minute)
            break
        except ValueError:
            print("Invalid format, please try again.")
    return time
