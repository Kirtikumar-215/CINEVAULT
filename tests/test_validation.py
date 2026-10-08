import pytest
from modules.validation import validate_rating, validate_year, validate_title

def test_valid_rating():
    assert validate_rating("4.5") == 4.5

def test_invalid_rating():
    with pytest.raises(ValueError):
        validate_rating("6")

def test_empty_title():
    with pytest.raises(ValueError):
        validate_title("")

def test_valid_year():
    assert validate_year("2025") == 2025
