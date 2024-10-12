from helpers.weight import WeightCalculator
from helpers.equations import HarrisBenedictEqs
from helpers import user_inputs

weight_initial = 196        # pounds
height = 71                 # inches
age = 33                    # years
multiplier = 2              # pounds per week
time = 52                   # weeks
# 
weight_initial = user_inputs.get_weight()
height = user_inputs.get_height()
age = user_inputs.get_age()
time = user_inputs.get_time()
# 
weight_calculator = WeightCalculator(w_i=weight_initial, a=multiplier, t=time)
time_range = weight_calculator.time_range()
weight_change = weight_calculator.weight_change()
# 
bmr_calculator = HarrisBenedictEqs(w_change=weight_change, h=height, y=age)
bmr = bmr_calculator.men()
data = {"time": time_range, "weight": weight_change, "bmr": bmr}
# 
message = f"""This is the {time}-weeks Basal Metabolic Rate for a men of {age}
years old, with {height} inches of height, and an initial wieght
of {weight_initial} pounds"""
print(message, data)