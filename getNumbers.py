import numpy as np
import matplotlib.pyplot as plt


def make_image(mnist_data: list, image_width: int = 28, image_height: int = 28):
    """
    Makes and displays the image of a given case, for the user to see -> this is not for the AI.
    From the MNIST database, each image is a 28*28 number, it is assumed that the image is from this database.
    :return: None
    """
    image_array = np.array(mnist_data[1:]).reshape(28, 28)

    # Display the grayscale image
    plt.axis(False)
    plt.imshow(image_array, cmap='gray')
    plt.title(f'Number {mnist_data[0]}')
    plt.show()
    pass


root_folder_location = "E:/MNIST (Labeled numbers)/MNIST_CSV/"


class MnistDataContainer:
    def __init__(self, file_name: str):
        self.file_location = f"{root_folder_location}{file_name}"
        # Gets the data for a MNIST number from a csv file representing a gray-scale image.
        self.mnist_data = [list(map(int, line.strip().split(','))) for line in open(self.file_location, 'r') if
                           line.strip() != '']
        pass

    def get_number(self, idx: int):
        """
        Gets the data from the mnist data at a particular index.
        :param idx: The index to get the data from.
        :return: Returns a list of ints, or None if the index does not exist.
        """
        try:
            return self.mnist_data[idx]
        except IndexError as ie:
            return None
        pass

    def show_image_at_index(self, idx: int):
        """
        Displays the grayscale image for a given index in the data.
        :param idx: The index to get the data from.
        :return: Returns if it was successful in showing the image, returns false if the index does not exist.
        """
        number = self.get_number(idx)
        if number is None:
            return False
        make_image(number)
        return True
        pass

    pass


# program_test = MnistDataContainer("mnist_train - Copy.csv")
# print(program_test.show_image_at_index(-1))
