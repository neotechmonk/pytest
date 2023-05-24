"""
    Automically imports imports fixtures from tests/conftest.py

    The below has been migrated to tests/conftest.py
    @pytest.fixture(scope="module")
    def data_folder():
        yield 'tests/assets/'
"""

import os

import pytest
from src import data_processor
from src.aggregate import get_age_stat


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


@pytest.mark.parametrize("last_name, stat, result", [
    ('Thomas', 'mean',  33.5),
    ('Thomas', 'median', 32.5),
    ('Clark', 'mean', 37),
    ('Clark', 'median', 37)
])
def test_age_stats(process_data, last_name, stat, result):
    data = process_data(file_name_or_type = "clean_list.csv")
  
    stat_result = get_age_stat(data, last_name, stat)
    assert stat_result == {'LastName': last_name, stat: result}
