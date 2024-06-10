import numpy as np


def activation(x: float) -> float:
    """
    Preforms the sigmoid function on some input value representing the activation of a node.
    :param x: float; The value to preform on.
    :return: float; A value between 0 and 1.
    """
    try:
        result = 1 / (1 + np.exp(-x))
    # Might overflow; if it overflows clamp to the max/min value.
    except OverflowError as ofe:
        if x > 0:
            result = 1.0
        else:
            result = 0.0
    return result
    pass


def activation_derivative(x) -> float:
    active = activation(x)
    return active * (1 - active)
    pass


def cost_derivative(node_activation: float, expected_activation: float) -> float:
    return expected_activation - node_activation
    pass


def node_cost(node_activation: float, expected_activation: float) -> float:
    """
    Gets the cost of a particular node with some expected activation value.
    :param node_activation: float; The activation of a node.
    :param expected_activation: float; The expected activation value.
    :return: float; cost of the node
    """
    # cost = 1/2(a - y)^2
    return .5 * (node_activation - expected_activation) ** 2
    pass


def output_cost(node_activations: list[float], expected_index: int):
    """
    Preforms the node_cost on every element of an array of node activations.
    :param node_activations: List of floats of the activations.
    :param expected_index: The index in the input list where the expected value is 1.
    :return: List of floats filled with the cost.
    """
    costs = []
    for idx, node_activation in enumerate(node_activations):
        costs.append(cost_derivative(node_activation, int(idx == expected_index)))
    return costs
    pass


def output_cost_derivative(node_costs: list[float], expected_index: int):
    cost_derivatives = []
    for idx, cost in enumerate(node_costs):
        cost_derivatives.append(node_cost(cost, int(idx == expected_index)))
    return cost_derivatives


if __name__ == "__main__":
    # operations = np.array([0, 999, 2, -999, -99])
    # print(operations.tolist())
    # print(sigmoid(operations).tolist())
    # print(sigmoid_derivative(operations).tolist())

    # output = [1, 1, 1, 1, 1, 1, 1]
    # correct_idx = 1

    pass
