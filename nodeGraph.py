import math
import numpy


def sigmoid(x: float, slope: float = 1) -> float:
    """
    Preforms the sigmoid function on some input value
    :param x: The value to preform on.
    :param slope: Modifies the slope of the sigmoid function.  Must be positive. slope>1 -> gets more steep
    :return: A value between 0 and 1.
    """
    slope = abs(slope)
    try:
        result = 1 / (1 + math.exp(-slope * x))

    except OverflowError as ofe:
        if x > 0:
            result = 1.0
        else:
            result = 0.0
        # print(ofe)

    return result
    pass


# print(math.exp(1))
# print(sigmoid(709, 0.01))


class NodeGraph:
    """
    The matrix for the nural network
    """

    def __init__(self):
        self.weights = None
        self.biases = None
        self.activations = None
        pass

    pass
