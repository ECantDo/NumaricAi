import getNumbers
import firstAttempt
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
    ai = firstAttempt.CantDoAI()

    wrong_idxs = []
    right_idxs = []
    for i in range(small_tester_data_set.size()):
        values = small_tester_data_set.get_numberf(i)
        ai.think(values[1:])
        output, top_value = format_output(ai.get_output())
        if int(values[0]) != top_value:
            wrong_idxs.append([i, int(values[0]), top_value])
        else:
            right_idxs.append([i, int(values[0]), top_value, output])
        # print(output)
        # print(f"Actual number: {int(values[i])}, Thought: {top_value}")

    print(f"Got Wrong:")
    for wrong_idx in wrong_idxs:
        print(f"Idx: {wrong_idx[0]}\t| Was: {wrong_idx[1]} | Thought: {output_names[wrong_idx[2]]}")
        # small_tester_data_set.show_image_at_index(wrong_idx)
        pass

    print(f"\nGot Right:")
    for right_idx in right_idxs:
        print(
            f"Idx: {right_idx[0]}\t| Was: {right_idx[1]} | Thought: {output_names[right_idx[2]]} | Confidence: {right_idx[3]}")
        # small_tester_data_set.show_image_at_index(wrong_idx)
        pass

    pass


main()
