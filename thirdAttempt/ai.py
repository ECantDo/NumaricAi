import numpy as np


class CantDoAi:

    def __init__(self, weights: list[int], biases: list[int], links: list[int]):
        # One weight for every 2 links
        self.weights = weights  # [1, 2, 2, 1, 0, 1]
        # 1 bias for each node
        self.biases = biases  # [0] * len(self.weights)
        self.links = links  # [0, 2, 0, 3, 1, 2, 1, 3, 2, 5, 3, 5, 3, 4, 5, 4]

        # Input nodes are just nodes that don't have any inputs; so they are the nodes that receive the inputs
        self.input_nodes = None
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

        # Get a copy of the input nodes and edges, to be safe from overwriting them
        # TODO: Look into if an extra copy is needed
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

    def get_leading_nodes(self, edges: list[int] = None, exclude_input_nodes: list[int] = ()) -> list[int]:
        """
        Returns the leading nodes of the AI
        :param edges: Use this to specify a custom list of edges
        :param exclude_input_nodes: Use this to remove nodes from the leading nodes; needs the custom list of edges to
        work properly
        :return: The leading nodes of the AI
        """
        input_nodes = [True] * len(self.biases)
        if edges is None:
            edges = self.links
        for i in range(1, len(edges), 2):
            input_nodes[edges[i]] = False
        for v in exclude_input_nodes:
            input_nodes[v] = False
        return [i for i, x in enumerate(input_nodes) if x]

    def find_outgoing_links(self, node: int, edges: list[int] = None) -> list[int]:
        """
        Returns the indexes of the outgoing links of a given node
        :param node: The node to find the outgoing links of
        :param edges: Use this to specify a custom list of edges
        :return:
        """
        if edges is None:
            edges = self.links
        return [i for i, x in enumerate(edges) if x == node and i % 2 == 0]
        pass

    def get_subgraph(self, node: int, edges: list[int] = None) -> list[int]:
        """
        Returns the subgraph of the AI, with the given nodes removed
        :param node: The node that is not in the subgraph
        :param edges: Use this to specify a custom list of edges
        :return: The edges of the subgraph
        """
        if edges is None:
            edges = self.links

        new_edges = []
        for i in range(0, len(edges), 2):
            if edges[i] != node:
                new_edges.append(edges[i])
                new_edges.append(edges[i + 1])
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
        return None


if __name__ == "__main__":
    ai = CantDoAi()
    ai.update_input_nodes()
    pass
