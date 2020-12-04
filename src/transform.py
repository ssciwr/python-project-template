#!/usr/bin/env python3
# Module containing the data transformation
import numpy as np


def area_circ(r_in):
    """Calculates the area of a circle with given radius.

    :Input: The radius of the circle (float, >=0).
    :Returns: The area of the circle (float)."""
    if r_in < 0:
        raise ValueError("The radius must be >= 0.")
    area_out = np.pi * r_in**2
    print("The area of a circle with radius r = {:3.2f}cm \
        is A = {:4.2f}cm2.".format(r_in, area_out))
    return area_out


def side_square(area_in):
    """Calculates the side length of a square given its radius.

    :Input: The area of the square (float, >=0).
    :Returns: The side length of the square (float)."""
    a_out = np.sqrt(area_in)
    print("The side length of a square with area = {:4.2f}cm2 \
        is a = {:3.8f}cm.".format(area_in, a_out))
    return a_out


def side_pentagon(area_in):
    """Calculates the side length of a pentagon given its radius.

    :Input: The area of the pentagon (float, >=0).
    :Returns: The side length of the pentagon (float)."""
    factor = 4.0 / np.sqrt(5.0*(5.0+2.0*np.sqrt(5.0)))
    a_out = np.sqrt(area_in * factor)
    print("The side length of a pentagon with area = {:4.2f}cm2 \
        is a = {:3.8f}cm.".format(area_in, a_out))
    return a_out
