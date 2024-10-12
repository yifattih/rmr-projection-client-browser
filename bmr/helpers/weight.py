import numpy as np

class WeightCalculator:
    """
    Class modeling a weight calculator based on weight loss rate

    :param w_i: initial weight
    :type w_i: float
    :param a: weight loss multiplier
    :type a: int
    :param t: time
    :type t: int
    """
    def __init__(self, w_i: float, a: int, t: int) -> None:
        """
        Class constructor

        :param w_i: initial weight
        :type w_i: float
        :param a: weight loss multiplier
        :type a: int
        :param t: time
        :type t: int
        """
        assert w_i > 0, """Weight is a positive physiscal property"""
        assert a > 0, """Weight loss multiplier must be positive"""
        assert 0 <= t <= 52, """Time is the number weeks in a period of a year
                                (between 0 and 52 weeks)"""

        self.w_i = w_i
        self.a = a
        self.t = t
        self.w = np.array([])

    def time_range(self):
        return np.array(range(0, self.t + 1, 1))

    def weight_loss_rate(self):
        """
        Calculates the weight loss rate

        :return: Weight Loss Rate
        :rtype: np.ndarray
        """
        self.w_r = 2*self.time_range()
        return self.w_r

    def weight_change(self):
        """
        Calculates the weight at specific time based on weight loss rate

        :return: Weingt in Time
        :rtype: np.ndarray
        """
        self.weight_loss_rate()
        return self.w_i - self.w_r
