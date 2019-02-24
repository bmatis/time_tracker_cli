from progress_bar import Progress_Bar

# A list for determining the hours needed for each level.
# Uses smaller gaps for low levels, up to a max of 200 hours.
# Hours needed for each additional level is determined by ONGOING_HOURS variable
LEVEL_HOURS = [0, 1, 2, 5, 10, 15, 25, 50, 75, 100, 150, 200]

# how many hours needed per level after the initial maximum set in LEVEL_HOURS
ONGOING_HOURS = 100


def get_level(time):
    """ Given an amount of time, will determine what level the skill is at. """

    # calculate level for times that are above what's explicitly defined in the
    # LEVEL_HOURS list
    level_hours_max = LEVEL_HOURS[-1]
    if time >= level_hours_max:
        return int(((time - level_hours_max) / ONGOING_HOURS) + len(LEVEL_HOURS))

    # for times within the LEVEL_HOURS list, use that to determine the level
    else:
        for level in range(len(LEVEL_HOURS)):
            if time < LEVEL_HOURS[level]:
                return level
            else:
                continue


def time_per_level(level):
    """
    Given a specific level number, return how many hours needed to hit it.
    """

    if level > len(LEVEL_HOURS):
        return ((level - len(LEVEL_HOURS)) * ONGOING_HOURS) + LEVEL_HOURS[-1]
    else:
        return LEVEL_HOURS[level-1]


def time_to_next_level(time):
    """
    Given an amount of time, determine what the next level is and how
    many more hours to get there.
    """

    next_level = get_level(time) + 1
    next_level_time = time_per_level(next_level)
    return next_level_time - time


def level_progress_percent(time):
    """
    Given an amount of time, will determine how far into the current level
    they are and returns that as a percentage, rounded to two decimal places.
    """
    current_level = get_level(time)
    next_level = current_level + 1

    current_level_start_time = time_per_level(current_level)
    next_level_start_time = time_per_level(next_level)
    total_time_gap = next_level_start_time - current_level_start_time
    time_progress = time - current_level_start_time

    # for testing - remove later!
    # print("Current level start time: " + str(current_level_start_time))
    # print("Next level start time: " + str(next_level_start_time))
    # print("Time gap: " + str(total_time_gap))
    # print("Time progess: " + str(time_progress))

    progress_percent = round((time_progress / total_time_gap * 100), 2)
    return progress_percent


# For in-progress testing
# time = float(input("How many hours? "))
#
# cur_level = get_level(time)
# next_level = get_level(time) + 1
# percent = level_progress_percent(time)
# cur_level_time = time_per_level(cur_level)
# next_level_time = time_per_level(next_level)
#
# print(str(time) + " hours is Level: " + str(cur_level))
# print("Total time needed to hit Level "+ str(next_level) + ": " + str(next_level_time))
# print("Which means the remaining hours to get there are: " + str(time_to_next_level(time)))
# print("Progress to next level: " + str(level_progress_percent(time)) + "%")
# print("")
#
# main_label = "Programming - Level " + str(cur_level) + " - " + str(time) + " Hours"
# left_label = "Level " + str(cur_level) + " [" + str(cur_level_time) + " Hours]"
# right_label = "Level " + str(next_level) + " [" + str(next_level_time) + " Hours]"
# pb = Progress_Bar()
# pb.draw_full_progress_display(main_label, percent, left_label, right_label)
# print("")

