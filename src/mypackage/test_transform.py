#!/usr/bin/env python3
# main testing routine

import numpy as np
import transform as tf
import pytest


@pytest.mark.parametrize(
    "myinput, myref", [(1, np.pi), (0, 0), (2.1, np.pi * 2.1**2)]
)
def test_area_circ(myinput, myref):
    assert tf.area_circ(myinput) == myref


def test_area_circ_values():
    """Make sure value errors are recognized for area_circ."""
    with pytest.raises(ValueError):
        tf.area_circ(-5)


def test_side_square():
    """Test the computed side values for the square against a reference."""
    assert tf.side_square(np.pi) == np.sqrt(np.pi)


def test_side_pentagon():
    """Test the computed side values for the pentagon against a reference."""
    assert tf.side_pentagon(np.pi) == pytest.approx(1.35129587)
