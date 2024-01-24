import getNumbers
import numpy as np
import ast

import nodeGraph


class CantDoAI:
    def __init__(self):
        self.__biases = CantDoAI.get_values("biases.cfg")
        self.__weights = CantDoAI.get_values("weights.cfg")
        self.__layers = [np.array([0] * len(self.__weights[0][0]))]
        for bias_layer in self.__biases:
            self.__layers.append([0] * len(bias_layer))
        pass

    @staticmethod
    def get_values(file_name: str):
        return ast.literal_eval(open(file_name, 'r').read())
        pass

    def print_bwl(self):
        print(self.__biases)
        print(self.__weights)
        print(self.__layers)
        pass

    def set_intput(self, input_values: list):
        """
        Sets the input layer to a copy of a list of the input values.
        :param input_values: A list of floats between zero and one
        :return: None
        """
        length = len(self.__layers[0])
        self.__layers[0] = list(input_values[:len(self.__layers[0])])

        while len(self.__layers[0]) != length:
            self.__layers[0].append(0)
        pass

    def get_output(self):
        """
        Gets the last activation layer representing the output
        :return: Returns a list of floats between zero and one representing the output of the AI
        """
        return self.__layers[-1]
        pass

    def multiply_layer(self, layer_idx: int):
        """
        Preforms matrix multiplication on a given layer.  Updates the next layer with the resulting values.
        :param layer_idx: A layer_idx of value 0, is the first hidden layer/what ever is after the input
        :return: None
        """
        if layer_idx < 0 and layer_idx < len(self.__biases):
            return
        self.__layers[layer_idx + 1] = (nodeGraph.sigmoid(np.add(
            np.dot(np.array(self.__weights[layer_idx]), np.array(self.__layers[layer_idx])),
            self.__biases[layer_idx])).tolist())

        pass

    def multiply(self):
        """
        Preforms the multiply_layer() function on all layers.
        Each layer in self.__layers gets updated.
        :return: None
        """

        for layer in range(len(self.__biases)):
            self.multiply_layer(layer)
        pass

    def think(self, input_values: list) -> list:  # EXPAND ON THIS MORE
        """
        Makes the AI think about a series of inputs, then contemplates how well it did in regard to its thinking.
        :param input_values: Expects a list of input values, with the first input value being the index of the
        expected result
        :return: Returns the cost of the inputs
        """

        self.set_intput(input_values[1:])
        self.multiply()

        cost = (list((lambda idx, x: (x - (1 if input_values[0] == idx else 0)) ** 2)(idx, x) for idx, x in
                     enumerate(self.get_output())))
        return cost

        pass
