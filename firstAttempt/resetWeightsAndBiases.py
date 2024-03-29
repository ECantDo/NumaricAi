import random


def reset_biases(layer_widths: list, r: int, seed: int = None):
    """

    :dimensions: Format: dimensions = [biases layer 1 count, biases layer 2 count, ..., biases layer n count]
    len(dimensions) = n
    :return:
    """
    biases = []
    if seed is not None:
        random.seed(seed)

    for layer_bias_count in layer_widths:
        if layer_bias_count <= 0:
            continue
        biases.append([random.random() * 2 * r - r for i in range(layer_bias_count)])

    open("biases.cfg", 'w').write(str(biases))
    return biases
    pass


def reset_weights(layer_widths: list, r: int, seed: int = None):
    """

    :param layer_widths: [number of inputs, layer width 1 count, layer width 2 count]
    :param r:
    :param seed:
    :return:
    """
    weights = []
    if seed is not None:
        random.seed(seed)

    for layer in range(len(layer_widths) - 1):
        weights.append([])
        for layer_width in range(layer_widths[layer + 1]):
            weights[layer].append([random.randrange(-r, r) for i in range(layer_widths[layer])])
            pass
        pass

    open("weights.cfg", 'w').write(str(weights))
    return weights
    pass


def reset(layer_widths: list, r: int = 4, seed: int = 0):
    print(reset_biases(layer_widths[1:], 0, seed))
    print(reset_weights(layer_widths, r, seed + 1))
    pass


if __name__ == "__main__":
    reset([784, 64, 64, 64, 11], 32)
    # reset([2, 2, 2], 2)
    pass
