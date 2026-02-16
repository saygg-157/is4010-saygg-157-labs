users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False}
]


def calculate_average_age(users):
    """
    Calculate the average age of users with valid integer ages.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries, each containing an optional 'age' key.

    Returns
    -------
    float
        The average age of users with integer ages. Returns 0.0 if no valid
        ages are found or the list is empty.

    Notes
    -----
    Only considers ages that are integers. Non-integer values and users
    without an 'age' key are skipped gracefully. Handles empty lists,
    None values, and type errors without crashing.
    """
    try:
        # Validate input
        if users is None:
            print("error: cannot calculate average age of None.")
            return 0.0
        if not isinstance(users, list):
            print("error: expected a list of user dictionaries.")
            return 0.0

        # Filter for valid integer ages
        valid_ages = [
            user.get("age") for user in users
            if isinstance(user, dict) and isinstance(user.get("age"), int)
        ]

        # Handle empty age list
        if not valid_ages:
            print("error: cannot calculate average age of an empty list.")
            return 0.0

        return sum(valid_ages) / len(valid_ages)

    except (ZeroDivisionError, TypeError) as e:
        print(f"error: cannot calculate average age - {type(e).__name__}: {e}")
        return 0.0


def get_active_user_emails(users):
    """
    Get email addresses of all active users.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries, each potentially containing 'is_active'
        and 'email' keys.

    Returns
    -------
    list of str
        Email addresses of users where 'is_active' is True and 'email'
        is present. Returns an empty list if no active users with emails
        are found or the input list is empty.

    Notes
    -----
    Users must have 'is_active' set to True and a non-empty 'email' value
    to be included. Missing keys or null values are handled gracefully.
    Handles empty lists, None values, type errors, and malformed data
    without crashing.
    """
    try:
        # Validate input
        if users is None:
            print("error: cannot retrieve active user emails from None.")
            return []
        if not isinstance(users, list):
            print("error: expected a list of user dictionaries.")
            return []

        # Filter for active users with valid emails
        active_emails = [
            user.get("email") for user in users
            if isinstance(user, dict) and user.get("is_active") and user.get("email")
        ]

        return active_emails

    except (KeyError, TypeError, AttributeError) as e:
        print(f"error: cannot retrieve active user emails - {type(e).__name__}: {e}")
        return []


if __name__ == '__main__':
    avg_age = calculate_average_age(users)
    print(f"average user age: {avg_age:.2f}")

    active_emails = get_active_user_emails(users)
    print(f"active user emails: {active_emails}")