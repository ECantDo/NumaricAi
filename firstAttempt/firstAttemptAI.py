import numpy as np
import ast

import basicFunctions


class CantDoAI:
    biases_file_name = "biases.cfg"
    weights_file_name = "weights.cfg"

    def __init__(self, learning_step_size: float = 0.1):
        self.learning_step_size = learning_step_size

        self.__biases = CantDoAI.__get_values(self.biases_file_name)
        self.__weights = CantDoAI.__get_values(self.weights_file_name)
        self.__layers = [[0] * len(self.__weights[0][0])]
        for bias_layer in self.__biases:
            self.__layers.append([0] * len(bias_layer))

        # self.__weights_cost = [[[0 for elem in row] for row in layer] for layer in self.__weights]
        self.__layer_costs = list(self.__layers[1:])
        pass

    @staticmethod
    def __get_values(file_name: str):
        return ast.literal_eval(open(file_name, 'r').read())
        pass

    def print_bwl(self):
        print("Biases: ", self.__biases)
        print("Weights: ", self.__weights)
        print("Layers: ", self.__layers)
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
        if not (0 <= layer_idx < len(self.__biases)):
            print("RETURN")
            return
        self.__layers[layer_idx + 1] = (basicFunctions.activation(np.add(
            np.dot(np.array(self.__weights[layer_idx]), np.array(self.__layers[layer_idx])),
            self.__biases[layer_idx])).tolist())

        pass

    def multiply(self):
        """
        Preforms the multiply_layer() function on all layers.
        Each layer in self.__layers gets updated.
        :return: None
        """
        # print(f"Layers: {self.__layers}")
        for layer in range(len(self.__weights)):
            self.multiply_layer(layer)
        # print(f"Layers: {self.__layers}")

        pass

    def __learn(self):
        self.__layer_costs[-1] = list(self.get_output())
        # COMPUTE COSTS
        for i in range(len(self.__layer_costs) - 1, 0, -1):
            dot = np.dot(self.__layer_costs[i], self.__weights[i])
            self.__layer_costs[i - 1] = dot
        pass

    def save_weights(self):
        """
        Saves the weights to a file
        :return:
        """
        open(self.weights_file_name, 'w').write(str(self.__weights))
        pass

    def get_thought_index(self):
        """
        Gets the index of the largest activation
        :return:
        """
        return np.argmax(np.array(self.get_output()))
        pass

    def think(self, input_values: list, learning: bool = True):  # EXPAND ON THIS MORE
        """
        Makes the AI think about a series of inputs, then contemplates how well it did in regard to its thinking. It
        then changes how it thinks based on its contemplations.
        :param input_values: Expects a list of input values, with the first input value being the index of the
        expected result
        :return:
        """

        self.set_intput(input_values[1:])
        self.multiply()

        if learning and self.get_thought_index() != input_values[0]:
            # input_values[0] = expected value/correct index of solution
            # gradient = (list((lambda idx, x: (x - (1 if input_values[0] == idx else 0)) * 2)(idx, x) for idx, x in
            #              enumerate(self.get_output())))
            self.__learn(self.get_output())

        if self.get_thought_index() != input_values[0]:
            return True
        pass
