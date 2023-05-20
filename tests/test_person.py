from src.person import Person


def test_person_initialization_nofirstname():
    p1 = Person(first_name=None, last_name="Sanders")

def test_full_name():
    p1 = Person("Adam", "Sanders")
    assert p1.get_full_name() == "Adam Sanders"
