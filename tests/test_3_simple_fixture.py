"""
    1. Initialise a Person as fixture
    2. Run simple tests for name age
"""
import pytest
from src.person import Person


@pytest.fixture (scope="function")
def adult_person():  
    return Person(first_name="Bob", last_name="Marley", age= 66)
    
@pytest.fixture (scope="function")
def under_aged_person():  
    return Person(first_name="Justin", last_name="Bieber", age= 17)
  
def test_person_fullname(adult_person):
    assert adult_person.get_full_name() =="Bob Marley"

def test_person_age(adult_person):
    assert adult_person.get_age() ==66

def test_person_isadult(adult_person):
    assert adult_person.is_adult() ==True

def test_person_isnotadult(under_aged_person):
    assert under_aged_person.is_adult() ==False




