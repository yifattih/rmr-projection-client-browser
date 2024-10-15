import numpy as np

class HarrisBenedict:
    def __init__(self,
                age: int,
                height: float,
                time_projection: np.ndarray,
                weight_initial: float,
                weight_loss_rate: float=2,
                energy_deficit: float=1000) -> None:

        assert 19 <= age <= 150, ("Height stop chaning probalbly after 19"
                                "and normally people don't live more than "
                                "150 year!")
        assert height >= 0, "Height must be positive"
        assert time_projection.size != 0, ("Time projection is required. "
                                        "Calculate with the "
                                        "time_projection module")
        assert weight_initial >= 0, "Initial weight must be positive"
        assert energy_deficit >= 0, "Energy deficit must be positive"

        self.age = age
        self.height = height
        self.time_projection = time_projection
        self.weight_initial = weight_initial
        self.weight_loss_rate = weight_loss_rate
        self.energy_deficit = energy_deficit

    def men_eq_in_pounds(self) -> tuple[np.ndarray, np.ndarray]:
        bmr = (66.47
               + 6.24*(self.weight_initial
                       - (self.weight_loss_rate*self.time_projection))
               + 12.7*self.height
               - 6.76*self.age)
        bmr_deficit = bmr - self.energy_deficit
        return bmr, bmr_deficit
    
    def female_eq_in_pounds(self) -> tuple[np.ndarray, np.ndarray]:
        bmr = (65.51
               + 4.34*(self.weight_initial
                       - (self.weight_loss_rate*self.time_projection))
               + 4.7*(self.height)
               - 4.7*(self.age))
        bmr_deficit = bmr - self.energy_deficit
        return bmr, bmr_deficit

    def __str__(self) -> str:
        return (f"Harris-Benedict BMR equations for a {self.age}-years "
                f"old person with {self.weight_initial}-lbs of weight and "
                f"{self.height}-inches height. Projection over "
                f"{self.time_projection}-weeks with an energy deficit "
                f"of {self.energy_deficit}")
    
    def __repr__(self) -> str:
        return (f"HarrisBenedict({self.age}, {self.height}, "
                f"{self.weight_initial}, {self.time_projection}, "
                f"{self.energy_deficit})")
