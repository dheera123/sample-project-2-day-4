import pytest
from src.auth.validator import validate_password


def test_valid_password():
    assert validate_password("SecurePass123!") is True


def test_missing_uppercase():
    with pytest.raises(ValueError) as exc_info:
        validate_password("weakpass123!")
    assert "Password must contain an uppercase letter" in str(exc_info.value)


def test_missing_lowercase():
    with pytest.raises(ValueError) as exc_info:
        validate_password("WEAKPASS123!")
    assert "Password must contain a lowercase letter" in str(exc_info.value)


def test_missing_digit():
    with pytest.raises(ValueError) as exc_info:
        validate_password("NoDigitsHere!")
    assert "Password must contain a digit" in str(exc_info.value)


def test_missing_special_character():
    with pytest.raises(ValueError) as exc_info:
        validate_password("NoSpecial123")
    assert "Password must contain a special character" in str(exc_info.value)


def test_too_short_password():
    with pytest.raises(ValueError) as exc_info:
        validate_password("Shrt1!")
    assert "Password must be at least 8 characters long" in str(exc_info.value)
