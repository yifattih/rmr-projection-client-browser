from .helpers.weight import WeightCalculator
from .helpers.equations import HarrisBenedictEqs


def calculate(weight_initial: float, height: float, age: int, time: int, multiplier = 2):
    weight_calculator = WeightCalculator(w_i=weight_initial, a=multiplier, t=time)
    time_range = weight_calculator.time_range()
    weight_change = weight_calculator.weight_change()
    bmr_calculator = HarrisBenedictEqs(w_change=weight_change, h=height, y=age)
    bmr = bmr_calculator.men()
    data = {"time": time_range, "weight": weight_change, "bmr": bmr}
    return data