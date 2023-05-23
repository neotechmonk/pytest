import os

import pytest
from src import data_processor


@pytest.fixture(scope="module")
def data_folder():
    yield 'tests/assets/'

@pytest.fixture(scope="module")
def process_data(data_folder):
    files = os.listdir(data_folder)

    def _file_type(file_name_or_type):
        for f in files:
            if file_name_or_type in f:
                if file_name_or_type.endswith(".json"):
                    data=data_processor.proces_json_data(data_folder+f)
                else:
                    data=data_processor.proces_csv_data(data_folder+f)
        return data
    yield _file_type

                
def test_headers_csv(process_data):
    data =  process_data(file_name_or_type="clean_list.csv")
    header = list(data[0].keys())
    assert header == ['FirstName', 'LastName', 'Age']

def test_headers_json(process_data):
    data =  process_data(file_name_or_type="clean_list.json")
    header = list(data[0].keys())
    assert header == ['FirstName', 'LastName', 'Age']


def test_malformed_csv_contents(process_data):
    with pytest.raises(ValueError) as exp:
        process_data(file_name_or_type="dirty_list.csv")
    
    assert str(exp.value) == "Invalid input: invalid literal for int() with base 10: ''"
   