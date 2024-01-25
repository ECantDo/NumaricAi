import math

import getNumbers
import firstAttemptAI
import numpy as np
import ast

output_names = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Nan")


def format_output(output_data: list):
    output = ""
    values_array = np.array(output_data)

    # Find the indices of the values in descending order
    indices_descending_order = np.argsort(values_array)[::-1]

    # Print the names corresponding to the largest values
    for index in indices_descending_order:
        output += f"|{output_names[index]}: {output_data[index] * 100}% Confidence|\t"
    return output, indices_descending_order[0]
    pass


def two_two_data_set():
    return ast.literal_eval(open("2x2AiInputs.txt", 'r').read())
    pass


def main():
    print("LOADING FILE.....")
    data_set = getNumbers.MnistDataContainer("mnist_train.csv")
    ai = firstAttemptAI.CantDoAI(learning_step_size=100)

    for i in range(1):  # Generations
        correct = 0
        last_percent = 0
        for idx in range(data_set.size()):
            data = data_set.get_number(idx)
            wrong = ai.think(data)

            percent = idx / data_set.size() * 100
            if percent >= last_percent + 1:
                last_percent = math.floor(percent)
                print(f"\r{last_percent}% Complete\tCorrect: {correct / idx * 100}%", end="")
            if not wrong:
                correct += 1

        ai.save_weights()
        print(f"\r100% Complete\tCorrect:  {correct / data_set.size() * 100}%\n")

    pass


def small_main():
    print("LOADING FILE.....")
    tester_dataset = two_two_data_set()
    print("FILE LOADED")
    small_ai = firstAttemptAI.CantDoAI(1)

    for i in range(5):
        correct = 0
        last_percent = 0
        for idx, data in enumerate(tester_dataset):
            wrong = small_ai.think(data)

            percent = idx / len(tester_dataset) * 100
            if percent >= last_percent + 1:
                last_percent = math.floor(percent)
                print(f"\r{last_percent}% Complete\tCorrect: {correct / idx * 100}%", end="")
            if not wrong:
                correct += 1

        small_ai.save_weights()
        print(f"\r100% Complete\tCorrect:  {correct / len(tester_dataset) * 100}%\n")
    pass


def test_small_ai():
    small_ai = firstAttemptAI.CantDoAI()
    small_ai.think([0, 0.8, 0.0833], False)

    print(small_ai.get_output())
    pass


# test_small_ai()
# small_main()
main()
