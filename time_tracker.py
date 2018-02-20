from timer import Timer

def main_loop():
    """Main application loop."""

    print("\nWelcome to Time Tracker\n")

    active = True
    categories = ['Programming', 'Reading', 'Running', 'Cooking']

    while active:
        prompt = input("Would you like to start a new timer? (y/n) ").lower()

        if prompt == 'n':
            active = False
        elif prompt == 'y':
            # Create a new timer.
            timer = Timer(categories)
            timer.set_category()

            # Prompt for starting the timer.
            input("\nPress enter to start timer. ")
            timer.start()

            # Prompt for stopping the timer.
            input("\nPress enter to stop timer. ")
            timer.stop()
            timer.show_duration()
        else:
            print("Invalid input. Please respond with 'y' or 'n'.")

main_loop()
