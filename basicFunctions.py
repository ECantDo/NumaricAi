import numpy as np


def activation(x):
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


def activation_derivative(x):
    active = activation(x)
    return active * (1 - active)
    pass


def slope(activation: float, expected_activation: float):
    return 2 * (activation - expected_activation)
    pass


def node_cost(activation: float, expected_activation: float):
    # cost = (a - y)^2
    return (activation - expected_activation) ** 2
    pass


if __name__ == "__main__":
    # operations = np.array([0, 999, 2, -999, -99])
    # print(operations.tolist())
    # print(sigmoid(operations).tolist())
    # print(sigmoid_derivative(operations).tolist())

    output = [1, 1, 1, 1, 1, 1, 1]
    correct_idx = 1
    pass
