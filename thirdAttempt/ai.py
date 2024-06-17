import numpy as np


class CantDoAi:

    def __init__(self, weights: list[int], biases: list[int], links: list[int]):
        self.weights = weights  # [1, 2, 2, 1, 0, 1]
        self.biases = biases  # [0] * len(self.weights)
        self.links = links  # [0, 2, 0, 3, 1, 2, 1, 3, 2, 5, 3, 5, 3, 4, 5, 4]

        # Update order is the order in which the nodes should be processed; None if not initialized
        self.update_order = None
        # Input nodes are just nodes that don't have any inputs; so they are the nodes that receive the inputs
        self.input_nodes = None
        self.update_update_order()
        pass

    # ==================================================================================================================
    # FUNCTIONS TO UPDATE INTERNAL STATES NEEDED FOR THE AI
    # ==================================================================================================================
    def update_update_order(self) -> list[int]:
        """
        Updates the update order of processing of the nodes in the AI
        :return:
        """
        order = []
        # Check if the input nodes have been initialized
        if self.input_nodes is None:
            # If not, initialize them
            self.update_input_nodes()

        # Get a copy of the input nodes and edges, to be safe from overwriting them
        # TODO: Look into if an extra copy is needed
        edgeless = list(self.input_nodes)
        edges = list(self.links)
        while len(edgeless) > 0:
            # print(f"\n{edgeless = }")
            # print(f"{edges = }")
            # print(f"{order = }")
            new_edges = []
            while len(edgeless) > 0:
                node = edgeless[0]
                edgeless = edgeless[1:]
                order.append(node)

                # print(f"{node = } | ", end="")

                for i in range(0, len(edges), 2):
                    if edges[i] != node:
                        new_edges.append(edges[i])
                        new_edges.append(edges[i + 1])

                edges = new_edges
                # print(f"{new_edges = }")
                new_edges = []

            # print(f"{self.get_leading_nodes(edges, order) = }\n")
            edgeless = self.get_leading_nodes(edges, order)

        # print(f"Final order: {order}")
        return order

    def get_leading_nodes(self, edges: list[int] = None, exclude_input_nodes: list[int] = ()) -> list[int]:
        input_nodes = [True] * len(self.weights)
        if edges is None:
            edges = self.links
        for i in range(1, len(edges), 2):
            input_nodes[edges[i]] = False
        for v in exclude_input_nodes:
            input_nodes[v] = False
        return [i for i, x in enumerate(input_nodes) if x]

    def update_input_nodes(self):
        # Get all the nodes that don't have any inputs in the default state
        self.input_nodes = self.get_leading_nodes(None, [])

    # ==================================================================================================================
    # FUNCTIONS TO IMPLEMENT THE AI
    # ==================================================================================================================

    def think(self, input_values: list[float]) -> list[float] or None:
        """
        Returns the output of the AI from a given input
        :param input_values: Inputs to the AI (floats)
        :return: Output of the AI (floats)
        """
        return None


if __name__ == "__main__":
    ai = CantDoAi()
    ai.update_input_nodes()
    ai.update_update_order()
    pass
