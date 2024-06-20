import random


def reset_network(input_node_count: int, output_node_count: int, seed: int = 0) -> tuple[list, list, list]:
    weights = []
    biases = [None] * input_node_count + [0] * output_node_count
    links = []
    random.seed(seed)

    for i in range(input_node_count):
        for j in range(output_node_count):
            # weights.append((i, j + input_node_count))
            weights.append(random.random() * 2 - 1)
            # weights.append(1)
            links.append((i, j + input_node_count))
            # links.append(j + input_node_count)

    return weights, biases, links
    pass


def main():
    # There needs to be 6 inputs; tile type in front of the agent (sight), x and y of the goal, x and y of the agent,
    # and the direction the agent is facing.
    # There needs to be 4 outputs; turn left, turn right, move forward, do nothing.
    weights, biases, links = reset_network(6, 4)
    with open("wbe.cfg", "w") as f:
        f.write(f"{weights}\n")
        f.write(f"{biases}\n")
        f.write(f"{links}\n")


if __name__ == "__main__":
    main()
    pass
