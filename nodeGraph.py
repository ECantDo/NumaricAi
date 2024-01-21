import numpy as np


class NodeGraph:
    """

    """

    def __init__(self):
        self.weights = None
        self.biases = None

        pass

    @staticmethod
    def sigmoid(x: float, slope: float = 1) -> float:
        """
        Preforms the sigmoid function on some input value, but maps the output between -1 and 1 instead of the typical 0
        and 1.
        :param x: The value to preform on.
        :param slope: Modifies the slope of the sigmoid function.  Must be positive. slope>1 -> gets more steep
        :return: A value between -1 and 1.
        """
        slope = abs(slope)
        return (2 / (1 + np.e ** (-slope * x))) - 1
        pass

    pass
