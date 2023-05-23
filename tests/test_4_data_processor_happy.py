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
     

def test_csv_file_reads(read_csv_data):
    data =  read_csv_data
    assert len(data) > 0
