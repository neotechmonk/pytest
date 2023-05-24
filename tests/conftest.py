
import os

import pytest
from src import data_processor

pytest_plugins = [
    "tests.utils.assets",
]

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
