import array
import unittest
import pytest
import numpy as np
from helpers.equations import HarrisBenedict 

class TestEquationsHarrisBenedict(unittest.TestCase):
    def test_equations_harrisbenedict_str(self) -> None:
        age = 22
        height = 5.5
        time_projected = np.array([1, 2, 3])
        weight_initial = 10
        energy_deficit = 0
        harris_benedict = HarrisBenedict(age=age,
                                        height=height,
                                        time_projection=time_projected,
                                        weight_initial=weight_initial,
                                        energy_deficit=energy_deficit)
        str_expected = f"Harris-Benedict BMR equations for a {age}-years old person with {weight_initial}-lbs of weight and {height}-inches height. Projection over {time_projected}-weeks with an energy deficit of {energy_deficit}"
        str_actual = str(harris_benedict)
        self.assertEqual(str_expected, str_actual)

    def test_equations_harrisbenedict_repr(self) -> None:
        age = 22
        height = 5.5
        time_projected = np.array([1, 2, 3])
        weight_initial = 10
        energy_deficit = 0
        harris_benedict = HarrisBenedict(age=age,
                                        height=height,
                                        time_projection=time_projected,
                                        weight_initial=weight_initial,
                                        energy_deficit=energy_deficit)
        repr_expected = f"HarrisBenedict({age}, {height}, {weight_initial}, {time_projected}, {energy_deficit})"
        repr_actual = repr(harris_benedict)
        self.assertEqual(repr_expected, repr_actual)

    def test_equations_harrisbenedict_raises_assertion_age_less_19(self) -> None:
        age = 5
        height = 5.5
        time_projected = np.array([1, 2, 3])
        weight_initial = 10
        energy_deficit = 0
        with pytest.raises(AssertionError):    
            HarrisBenedict(age=age,
                           height=height,
                           time_projection=time_projected,
                           weight_initial=weight_initial,
                           energy_deficit=energy_deficit)

    def test_equations_harrisbenedict_raises_assertion_height_less_0(self) -> None:
        age = 22
        height = -10
        time_projected = np.array([1, 2, 3])
        weight_initial = np.array([100, 98, 88])
        energy_deficit = 0
        with pytest.raises(AssertionError):    
            HarrisBenedict(age=age,
                           height=height,
                           time_projection=time_projected,
                           weight_initial=weight_initial,
                           energy_deficit=energy_deficit)

    def test_equations_harrisbenedict_raises_assertion_time_empty(self) -> None:
        age = 22
        height = 5.5
        time_projected = np.array([])
        weight_initial = np.array([100, 98, 88])
        energy_deficit = 0
        with pytest.raises(AssertionError):    
            HarrisBenedict(age=age,
                           height=height,
                           time_projection=time_projected,
                           weight_initial=weight_initial,
                           energy_deficit=energy_deficit)

    def test_equations_harrisbenedict_raises_assertion_weight_negative(self) -> None:
        age = 22
        height = 5.5
        time_projected = np.array([1, 2, 3])
        weight_initial = -1
        energy_deficit = 0
        with pytest.raises(AssertionError):    
            HarrisBenedict(age=age,
                           height=height,
                           time_projection=time_projected,
                           weight_initial=weight_initial,
                           energy_deficit=energy_deficit)

    def test_equations_harrisbenedict_raises_assertion_energy_deficit_negative(self) -> None:
        age = 22
        height = 5.5
        time_projected = np.array([1, 2, 3])
        weight_initial = 10
        energy_deficit = -10
        with pytest.raises(AssertionError):    
            HarrisBenedict(age=age,
                           height=height,
                           time_projection=time_projected,
                           weight_initial=weight_initial,
                           energy_deficit=energy_deficit)

    def test_men_eq_in_pounds_return_valid_result(self) -> None:
        age = 33
        height = 71
        weight_initial = 196
        time_projected = np.array([0])
        harris_benedict = HarrisBenedict(age=age,
                                        height=height,
                                        weight_initial=weight_initial,
                                        time_projection=time_projected)
        bmr_expected, bmr_deficit_expected = (np.array([1968.13]),
                                                np.array([968.13]))
        (bmr_actual,
        bmr_deficit_actual) = np.round(harris_benedict.men_eq_in_pounds(), 2)
        for i in range(0, len(bmr_expected)):
            self.assertEqual(bmr_expected[i], bmr_actual[i])
            self.assertEqual(bmr_deficit_expected[i], bmr_deficit_actual[i])
