import numpy as np
from ai import CantDoAi


class MicroGameWrapper:
    def __init__(self, env_name="MicroGame-v0"):
        weights, biases, links = [eval(line) for line in open("wbe.cfg").readlines()]
        # print(weights, biases, links)
        self.ai = CantDoAi(weights, biases, links)
        self.env_name = env_name

        print(self.ai.think([1, 1, 1, 1, 1, 1]))

        import visulizeGraph
        visulizeGraph.main(weights)
        pass


if __name__ == "__main__":
    MicroGameWrapper()
    pass
