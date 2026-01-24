# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging 

### My Prompt:
> **Context**: I have python function supposed to sum all even numbers that I would like you to check and debug the ccode for me. Please be clear and concise with the code and double check it before showing it to me. 

>**Persona**: You are a senior python developer who have more than 30 year's experience in the field, and work with many different firms. 

>**Task**: Please provide the correct codes so that I can see the before and after. Identify the bugging line of the code. Please include example and test the code too. 

>**Format**: Provide it in code blocks and explain the code in short and concise as much as possible.

### Bugging Code
```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list."""
    total = 0
    for num in numbers:
        # BUG: This checks if the remainder is 1 (Odd), not 0 (Even)
        if num % 2 == 1:  
            total += num
    return total
```

### AI's fixed version of the code
```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list."""
    total = 0
    for num in numbers:
        # FIX: Check if remainder is 0
        if num % 2 == 0:  
            total += num
    return total
```
### Testing 
```python
test_list = [1, 2, 3, 4, 5, 6]
print(f"Sum of evens: {sum_of_evens(test_list)}") # Expected: 12 (2 + 4 + 6)
```

## Problem 2: Refactoring

### My Prompt:
>**Context**: I have a function that is working properly but it was unreadable function and it was so confusing. Please be specific and illustrate the point in the python code that neede assistance with. Additionally, please recheck the code onace again before showing the code. 

>**Persona**: You are a senior python developer who have more than 30 year's experience in the field, and work with many different firms. 

>**Task**: I would like you to help me make this python code more clearer in variable name, better iteration patterns, idiomatic, more easy to understand and readable. Please include examples and testing result of the code to make sure it is working properly.

>**Format**: I would like you to show me in code blocks. Make sure to identify the issue lying in the code that can be change to be concise. Moreover, please provides a basic explanations in bullets point. 

### Original Code
```python
def get_names_of_adults(users):
    results = []
    # ISSUE 1: iterating by index (range/len) is un-Pythonic and verbose
    for i in range(len(users)):
        # ISSUE 2: Repetitive lookup users[i] makes code "noisy"
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
    return results
```
### AI's fixed version of refactored code (Idiomatic)
```python
def get_names_of_adults(users):
    """Returns a list of names for users aged 18 or older."""
    # IMPROVEMENT: Direct iteration + List Comprehension
    return [user['name'] for user in users if user['age'] >= 18]
```
### Testing 
```python
test_users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 16},
    {"name": "Charlie", "age": 19},
    {"name": "David", "age": 12}
]

result = get_names_of_adults(test_users)
print(f"Adults found: {result}")
# Expected Output: ['Alice', 'Charlie']
```

## Problem 3: Documenting

### My Prompt:

>**Context**: I have python code that is working properly but currently it does not have a record documentation. Also, I would like to be easy to understand the information.

>**Persona**: You are a senior python developer who have more than 30 year's experience in the field, and work with many different firms. 

>**Task**: Could you please help write a clear, professonal, and NumPy-style docstring for this function. Please make sure to check the formats and every single details before showing it to me. Additionally, please double check the NumPy-style to make sure it is suitable for professional setting. Please include examples in the code.

>**Formats**: It has to be in NumPy-style docstring the provided function format and mention that the function raises a ValueError for invalid inputs.

### AI's fixed version of documented code
```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters
    ----------
    length : int or float
        The length of the rectangle. Must be a positive number.
    width : int or float
        The width of the rectangle. Must be a positive number.

    Returns
    -------
    int or float
        The calculated area (length * width).

    Raises
    ------
    ValueError
        If `length` or `width` is less than or equal to zero.

    Examples
    --------
    >>> calculate_area(10, 5)
    50
    >>> calculate_area(2.5, 4)
    10.0
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```


