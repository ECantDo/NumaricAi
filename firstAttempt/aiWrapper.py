import getNumbers
import firstAttemptAI
import numpy as np

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


def main():
    small_tester_data_set = getNumbers.MnistDataContainer("mnist_train - Copy.csv")
    ai = firstAttemptAI.CantDoAI()

    values = small_tester_data_set.get_numberf(1)
    print(ai.think(values))
    print(ai.get_output())

    small_tester_data_set.make_image(small_tester_data_set.get_number(1))

    pass


main()
