from thirdAttempt.ai import CantDoAi


def test_init():
    weights = [1, 2, 2, 1, 0, 1]
    biases = [0] * len(weights)
    links = [0, 2, 0, 3, 1, 2, 1, 3, 2, 5, 3, 5, 3, 4, 5, 4]

    ai = CantDoAi(weights, biases, links)

    # Make sure the values of the AI are saved
    assert ai.weights == weights
    assert ai.biases == biases
    assert ai.links == links


def test_get_leading_nodes1():
    weights = []  # Can be empty, nothing done with these values when getting leading nodes
    biases = [0, 1, 2, 3, 4, 5]
    links = [(0, 2), (0, 3), (1, 2), (1, 3), (2, 5), (3, 5), (3, 4), (5, 4)]

    ai = CantDoAi(weights, biases, links)
    assert ai.get_leading_nodes() == [0, 1]


def test_get_leading_nodes2():
    weights = []  # Can be empty, nothing done with these values when getting leading nodes
    biases = [0, 1, 2, 3, 4]
    links = [(4, 0), (4, 2), (4, 3), (4, 1), (3, 0), (2, 0), (0, 1)]

    ai = CantDoAi(weights, biases, links)

    assert ai.get_leading_nodes() == [4]


def test_get_leading_nodes3():
    weights = []  # Can be empty, nothing done with these values when getting leading nodes
    biases = [0, 1, 2, 3, 4]
    links = [(4, 0), (4, 3), (4, 1), (3, 0), (2, 0), (0, 1)]

    ai = CantDoAi(weights, biases, links)

    assert ai.get_leading_nodes() == [2, 4]


def test_find_outgoing_links1():
    weights = []  # Can be empty, nothing done with these values when getting outgoing links
    biases = [0, 1, 2, 3, 4]
    links = [(4, 0)]

    ai = CantDoAi(weights, biases, links)

    assert ai.find_outgoing_links(4) == [0]


def test_find_outgoing_links2():
    weights = []  # Can be empty, nothing done with these values when getting outgoing links
    biases = [0, 1, 2, 3, 4]
    links = [(4, 0), (4, 1), (4, 2), (4, 3)]

    ai = CantDoAi(weights, biases, links)

    assert ai.find_outgoing_links(4) == [0, 2, 4, 6]


def test_update_order1():
    weights = []  # Can be empty, nothing done with these values when getting update order
    biases = [0]
    links = []

    ai = CantDoAi(weights, biases, links)

    assert ai.update_order == [0]


def test_update_order2():
    weights = []  # Can be empty, nothing done with these values when getting update order
    biases = [0, 0]
    links = [(0, 1)]

    ai = CantDoAi(weights, biases, links)

    assert ai.update_order == [0, 1]


def test_update_order3():
    weights = []  # Can be empty, nothing done with these values when getting update order
    biases = [0, 0, 0, 0, 0]
    links = [(0, 4), (1, 4), (2, 4), (3, 4)]

    ai = CantDoAi(weights, biases, links)

    assert ai.update_order == [0, 1, 2, 3, 4]


def test_update_order4():
    weights = []  # Can be empty, nothing done with these values when getting update order
    biases = [0, 0, 0, 0, 0]
    links = [(4, 0), (4, 2), (4, 3), (4, 1)]

    ai = CantDoAi(weights, biases, links)

    assert ai.update_order == [4, 0, 1, 2, 3]


def test_update_order5():
    weights = []  # Can be empty, nothing done with these values when getting update order
    biases = [0, 0, 0, 0, 0]
    links = [(4, 0), (4, 2), (4, 3), (4, 1), (3, 0), (2, 0), (0, 1)]

    ai = CantDoAi(weights, biases, links)

    assert ai.update_order == [4, 2, 3, 0, 1]


def test_values_after_update1():
    weights = []  # Can be empty, nothing done with these values when getting update order
    biases = [0]
    links = []

    ai = CantDoAi(weights, biases, links)

    assert ai.weights == []
    assert ai.biases == [0]
    assert ai.links == []


def test_values_after_update2():
    weights = []  # Can be empty, nothing done with these values when getting update order
    biases = [0, 0]
    links = [0, 1]

    ai = CantDoAi(weights, biases, links)

    assert ai.weights == []
    assert ai.biases == [0, 0]
    assert ai.links == [(0, 1)]


def test_values_after_update3():
    weights = []  # Can be empty, nothing done with these values when getting update order
    biases = [0, 0, 0, 0, 0]
    links = [(0, 4), (1, 4), (2, 4), (3, 4)]

    ai = CantDoAi(weights, biases, links)

    assert ai.weights == []
    assert ai.biases == [0, 0, 0, 0, 0]
    assert ai.links == [(0, 4), (1, 4), (2, 4), (3, 4)]


def test_values_after_update4():
    weights = []  # Can be empty, nothing done with these values when getting update order
    biases = [0, 0, 0, 0, 0]
    links = [(4, 0), (4, 2), (4, 3), (4, 1)]

    ai = CantDoAi(weights, biases, links)

    assert ai.weights == []
    assert ai.biases == [0, 0, 0, 0, 0]
    assert ai.links == [(4, 0), (4, 2), (4, 3), (4, 1)]


def test_values_after_update5():
    weights = []  # Can be empty, nothing done with these values when getting update order
    biases = [0, 0, 0, 0, 0]
    links = [(4, 0), (4, 2), (4, 3), (4, 1), (3, 0), (2, 0), (0, 1)]

    ai = CantDoAi(weights, biases, links)

    assert ai.weights == []
    assert ai.biases == [0, 0, 0, 0, 0]
    assert ai.links == [(4, 0), (4, 2), (4, 3), (4, 1), (3, 0), (2, 0), (0, 1)]


def test_get_trailing_nodes1():
    weights = []  # Can be empty, nothing done with these values when getting update order
    biases = [0]
    links = []

    ai = CantDoAi(weights, biases, links)

    assert ai.get_trailing_nodes() == [0]


def test_get_trailing_nodes2():
    weights = []  # Can be empty, nothing done with these values when getting update order
    biases = [0, 1]
    links = [(0, 1)]

    ai = CantDoAi(weights, biases, links)

    assert ai.get_trailing_nodes() == [1]


def test_get_trailing_nodes3():
    weights = []  # Can be empty, nothing done with these values when getting update order
    biases = [0, 1, 2, 3, 4]
    links = [(4, 2), (4, 3), (4, 0), (3, 0), (2, 0), (0, 1)]

    ai = CantDoAi(weights, biases, links)

    assert ai.get_trailing_nodes() == [1]
