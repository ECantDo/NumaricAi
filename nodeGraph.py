import numpy as np


class NodeGraph:
    """
    The matrix for the nural network
    """

    def __init__(self):
        self.weights = None
        self.biases = None
        self.activations = None

        pass

    @staticmethod
    def sigmoid(x: float, slope: float = 1) -> float:
        """
        Preforms the sigmoid function on some input value
        :param x: The value to preform on.
        :param slope: Modifies the slope of the sigmoid function.  Must be positive. slope>1 -> gets more steep
        :return: A value between 0 and 1.
        """
        slope = abs(slope)
        return 1 / (1 + np.e ** (-slope * x))
        pass

    pass
