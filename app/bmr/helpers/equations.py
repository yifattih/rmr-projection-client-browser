import numpy as np

class HarrisBenedictEqs:
    """
    Class modeling the Harris-Benedict Equations calculator for the Basal
    Metabolic Rate
    
    :param w_r: Weight Loss Rate
    :type w_r: np.array
    :param heihgt: height in inches
    :type heihgt: float
    :param age: age in years
    :type age: int
    """
    def __init__(self,
                weight_projection: np.ndarray,
                heihgt: float,
                age: int) -> None:
        """
        Class constructor

        :param w_r: Weight Loss Rate
        :type w_r: np.array
        :param heihgt: height in inches
        :type heihgt: float
        :param age: age in years
        :type age: int
        """
        assert [_ > 0 for _ in weight_projection], """Weight change values must be positive"""
        assert heihgt > 0, """Height is a positive physical property"""
        assert age >= 19, """Age must be 19 or greater"""

        self.weight_projection = weight_projection
        self.heihgt = heihgt
        self.age = age

    def for_men(self) -> np.ndarray:
        """
        Calculates the Harris-Benedict Equation for men

        :return: Basal Metabolic Rate
        :rtype: np.ndarray
        """
        self.bmr_men = 66.47 + (6.24*self.weight_projection) + (12.7*self.heihgt) - (6.76*self.age)
        return self.bmr_men
    
    def for_women(self) -> np.ndarray:
        """
        Calculates the Harris-Benedict Equation for men

        :return: Basal Metabolic Rate
        :rtype: np.ndarray
        """
        self.bmr_women = 65.51 + (4.34*self.weight_projection) + (4.7*self.heihgt) - (4.7*self.age)
        return self.bmr_women
    
    def jsonable_results(self) -> dict[str, list[float]] | None:
        if self.bmr_men.size != 0:
            return {"bmr": self.bmr_men.tolist()}
        elif self.bmr_women.size != 0:
            return {"bmr": self.bmr_women.tolist()}


class MifflinStJeorEq:
    pass