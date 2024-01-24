import numpy as np


def sigmoid(x):
    """
    Preforms the sigmoid function on some input value
    :param x: The value to preform on.
    :return: A value between 0 and 1.
    """
    try:
        result = 1 / (1 + np.exp(-x))
    except OverflowError as ofe:
        if x > 0:
            result = 1.0
        else:
            result = 0.0
    return result
    pass


def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)
    pass


if __name__ == "__main__":
    operations = np.array([0, 999, 2, -999, -99])
    print(operations.tolist())
    print(sigmoid(operations).tolist())
    print(sigmoid_derivative(operations).tolist())
    pass
