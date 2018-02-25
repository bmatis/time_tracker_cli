from datetime import datetime, timedelta

def print_menu(options):
    """Prints a numbered list of menu options."""
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
    t = datetime.strptime(time_str, "%H:%M:%S.%f")

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
    t = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")
    return t

def press_enter_to_continue():
    """Wait for the user to press enter to continue and tell them this."""
    input("\nPress enter to continue...")
    print("\n")
