### Prompts with AI
## Problem 1,2,3
- Using week04 folder, Could you please help me with the code that supposed to be implemented in lab04.py and I would like you to help me generate the code that will help find concise and right information. Additionally, please make sure to double check the codes and also explained it to me why this codes will be best fit in this scenarios. 

# AI's recommendation and reasoning
```python
def find_common_elements(list1, list2):
    """Find the common elements between two lists.

    This function should take two lists and return a new list containing
    only the elements that are present in both input lists. The final
    list can be in any order.

    Parameters
    ----------
    list1 : list
        The first list of elements.
    list2 : list
        The second list of elements.

    Returns
    -------
    list
        A list of elements common to both list1 and list2.
    """
    return list(set(list1) & set(list2))


def find_user_by_name(users, name):
    """Find a user's profile by name from a list of user data.

    Parameters
    ----------
    users : list of dict
        A list of dictionaries, where each dictionary represents a user
        and has 'name', 'age', and 'email' keys. It is recommended to
        convert this list into a more efficient data structure for lookups.
    name : str
        The name of the user to find.

    Returns
    -------
    dict or None
        The dictionary of the found user, or None if no user is found.
    """
    # Convert the list of dictionaries into a dictionary keyed by name for O(1) lookup
    user_dict = {user['name']: user for user in users}
    return user_dict.get(name, None)


def get_list_of_even_numbers(numbers):
    """Return a new list containing only the even numbers from the input list.

    The order of the numbers in the output list must be the same as the
    order of the even numbers in the input list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    list of int
        A new list containing only the even integers from the input list.
    """
    return [num for num in numbers if num % 2 == 0]
```
# Problem 1: Finding common items
- Set Intersection (&): Sets support the & operator which creates a mathematical intersection in O(n + m) time—much faster than nested loops O(n × m)
- Duplicate handling: If the input lists have duplicates, converting to sets automatically removes them, keeping only unique common elements
- Order doesn't matter: The problem explicitly states "order does not matter," making sets perfect since they're unordered
- Real-world benefit: For two large supplier lists, sets provide O(1) lookup time instead of O(n)

# Problem 2: User profile lookup
- O(1) Lookup: Dictionary lookups by key are constant time, vs O(n) for list iteration
- Key-Value mapping: Each username maps directly to their complete profile (name, age, email)
- Real-world scalability: When you have thousands of users, a dictionary lookup is orders of magnitude faster than iterating through the entire list
- Safe retrieval: Using .get() returns None if the user doesn't exist, which is exactly what the tests expect

# Problem 3: 
- Order preservation: Lists maintain insertion order, which the problem requires ("exact same order")
- Concise & readable: List comprehensions are Pythonic and express intent clearly—"get even numbers in order"
- Efficiency: One pass through the list with a simple condition check (O(n))
- Modulo operator: num % 2 == 0 is the standard way to test for even numbers


