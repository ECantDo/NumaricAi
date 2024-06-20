from thirdAttempt.ai import CantDoAi
import random


class RandomizeNetwork:

    def __init__(self, network: CantDoAi, seed: int = 0):
        self.rand = random.Random(seed)
        pass

    def add_random_node(self):
        raise Exception("Not yet implemented")
        pass

    def add_random_edge(self):
        raise Exception("Not yet implemented")
        pass

    def modify_random_bias(self):
        raise Exception("Not yet implemented")
        pass

    def modify_random_weight(self):
        raise Exception("Not yet implemented")
        pass


if __name__ == "__main__":
    pass
