import nodeGraph


def test_sigmoid():
    test_cases = [
        [0, 1, 0],  # x = 0, n = 1
        [1, 2, 0.761594155956],  # x = 1, n = 2
        [-1, 0.5, -0.244918662404],  # x = -1, n = 0.5
        [2, 3, 0.995054753687],  # x = 2, n = 3
        [0.5, 1.5, 0.358357398351],  # x = 0.5, n = 1.5
    ]
    success = True
    for test_case in test_cases:
        output = nodeGraph.NodeGraph.sigmoid(test_case[0], test_case[1])
        output = round(output, 12)
        equal = output == test_case[2]
        print(f"x: {test_case[0]};\tslope: {test_case[1]};\tOutput=Test?: {equal}", end=" ")
        if not equal:
            print(f"Output: {output};\tTestCase: {test_case[2]}")
        else:
            print()
        success = success and equal
        pass
    return success
    pass


sigmoid_test = test_sigmoid()
print(sigmoid_test)
