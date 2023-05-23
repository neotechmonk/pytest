"""
    1. Tests if correctly formatted csv import works in the happy path
    2. Test if malformed csv import is handled correctly
"""
import pytest
from src.data_processor import proces_csv_data


@pytest.fixture(scope="module")
def csv_filelocation():
    return "tests/assets/clean_list.csv"

@pytest.fixture(scope="module")
def read_csv_data(csv_filelocation):
    yield proces_csv_data(csv_filelocation)
     

def test_row_count(read_csv_data):
    data =  read_csv_data
    assert len(data) ==29 #30 with headers

def test_headers(read_csv_data):
    data =  read_csv_data
    header = list(data[0].keys())
    assert header == ['FirstName', 'LastName', 'Age']

