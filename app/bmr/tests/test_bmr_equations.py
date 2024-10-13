import unittest
import numpy as np
from helpers.weight import WeightCalculator
from helpers.equations import HarrisBenedictEqs

class TestBasalMetabolicRate(unittest.TestCase):

    def test_men_bmr(self):
        """Should return a numpy array containing the basal metabolic rate
        for men"""
        w_initial = 196
        multiplier = 2
        weeks = 6
        height = 71  # inches
        age = 33  # years
        
        weight_calculator = WeightCalculator(w_i=w_initial, a=multiplier,
                                             t=weeks)
        w_change = weight_calculator.weight_change()
        
        bmr_calculator = HarrisBenedictEqs(w_change=w_change, h=height, y=age)
        
        w_chage_test = np.array([196, 194, 192, 190, 188, 186])
        bmr_expected = 66.47 + (6.24*w_chage_test) + (12.7*height) - (6.76*age)
        bmr_actual = bmr_calculator.men()
        
        for i in range(0, len(bmr_expected)):
            self.assertEqual(first=bmr_expected[i], second=bmr_actual[i])

    def test_women_bmr(self):
        """Should return a numpy array containing the basal metabolic rate
        for men"""
        w_initial = 196
        multiplier = 2
        weeks = 6
        height = 71  # inches
        age = 33  # years
        
        weight_calculator = WeightCalculator(w_i=w_initial, a=multiplier,
                                             t=weeks)
        w_change = weight_calculator.weight_change()
        
        bmr_calculator = HarrisBenedictEqs(w_change=w_change, h=height, y=age)
        
        w_chage_test = np.array([196, 194, 192, 190, 188, 186])
        bmr_expected = 65.51 + (4.34*w_chage_test) + (4.7*height) - (4.7*age)
        bmr_actual = bmr_calculator.women()
        
        for i in range(0, len(bmr_expected)):
            self.assertEqual(first=bmr_expected[i], second=bmr_actual[i])
        
        
        
