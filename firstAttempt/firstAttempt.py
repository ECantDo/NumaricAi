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

    pass


def matrix_mult_example():
    matrix_A = np.array([[1, 2, 3], [3, 4, 3]])
    matrix_B = np.array([[1, 2], [3, 4], [5, 6]])

    # Perform matrix multiplication using numpy.dot
    result_dot = np.dot(matrix_A, matrix_B)

    # Perform matrix multiplication using @ operator
    result_operator = matrix_A @ matrix_B

    # Display the results
    print("Matrix A:")
    print(matrix_A)

    print("\nMatrix B:")
    print(matrix_B)

    print("\nResult using numpy.dot:")
    print(result_dot)

    print("\nResult using @ operator:")
    print(result_operator)


ai = CantDoAI()
# ai.set_intput([.0117647059, .0705882353, .0705882353, .0705882353])
# ai.print_bwl()
# ai.multiply_layer(0)
# ai.print_bwl()

# matrix_mult_example()
