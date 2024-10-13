import numpy as np

class WeightCalculator:
    """
    Class modeling a weight calculator based on weight loss rate

    :param weight_initial: initial weight
    :type weight_initial: float
    :param multiplier: weight loss multiplier
    :type multiplier: int
    :param time: time
    :type time: int
    """
    def __init__(self,
                weight_initial: float,
                time: int,
                multiplier: int = 2) -> None:
        """
        Class constructor

        :param weight_initial: initial weight
        :type weight_initial: float
        :param multiplier: weight loss multiplier
        :type multiplier: int
        :param time: time
        :type time: int
        """
        assert weight_initial > 0, """Weight is a positive physiscal property"""
        assert multiplier > 0, """Weight loss multiplier must be positive"""
        assert 0 <= time <= 52, """Time is the number weeks in a period of a year
                                (between 0 and 52 weeks)"""

        self.weight_initial = weight_initial
        self.multiplier = multiplier
        self.time = time
        self.w = np.array([])

    def weight_loss_rate_time(self):
        self.loss_rate_time = np.array(range(0,
                                             self.time + 1,
                                             1))
        return self.loss_rate_time

    def weight_loss_rate(self):
        """
        Calculates the weight loss rate

        :return: Weight Loss Rate
        :rtype: np.ndarray
        """
        self.loss_rate = 2*self.weight_loss_rate_time()
        return self.loss_rate

    def weight_loss_projection(self):
        """
        Calculates the weight at specific time based on weight loss rate

        :return: Weingt in Time
        :rtype: np.ndarray
        """
        self.weight_loss_rate()
        self.weight_projection = self.weight_initial - self.loss_rate
        return self.weight_projection
    
    def jsonable_results(self):
        return {"weight_loss_rate_time": self.loss_rate_time.tolist(),
                "weight_loss_rate": self.loss_rate.tolist(),
                "weight_loss_projection": self.weight_projection.tolist()}