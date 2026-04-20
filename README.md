# Assignment: Binary Search and Testing

In this assignment, I wrote tests for binary search functions before implementing them.

## Instructions given by the tutor

1. Each student in the pair should accept the assignment to be added to the repository.
2. In each pair, only one student creates a codespace.
3. Click **Live Share** icon in the codespace status bar (at the bottom)  
   ![Live Share](images/image1.png)
4. The status will change to **Shared** and a window will appear:  
   ![Live Share Window](images/image2.png)
5. Copy the link and share it with your programming partner to start collaborating
6. The programming partner should click on the link, then click **Accept read-write** to proceed.

---

## Part 1: Write Your Tests

Open `test_main.py` and write test functions for both binary search algorithms.

You will use the `assert` keyword to write tests. The `assert` keyword follows the syntax pattern `assert <expression>`. If the expression evaluates to `True`, nothing happens. If the expression evaluates to `False`, an `AssertionError` is raised.

### Example

```python
assert 1 == 2
# AssertionError
```

This will raise an `AssertionError`. To add an error message to the error, include the message after the assert statement, separated by a comma:

```python
assert 1 == 2, "1 is not equal to 2"
# AssertionError: 1 is not equal to 2
```

When testing a function, compare the return value from the function against the expected value:

```python
return_value = function(argument1, argument2, ...)
assert return_value == expected_result, f"function(argument1, argument2, ...): expected {expected_result}, Actual: {return_value}"
```

### Conventions

1. **Function names start with `test_`** and describe what is being tested
2. **Test coverage**: your tests should cover normal cases (both positive and negative outcomes), edge cases, and abnormal cases (invalid input)

| Normal Cases            | Edge Cases                 | Abnormal Cases |
|-------------------------|----------------------------|----------------|
| Element in middle       | Empty list                 | Not a list     |
| Element at start        | Single element (found)     |                |
| Element at end          | Single element (not found) |                |
| Even number of elements | Element not present        |                |
| Odd number of elements  |                            |                |


---

## Part 2: Implement the Functions

After writing your tests, implement the functions in `main.py`.

### Task 1.1:

Function interface: `binary_search(data: list[int], key: int) -> int`

- Accepts `data` (sorted list of integers) and `key` (integer to find)
- Uses an **iterative** approach (loop, not recursion)
- Returns the index of `key` in `data`, or `-1` if not found
- **No built-in methods allowed** (e.g., no `.index()`)

### Task 1.2:

Function interface: `binary_search_recursive(data: list[int], key: int, start: int, end: int) -> int`

- Accepts `data`, `key`, `start`, and `end` indices
- Uses a **recursive** approach
- Returns the index of `key` in `data`, or `-1` if not found
- **No built-in methods allowed**

---

## Running Your Work

1. Write tests in `test_main.py`
2. Run `python test_main.py` (tests will fail initially)
3. Implement the functions in `main.py`
4. Run `python test_main.py` again (tests should pass)
5. Optionally run `python main.py` to test manually

---

# Submission

Before submitting:
1. All tests in `test_main.py` are complete
2. Running `python test_main.py` shows all tests pass
3. Both functions in `main.py` are implemented
4. Push your code to GitHub
