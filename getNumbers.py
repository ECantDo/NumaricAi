import numpy as np


def get_data(file_path: str):
    """
    Gets the data from a csv file representing a gray-scale image
    :param file_path:
    :return:
    """
    mnist_data = np.array(
        [list(map(int, line.strip().split(','))) for line in open(file_path, 'r') if line.strip() != '']
    )
    print(mnist_data[0])
    return mnist_data
    pass


def make_image(mnist_data, rescale: float = 1.0, image_width: int = 28, image_height: int = 28):
    """
    Makes and displays the image of a given case, for the user to see -> this is not for the AI.
    From the MNIST database, each image is a 28*28 number, it is assumed that the image is from this database.
    :return:
    """
    pass


root_folder_location = "E:/MINSIT (Labeled numbers)/MNIST_CSV/"


class TestingData:
    file_location = f"{root_folder_location}mnist_test.csv"

    def __init__(self):
        get_data(self.file_location)

    pass


class TrainingData:
    file_location = f"{root_folder_location}mnist_train.csv"

    def __init__(self):
        get_data(self.file_location)

    pass


TrainingData()
