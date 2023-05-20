"""
    1. Data validation and exception handling
"""
import pytest
from src.person import Person


def test_person_initialization_nofirstname():
    with pytest.raises(ValueError) as exp:
        p1 = Person(first_name=None, last_name="Sanders", age=54)
    assert str(exp.value) == 'First and last names must have values'


def test_person_initialization_nolastname():
    with pytest.raises(ValueError) as exp:
        p1 = Person(first_name='Colonel', last_name="", age = 76)
    assert str(exp.value) == 'First and last names must have values'