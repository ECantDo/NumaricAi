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
    small_tester_data_set = getNumbers.MnistDataContainer("mnist_train - Copy.csv")
    ai = firstAttemptAI.CantDoAI()

    values = small_tester_data_set.get_numberf(1)
    print(ai.think(values))
    print(ai.get_output())

    small_tester_data_set.make_image(small_tester_data_set.get_number(1))

    pass


def small_main():
    print("LOADING FILE.....")
    tester_dataset = two_two_data_set()
    print("FILE LOADED")
    small_ai = firstAttemptAI.CantDoAI(1)

    # small_ai.think(tester_dataset[1])
    # # print(small_ai.print_bwl())
    #
    # exit(0)
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
            # print(data)
            # print(small_ai.think(data), end="\n\n")
            # print(f"{small_ai.get_output()}\t|| {data[0]} || {small_ai.get_thought_index()}")
        small_ai.save_weights()
        print(f"\r100% Complete\tCorrect:  {correct / len(tester_dataset) * 100}%\n")
    pass


def test_small_ai():
    small_ai = firstAttemptAI.CantDoAI()
    small_ai.think([0, 0.8, 0.0833], False)

    print(small_ai.get_output())
    pass


# test_small_ai()
small_main()
