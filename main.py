# Task 1.1: Iterative Binary Search

#Shared Link: https://prod.liveshare.vsengsaas.visualstudio.com/join?16278AEE607A319407EA256D4F0F82626C01

def binary_search(data: list[int], key: int) -> int:
    """
    Performs an iterative binary search on a sorted list.

    Args:
        data: A list of integers sorted in ascending order
        key: The integer value to search for

    Returns:
        The index of the element matching key, or -1 if not found
    """
    # TODO: Implement the iterative binary search algorithm
    # Remember: you cannot use built-in methods like .index()
    start = 0
    end = len(data) -1

    while start <= end:
        mid = (start + end) // 2
        if key == data[mid]:
            return mid
        elif key < data[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


# Task 1.2: Recursive Binary Searchtes

def binary_search_recursive(data: list[int], key: int, start: int, end: int) -> int:
    """
    Performs a recursive binary search on a sorted list.

    Args:
        data: A list of integers sorted in ascending order
        key: The integer value to search for
        start: The start index of the list segment to search
        end: The end index of the list segment to search

    Returns:
        The index of the element matching key, or -1 if not found
    """
    # TODO: Implement the recursive binary search algorithm
    # Remember: you cannot use built-in methods like .index()
    mid = (start + end) // 2
    if start > end:
        return -1

    if key == data[mid]:
        return mid
    elif key < data[mid]:
        end = mid - 1
    else:
        start = mid + 1
    return binary_search_recursive(data, key, start, end)
    


if __name__ == "__main__":  # DO NOT DELETE THIS LINE
    # Example usage - uncomment after implementing the functions
    data = [12, 22, 34, 41, 55]

    ## Test iterative binary search
    print(f"Searching for 34 in {data}:")
    print(f"  Iterative result: {binary_search(data, 34)}")
     # print(f"  Iterative result: {binary_search(data, 12)}")
     # print(f"  Iterative result: {binary_search(data, 44)}")
    print(f"  Recursive result: {binary_search_recursive(data, 34, 0, len(data) - 1)}")

    print(f"\nSearching for 100 in {data}:")
    print(f"  Iterative result: {binary_search(data, 100)}")
    print(f"  Recursive result: {binary_search_recursive(data, 100, 0, len(data) - 1)}")
    # Add any additional code you want to use for testing

