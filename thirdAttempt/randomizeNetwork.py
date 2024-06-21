from thirdAttempt import helperFunctions
from thirdAttempt.ai import CantDoAi
import random


class RandomizeNetwork:

    def __init__(self, network: CantDoAi, seed: int = 0):
        self.rand = random.Random(seed)
        self.network = network
        pass

    def set_network(self, network: CantDoAi):
        self.network = network
        pass

    def add_random_node(self):
        # Get the node number
        node = len(self.network.biases)

        # Get the outgoing and incoming nodes (do it before the new node is added, so it cant loop back on itself)
        outgoing = helperFunctions.get_outgoing_nodes(self.network)
        incoming = helperFunctions.get_incoming_nodes(self.network)

        # Add the new node
        self.network.weights.append(self.rand.random() * 2 - 1)
        self.network.weights.append(self.rand.random() * 2 - 1)
        self.network.biases.append(self.rand.random() * 2 - 1)

        # Add the links
        link = (self.rand.choice(outgoing), node)
        self.network.links.append(link)
        link = (node, self.rand.choice(incoming))
        self.network.links.append(link)
        pass

    def add_random_edge(self):
        raise Exception("Not yet implemented")
        pass

    def modify_random_weight(self):
        val = self.rand.random() * 2 - 1
        idx = self.rand.randint(0, len(self.network.weights) - 1)
        # print(idx, weights[idx], val)
        self.network.weights[idx] = (self.network.weights[idx] + val) / 2.0
        # print(weights[idx])
        pass

    def modify_random_bias(self):
        val = self.rand.random() * 2 - 1
        idx = self.rand.randint(0, len(self.network.biases) - 1)
        # print(idx, biases[idx], val)
        self.network.biases[idx] = (self.network.biases[idx] + val) / 2.0
        # print(biases[idx])
        pass


def main():
    weights, biases, links = [eval(line) for line in open("wbe.cfg").readlines()]
    # print(weights, biases, links)
    ai = CantDoAi(weights, biases, links)

    print(ai.links)
    import visualizeGraph
    # visualizeGraph.main(ai)
    RandomizeNetwork(ai).add_random_node()
    print(ai.links)
    visualizeGraph.main(ai)


if __name__ == "__main__":
    main()
    pass
