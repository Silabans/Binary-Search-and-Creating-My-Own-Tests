"""
Test file for binary search functions.

Write your test functions using assert statements.

Your tests should:
- Start with 'test_'
- Be descriptive of what is being tested
- Use assert statements to verify correctness
- Cover normal cases and edge cases
"""

from main import binary_search, binary_search_recursive

# =============================================================================
# Tests for binary_search (iterative)
# =============================================================================

# Normal Cases

def test_binary_search_element_in_middle():
    """Test that binary_search finds an element in the middle of the list"""
    # Write your test here
    element_index = binary_search([1, 2, 3], 2)
    assert element_index == 1, "Index of the middle element does not match the returned index"


def test_binary_search_element_at_start():
    """Test that binary_search finds an element at the start of the list"""
    # Write your test here
    element_index = binary_search([1, 2, 3], 1)
    assert element_index == 0, "Index of the starting element does not match the returned index"


def test_binary_search_element_at_end():
    """Test that binary_search finds an element at the end of the list"""
    # Write your test here
    element_index = binary_search([1, 2, 3], 3)
    assert element_index == 2, "Index of the final element does not match the returned index"


def test_binary_search_even_number_of_elements():
    """Test binary_search with a list having an even number of elements"""
    # Write your test here
    element_index = binary_search([1, 2, 3, 4], 2)
    # Data list has an even number of elements
    assert element_index == 1, "Index does not match; Even number of elements"


def test_binary_search_odd_number_of_elements():
    """Test binary_search with a list having an odd number of elements"""
    # Write your test here
    element_index = binary_search([1, 2, 3], 2)
    assert element_index == 1, "Index does not match; Odd number of elements"


# Abnormal/Edge Cases

def test_binary_search_empty_list():
    """Test binary_search with an empty list"""
    # Write your test here
    returned_value = binary_search([], 2)
    assert returned_value == -1, "The value returned should be -1 as the list is empty"


def test_binary_search_single_element_found():
    """Test binary_search with a single element list - element found"""
    # Write your test here
    returned_value = binary_search([1], 1)
    assert returned_value == 0, "Index does not match; list has a single element"


def test_binary_search_single_element_not_found():
    """Test binary_search with a single element list - element not found"""
    # Write your test here
    returned_value = binary_search([1], 2)
    assert returned_value == -1, "The returned value should be -1 as the key is not found; list has a single element"


def test_binary_search_element_not_present():
    """Test binary_search when the element is not in the list"""
    # Write your test here
    returned_value = binary_search([1, 4, 5], 2)
    assert returned_value == -1, "The returned value should be -1 as the key is not found"


# =============================================================================
# Tests for binary_search_recursive
# =============================================================================

# Normal Cases

def test_recursive_element_in_middle():
    """Test that binary_search_recursive finds an element in the middle"""
    # Write your test here
    returned_value = binary_search_recursive([1, 2, 3], 2, 0, 2)
    assert returned_value == 1, "Index does not match; element is in the middle"


def test_recursive_element_at_start():
    """Test that binary_search_recursive finds an element at the start"""
    # Write your test here
    returned_value = binary_search_recursive([1, 2, 3], 1, 0, 2)
    assert returned_value == 0, "Index does not match; element is at the start"


def test_recursive_element_at_end():
    """Test that binary_search_recursive finds an element at the end"""
    # Write your test here
    returned_value = binary_search_recursive([1, 2, 3], 3, 0, 2)
    assert returned_value == 2, "Index does not match; element is at the end"


def test_recursive_even_number_of_elements():
    """Test binary_search_recursive with even number of elements"""
    # Write your test here
    returned_value = binary_search_recursive([1, 2, 3, 4], 2, 0, 3)
    assert returned_value == 1, "Index does not match; number of elements is even"


def test_recursive_odd_number_of_elements():
    """Test binary_search_recursive with odd number of elements"""
    # Write your test here
    returned_value = binary_search_recursive([1, 2, 3], 2, 0, 2)
    assert returned_value == 1, "Index does not match; number of elements is odd"


# Abnormal/Edge Cases

def test_recursive_empty_list():
    """Test binary_search_recursive with an empty list"""
    # Write your test here
    returned_value = binary_search_recursive([], 2, 0, -1)
    assert returned_value == -1, "The value returned should be -1 as the list is empty"


def test_recursive_single_element_found():
    """Test binary_search_recursive with single element - found"""
    # Write your test here
    returned_value = binary_search_recursive([2], 2, 0, 0)
    assert returned_value == 0, "The value returned should be 0 as there is only one element in the list"

def test_recursive_single_element_not_found():
    """Test binary_search_recursive with single element - not found"""
    # Write your test here
    returned_value = binary_search_recursive([2], 1, 0, 0)
    assert returned_value == -1, "The value returned should be -1 as the element is not within the list; the list has a single element"


def test_recursive_element_not_present():
    """Test binary_search_recursive when element is not present"""
    # Write your test here
    returned_value = binary_search_recursive([2, 3, 4], 1, 0, 2)
    assert returned_value == -1, "The value returned should be -1 as the element is not within the list"



# =============================================================================
# Test Runner
# =============================================================================

if __name__ == '__main__':
    tests = [
        test_binary_search_element_in_middle,
        test_binary_search_element_at_start,
        test_binary_search_element_at_end,
        test_binary_search_even_number_of_elements,
        test_binary_search_odd_number_of_elements,
        test_binary_search_empty_list,
        test_binary_search_single_element_found,
        test_binary_search_single_element_not_found,
        test_binary_search_element_not_present,
        test_recursive_element_in_middle,
        test_recursive_element_at_start,
        test_recursive_element_at_end,
        test_recursive_even_number_of_elements,
        test_recursive_odd_number_of_elements,
        test_recursive_empty_list,
        test_recursive_single_element_found,
        test_recursive_single_element_not_found,
        test_recursive_element_not_present,
    ]

    print(f"Running {len(tests)} tests...\n")

    passed = 0
    failed = 0

    for test_func in tests:
        try:
            test_func()
            print(f"[PASS] {test_func.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"[FAIL] {test_func.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"[FAIL] {test_func.__name__}: Error - {e}")
            failed += 1

    print(f"\n{'='*40}")
    print(f"Results: {passed} passed, {failed} failed")

    if failed == 0:
        print("All tests passed!")
    else:
        print(f"\n{failed} test(s) failed. Please fix and try again.")
