# main program

import sys
import argparse
import transform as tf


def parse_command_line():
    """Function to parse user input. User input is a float and a string.
    :Returns: radius of the circle (float) and which type of object is
    selected (string)."""
    parser = argparse.ArgumentParser(description="""Program to calculate side
        length of square (pentagon) containing the same area as circle with
        given radius. Provide input values. Check -h or --help for options.
        Usage: ./main.py square -r 4""")
    parser.add_argument("-r", "--radius", default=3.0, help="Radius of the \
        circle, in cm. \
        Default value: 3.0 cm")
    parser.add_argument("output", choices=["square", "pentagon"],
                        help="Choice of output object.")

    args = parser.parse_args()

    r = float(args.radius)
    l_output = args.output
    if l_output == "square":
        print("""Calculation of the side length of a square containing the
        same area as a selected circle.""")
        calc_square = True
    elif l_output == "pentagon":
        print("""Calculation of the side length of a pentagon containing the
            same area as a selected circle.""")
        calc_square = False
    else:
        sys.exit("No further output objects have been implemented \
            yet! Aborting...")

    return r, calc_square


if __name__ == "__main__":
    """Main function that drives the calculation."""
    # Get the input parameters
    r, calc_square = parse_command_line()
    # Calculate the area of the given circle
    ac = tf.area_circ(r)
    if calc_square:
        # Get the side length of the square with same area
        a_square = tf.side_square(ac)
    else:
        # Get the side length of the pentagon with same area
        a_pentagon = tf.side_pentagon(ac)
