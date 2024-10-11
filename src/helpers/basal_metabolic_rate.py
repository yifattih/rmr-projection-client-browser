import numpy as np

class HarrisBenedictEqs:
    """
    Class modeling the Harris-Benedict Equations calculator for the Basal
    Metabolic Rate
    
    :param w_r: Weight Loss Rate
    :type w_r: np.array
    :param h: height in inches
    :type h: float
    :param y: age in years
    :type y: int
    """
    def __init__(self, w_change: np.ndarray, h: float, y: int) -> None:
        """
        Class constructor

        :param w_r: Weight Loss Rate
        :type w_r: np.array
        :param h: height in inches
        :type h: float
        :param y: age in years
        :type y: int
        """
        assert [_ > 0 for _ in w_change], """Weight change values must be
                                             positive"""
        assert h > 0, """Height is a positive physical property"""
        assert y >= 19, """Age must be 19 or greater"""

        self.w_change = w_change
        self.h = h
        self.y = y

    def men(self):
        """
        Calculates the Harris-Benedict Equation for men

        :return: Basal Metabolic Rate
        :rtype: np.ndarray
        """
        return 66.47 + (6.24*self.w_change) + (12.7*self.h) - (6.76*self.y)
    
    def women(self):
        """
        Calculates the Harris-Benedict Equation for men

        :return: Basal Metabolic Rate
        :rtype: np.ndarray
        """
        return 65.51 + (4.34*self.w_change) + (4.7*self.h) - (4.7*self.y)


class MifflinStJeorEq:
    pass