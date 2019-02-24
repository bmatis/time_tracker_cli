class Progress_Bar():
    """A class for generating and displaying progress bars."""

    def __init__(self, width=52):
        self.total_width = width

    def draw_progress_bar(self, progress_percent):
        """
        input: number for indicating what percent complete to use
        output: Prints out just the progress bar portion for the given %.
        """

        bar_width = self.total_width - 2
        progress_width = round(progress_percent / 100 * bar_width)

        # If progress bar would be over 100%, set it to max of total width.
        if progress_width > bar_width:
            progress_width = bar_width

        # Calculate the empty portion of the progress bar.
        empty_width = bar_width - progress_width

        # Print out the progress bar.
        print("[" + "■" * progress_width + "-" * empty_width + "]")

    def draw_full_progress_display(
        self, main_label, percent, left_label, right_label):
        """
        inputs: a main label, what percent complete to draw, labels for the
                left and right sides at the bottom of the progerss bar.
        output: Prints out a detailed progress bar along with labels.
        """

        # Print the main label that appears above the bar
        print("\n" + main_label)

        # Generate and display the progress bar.
        self.draw_progress_bar(percent)

        # Display the labels along the bottom
        padding = int(self.total_width/2)
        print(left_label.ljust(padding) + right_label.rjust(padding))
