import pytest
from app import is_valid_niet_email

def test_valid_niet_email():
    assert is_valid_niet_email("student@niet.co.in") is True
    assert is_valid_niet_email("abc123@niet.co.in") is True
    assert is_valid_niet_email("NAME@NIET.CO.IN") is True  # case-insensitive

def test_invalid_email_domains():
    assert is_valid_niet_email("student@gmail.com") is False
    assert is_valid_niet_email("user@niet.ac.in") is False
    assert is_valid_niet_email("test@example.com") is False
    assert is_valid_niet_email("someone@niet.co") is False

def test_empty_and_none_like():
    assert is_valid_niet_email("") is False
    assert is_valid_niet_email(None) is False
