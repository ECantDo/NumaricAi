import thirdAttempt.helperFunctions as hf


def test_binary_tuple_search1():
    lst = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]
    assert hf.binary_search_tuples(lst, key=5, tuple_index=0) == 5


def test_tuple_search1():
    lst = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]
    assert hf.tuple_search(lst, key=5, tuple_index=0) == 5


def test_binary_tuple_search2():
    lst = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]
    assert hf.binary_search_tuples(lst, key=7, tuple_index=1) == 7


def test_tuple_search2():
    lst = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]
    assert hf.tuple_search(lst, key=7, tuple_index=1) == 7


def test_tuple_sort1():
    lst = [(9, 5), (9, 3), (9, 7), (3, 1), (4, 1)]
    sorted_0 = hf.tuple_sort(lst, tuple_index=0)
    sorted_1 = hf.tuple_sort(lst, tuple_index=1)
    assert sorted_0 == [(3, 1), (4, 1), (9, 5), (9, 3), (9, 7)]
    assert sorted_1 == [(3, 1), (4, 1), (9, 3), (9, 5), (9, 7)]


def test_tuple_sort2():
    lst = [(2, 8), (0, 8), (0, 9), (1, 8), (2, 7), (0, 6), (2, 6), (0, 7), (1, 9), (1, 7), (1, 6), (2, 9)]
    sorted_0 = hf.tuple_sort(lst, tuple_index=0)
    sorted_1 = hf.tuple_sort(lst, tuple_index=1)

    assert sorted_0 == [(0, 8), (0, 9), (0, 6), (0, 7), (1, 8), (1, 9), (1, 7), (1, 6), (2, 8), (2, 7), (2, 6), (2, 9)]
    assert sorted_1 == [(0, 6), (2, 6), (1, 6), (2, 7), (0, 7), (1, 7), (2, 8), (0, 8), (1, 8), (0, 9), (1, 9), (2, 9)]


def test_tuple_sort3():
    lst = [(2, 8), (0, 8), (0, 9), (1, 8), (2, 7), (0, 6), (2, 6), (0, 7), (1, 9), (1, 7), (1, 6), (2, 9)]
    sorted_0 = hf.tuple_sort(lst, tuple_index=0)
    sorted_1 = hf.tuple_sort(sorted_0, tuple_index=1)

    assert sorted_0 == [(0, 8), (0, 9), (0, 6), (0, 7), (1, 8), (1, 9), (1, 7), (1, 6), (2, 8), (2, 7), (2, 6), (2, 9)]
    assert sorted_1 == [(0, 6), (1, 6), (2, 6), (0, 7), (1, 7), (2, 7), (0, 8), (1, 8), (2, 8), (0, 9), (1, 9), (2, 9)]


def test_tuple_sort4():
    lst = [(2, 8), (0, 8), (0, 9), (1, 8), (2, 7), (0, 6), (2, 6), (0, 7), (1, 9), (1, 7), (1, 6), (2, 9)]
    sorted_1 = hf.tuple_sort(lst, tuple_index=1)
    sorted_0 = hf.tuple_sort(sorted_1, tuple_index=0)

    assert sorted_1 == [(0, 6), (2, 6), (1, 6), (2, 7), (0, 7), (1, 7), (2, 8), (0, 8), (1, 8), (0, 9), (1, 9), (2, 9)]
    assert sorted_0 == [(0, 6), (0, 7), (0, 8), (0, 9), (1, 6), (1, 7), (1, 8), (1, 9), (2, 6), (2, 7), (2, 8), (2, 9)]
