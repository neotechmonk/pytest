"""
    1. Tests if correctly formatted csv import works in the happy path
    2. Test if malformed csv import is handled correctly
"""
import pytest
from src.data_processor import proces_csv_data


@pytest.fixture(scope="module")
def csv_filelocation_malformed():
    return "tests/assets/dirty_list.csv"


     
def test_malformed_csv_contents(csv_filelocation_malformed):
    with pytest.raises(ValueError) as exp:
        proces_csv_data(csv_filelocation_malformed)
    
    assert str(exp.value) == "Invalid input: invalid literal for int() with base 10: ''"
   