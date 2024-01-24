import getNumbers
import numpy as np
import ast

import nodeGraph


class CantDoAI:
    def __init__(self):
        self.biases = CantDoAI.get_values("biases.arr")
        self.weights = CantDoAI.get_values("weights.arr")
        self.layers = [np.array([0] * len(self.weights[0]))]
        for bias_layer in self.biases:
            self.layers.append([0] * len(bias_layer))
        pass

    @staticmethod
    def get_values(file_name: str):
        return ast.literal_eval(open(file_name, 'r').read())
        pass

    def print_bwl(self):
        print(self.biases)
        print(self.weights)
        print(self.layers)
        pass

    def set_intput(self, input_values: list):
        length = len(self.layers[0])
        self.layers[0] = list(input_values[:len(self.layers[0])])

        while len(self.layers[0]) != length:
            self.layers[0].append(0)
        pass

    def get_output(self):
        return self.layers[-1]
        pass

    def multiply_layer(self, layer_idx: int):
        """

        :param layer_idx: A layer_idx of value 0, is the first hidden layer/what ever is after the input
        :return:
        """
        if layer_idx < 0 and layer_idx < len(self.biases):
            return

        self.layers[layer_idx + 1] = (nodeGraph.sigmoid(np.add(
            np.dot(np.array(self.weights[layer_idx]).T, np.array(self.layers[layer_idx])),
            self.biases[layer_idx])).tolist())

        pass

    def multiply(self):
        for layer in range(len(self.biases)):
            self.multiply_layer(layer)
        pass

    def think(self, input_values: list):  # EXPAND ON THIS MORE
        self.set_intput(input_values)
        self.multiply()
        pass

    pass
