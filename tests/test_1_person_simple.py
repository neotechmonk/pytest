"""
    1. Simple assert - happy
    2. Simple assert - sad

"""
from src.person import Person


def test_full_name():
    p1 = Person("Adam", "Sanders")
    assert p1.get_full_name() == "Adam Sanders"
