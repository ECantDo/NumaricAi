# ======================================================================================================================
# SEARCH FUNCTIONS
# ======================================================================================================================

def binary_search_tuples(lst: list[tuple], key: int, tuple_index: int = 0) -> int:
    """
    Binary search for a tuple in a list
    :param lst: The list of tuples to search
    :param key: It's a key to search for
    :param tuple_index: The index within the tuple to search through
    :return:
    """
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if key == lst[mid][tuple_index]:
            return mid
        elif key < lst[mid][tuple_index]:
            end = mid - 1
        else:
            start = mid + 1

    return -1


def tuple_search(lst: list[tuple], key: int, tuple_index: int = 0) -> int:
    """
    Search for a tuple in a list
    :param lst: The list of tuples to search
    :param key: It's a key to search for
    :param tuple_index: The index within the tuple to search through
    :return:
    """
    for i in range(len(lst)):
        if key == lst[i][tuple_index]:
            return i
    return -1


# ======================================================================================================================
# SORT FUNCTIONS
# ======================================================================================================================

def tuple_sort(lst: list[tuple], tuple_index: int = 0) -> list[tuple]:
    """
    Sorts a list of tuples based on the first element of the tuple
    :param lst: The list of tuples to sort
    :param tuple_index: The index within the tuple to sort
    :return: The sorted list
    """
    return sorted(lst, key=lambda x: x[tuple_index])


# ======================================================================================================================
# EXISTENCE FUNCTIONS
# ======================================================================================================================
def tuple_exist(lst: list[tuple], key: int, tuple_index: int = 0, use_binary_search: bool = False) -> bool:
    """
    Checks if a tuple exists in a list
    :param use_binary_search: A flag to use binary search
    :param lst: The list of tuples to search
    :param key: It's a key to search for
    :param tuple_index: The index within the tuple to search through
    :return:
    """
    if use_binary_search:
        return binary_search_tuples(lst, key, tuple_index) != -1
    else:
        return tuple_search(lst, key, tuple_index) != -1
