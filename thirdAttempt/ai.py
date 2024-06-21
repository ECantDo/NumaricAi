import numpy as np


class CantDoAi:

    def __init__(self, weights: list[float], biases: list[float], links: list[tuple[int, int]]):
        # One weight for every 2 links
        self.weights = weights  # [1, 2, 2, 1, 0, 1]
        # 1 bias for each node
        self.biases = biases  # [0] * len(self.weights)
        self.links = links  # [(0, 2), (0, 3), (1, 2), (1, 3), (2, 5), (3, 5), (3, 4), (5, 4)]

        # Input nodes are just nodes that don't have any inputs; so they are the nodes that receive the inputs
        self.input_nodes = self.get_leading_nodes(None, [])
        self.output_nodes = self.get_trailing_nodes(None)
        # Any nodes that are added have to be inbetween the input nodes and the output nodes
        self.update_order = self.get_update_order()
        pass

    # ==================================================================================================================
    # FUNCTIONS TO UPDATE INTERNAL STATES NEEDED FOR THE AI
    # ==================================================================================================================
    def get_update_order(self) -> list[int]:
        """
        Updates the update order of processing of the nodes in the AI.
        Updates the input nodes if they have not been initialized yet.
        Assumes that the links making the graph, make an acyclic graph.
        :return: The processing order of the nodes in the AI
        """
        order = []
        # Check if the input nodes have been initialized
        if self.input_nodes is None:
            # If not, initialize them
            self.update_input_nodes()

        edgeless = list(self.input_nodes)  # Needs to be a copy; otherwise data will be lost
        edges = self.links  # Doesn't need to be a copy; the point is changed, not the data
        while len(edgeless) > 0:
            while len(edgeless) > 0:
                node = edgeless[0]
                edgeless = edgeless[1:]
                order.append(node)

                edges = self.get_subgraph(node, edges)

            edgeless = self.get_leading_nodes(edges, order)

        # print(f"Final order: {order}")
        return order

    def get_leading_nodes(self, edges: list[tuple[int, int]] = None, exclude_input_nodes: list[int] = ()) -> list[int]:
        """
        Returns the leading nodes of the AI; i.e. the nodes that have no incoming links
        :param edges: Use this to specify a custom list of edges
        :param exclude_input_nodes: Use this to remove nodes from the leading nodes; needs the custom list of edges to
        work properly
        :return: The leading nodes of the AI
        """
        input_nodes = [True] * len(self.biases)
        if edges is None:
            edges = self.links
        # for i in range(1, len(edges), 2):
        #     input_nodes[edges[i]] = False
        for edge in edges:
            input_nodes[edge[1]] = False
        for v in exclude_input_nodes:
            input_nodes[v] = False
        return [i for i, x in enumerate(input_nodes) if x]

    def get_trailing_nodes(self, edges: list[int] = None) -> list[int]:
        """
        Returns the trailing nodes of the AI; i.e. the nodes that have no outgoing links
        :param edges: A custom list of edges
        :return: The trailing nodes of the AI
        """
        if edges is None:
            edges = self.links
        has_outgoing_connection = [False] * len(self.biases)
        # for i in range(0, len(edges), 2):
        #     has_outgoing_connection[edges[i]] = True
        for edge in edges:
            has_outgoing_connection[edge[0]] = True
        return [idx for idx, cnnts in enumerate(has_outgoing_connection) if not cnnts]
        pass

    def find_outgoing_links(self, node: int, edges: list[tuple[int, int]] = None) -> list[int]:
        """
        Returns the indexes of the outgoing links of a given node
        :param node: The node to find the outgoing links of
        :param edges: Use this to specify a custom list of edges
        :return:
        """
        if edges is None:
            edges = self.links
        # return [i for i, x in enumerate(edges) if x == node and i % 2 == 0]
        return [i for i, edge in enumerate(edges) if edge[0] == node]
        pass

    def get_subgraph(self, node: int, edges: list[tuple[int, int]] = None) -> list[tuple[int, int]]:
        """
        Returns the subgraph of the AI, with the given nodes removed
        :param node: The node that is not in the subgraph
        :param edges: Use this to specify a custom list of edges
        :return: The edges of the subgraph
        """
        if edges is None:
            edges = self.links

        new_edges = []
        # for i in range(0, len(edges), 2):
        #     if edges[i] != node:
        #         new_edges.append(edges[i])
        #         new_edges.append(edges[i + 1])
        for edge in edges:
            if edge[0] != node:
                new_edges.append(edge)
        return new_edges
        pass

    def update_input_nodes(self):
        """
        Updates the input nodes of the AI, using the @get_leading_nodes function
        :return:
        """
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
        values = input_values + [0] * (len(self.biases) - len(input_values))
        for node in self.update_order:
            outgoing_links = self.find_outgoing_links(node)
            updated_nodes = set()
            for idx in outgoing_links:
                # TODO: Check if this works
                other_node = self.links[idx][1]
                updated_nodes.add(other_node)
                weight = self.weights[self.links.index((node, other_node))]
                values[other_node] += values[node] * self.weights[weight] + self.biases[other_node]

            for updated_node in updated_nodes:
                values[updated_node] = ActivationFunctions.relu(values[updated_node])
            pass
        return values


# ======================================================================================================================
# CLASS: ACTIVATION FUNCTIONS
# ======================================================================================================================
class ActivationFunctions:
    """
    This class contains the math functions used by the AI
    """

    @staticmethod
    def sigmoid(x: float) -> float:
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def tanh(x: float) -> float:
        """
        Basically the same as the sigmoid function, just it maps between -1 and 1
        :param x:
        :return:
        """
        return np.tanh(x)

    @staticmethod
    def relu(x: float) -> float:
        return np.max(x, 0)

    @staticmethod
    def step(x: float) -> float:
        return 1 if x > 0 else 0

    pass


if __name__ == "__main__":
    pass
