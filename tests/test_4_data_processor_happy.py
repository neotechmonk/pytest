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

def test_contents(read_csv_data):
    data =  read_csv_data

    # Last record
    assert list(data[-1].values()) == ['Kevin', 'King', 21]

    # First record
    assert list(data[0].values()) == ['John', 'Doe', 25]

    # Random data check 
    assert data[10]['FirstName'] == 'Daniel'
    assert data[19]['LastName'] == 'Adams'

    # type check
    for row in data:
        assert isinstance(row['FirstName'], str)
        assert isinstance(row['LastName'], str)
        assert isinstance(row['Age'], int)

 


