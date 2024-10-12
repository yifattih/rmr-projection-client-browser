import unittest
import numpy as np
from helpers.weight import WeightCalculator

class TestWeight(unittest.TestCase):

    def test_weight_time_range(self):
        """Should return a numpy array with time in weeks
        """
        weight_initial = 196
        multiplier = 2
        weeks = 6
        weight_calculator = WeightCalculator(w_i=weight_initial, a=multiplier,
                                             t=weeks)
        
        time_range_expected = np.array([0, 1, 2, 3, 4, 5, 6])
        time_range_actual = weight_calculator.time_range()
        
        for i in range(0, len(time_range_expected)):
            self.assertEqual(first=time_range_expected[i],
                             second=time_range_actual[i])

    def test_weight_loss_per_week(self):
        """Should return a numpy array with amount of weight lost per unit
        time (week)"""
        weight_initial = 196
        multiplier = 2
        weeks = 6
        weight_calculator = WeightCalculator(w_i=weight_initial, a=multiplier,
                                             t=weeks)
        w_r_expected = np.array([0, 2, 4, 6, 8, 10])
        w_r_actual = weight_calculator.weight_loss_rate()
        
        for i in range(0, len(w_r_expected)):
            self.assertEqual(first=w_r_expected[i], second=w_r_actual[i])

    def test_weight_in_time(self):
        """Should return a numpy array with the current weight calculated
        based on the weight loss rate"""
        weight_initial = 196
        multiplier = 2
        weeks = 6
        weight_calculator = WeightCalculator(w_i=weight_initial, a=multiplier,
                                             t=weeks)
        weight_calculator.weight_loss_rate()
        
        w_expected = np.array([196, 194, 192, 190, 188, 186])
        w_actual = weight_calculator.weight_change()
        
        for i in range(0, len(w_expected)):
            self.assertEqual(first=w_expected[i], second=w_actual[i])
