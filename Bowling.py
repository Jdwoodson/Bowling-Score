'''
Created on Nov 8, 2016

@author: Justin
'''


def roll_string() -> str:
    """
    Input valid sequence of rolls for line of 10pin bowling
    """
    rolls = input("Please input string: ")
    return rolls


def line_decoder(roll_string) -> list:
    """
    Takes a string of rolls, and returns a list of two dictionaries.
    The first contains a total pin count for each roll.
    The second contains the status (Strike, Spare, Miss, Pins) for each frame.
    """
    pin_count = []
    frame_status = {}

    # Create numbered dicionary from the string
    for char in roll_string:
        pin_count.append(char)
    pin_count = dict(enumerate(pin_count, start=1))

    # Update Dictionaries for pin counts and frame status
    for key, value in pin_count.items():
        if value == 'X':
            pin_count[key] = 10
            frame_status[key] = 'Strike'

        elif value == '/':
            previous_pins = int(pin_count.get(key - 1))
            remaining_pins = 10 - previous_pins
            pin_count[key] = remaining_pins
            frame_status[key] = 'Spare'

        elif value == '-':
            pin_count[key] = 0
            frame_status[key] = 'Miss'

        else:
            pin_count[key] = int(value)
            frame_status[key] = 'Pins'

    return [pin_count, frame_status]


def get_score(pin_count, frame_status) -> int:
    """
    Takes Pin Count dictionary, Frame Status Dictionary
    Returns an int of the total pins over all 10 frames.
    """
    pin_total = []
    frame_count = 1
    ball_count = 0

    # Collect pin total
    for ball, status in frame_status.items():
        if status == 'Strike':
            if frame_count <= 10:                   # Until the 10th "frame",
                pin_total.append(pin_count[ball])   # Add pin totals for next
                # two balls, advance ball
                pin_total.append(pin_count[ball + 1])
                # count by two, and advance
                pin_total.append(pin_count[ball + 2])
                frame_count += 1                    # to next frame
                ball_count += 2

        elif status == 'Spare':
            if frame_count <= 10:                   # Until the 10th "frame",
                pin_total.append(pin_count[ball])   # Add pin totals for next
                # ball, advance ball count
                pin_total.append(pin_count[ball + 1])
                frame_count += 1                    # by one, advance frame
                ball_count += 1

        elif status == 'Miss' or 'Pins':
            if frame_count <= 10:
                pin_total.append(pin_count[ball])
                ball_count += 1                     # Advance ball count,
                if ball_count % 2 == 0:             # If second ball, advance
                    frame_count += 1                # frame

    total = sum(pin_total)
    return total


def main():
    rolls = roll_string()
    pins, frames = line_decoder(rolls)
    score = get_score(pins, frames)

    print("Total pins: %i" % score)

if __name__ == '__main__':
    main()
