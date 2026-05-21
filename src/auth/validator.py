from string import punctuation


def validate_password(password: str) -> bool:
    """Validate password strength and return True for valid passwords."""
    if not isinstance(password, str):
        raise ValueError("Password must be a string")

    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")

    if not any(char.isupper() for char in password):
        raise ValueError("Password must contain an uppercase letter")

    if not any(char.islower() for char in password):
        raise ValueError("Password must contain a lowercase letter")

    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain a digit")

    if not any(char in punctuation for char in password):
        raise ValueError("Password must contain a special character")

    return True
