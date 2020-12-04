#!/usr/bin/env python3
# main testing routine

import unittest
import numpy as np
import transform as tf


class test_area_circ(unittest.TestCase):
    def test_area_circ(self):
        """Test the area values against a reference for r >= 0."""
        self.assertAlmostEqual(tf.area_circ(1), np.pi)
        self.assertAlmostEqual(tf.area_circ(0), 0)
        self.assertAlmostEqual(tf.area_circ(2.1), np.pi*2.1**2)

    def test_values(self):
        """Make sure value errors are recognized for area_circ."""
        self.assertRaises(ValueError, tf.area_circ, -5)

    def test_side_square(self):
        """Test the computed side values for the square against a reference."""
        self.assertAlmostEqual(tf.side_square(np.pi), np.sqrt(np.pi))

    def test_side_pentagon(self):
        """Test the computed side values for the pentagon \
            against a reference."""
        self.assertAlmostEqual(tf.side_pentagon(np.pi), 1.35129587)
