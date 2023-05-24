import pytest


@pytest.fixture(scope="module")
def data_folder():
    yield 'tests/assets/'

@pytest.fixture(scope="module")
def clean_list_csv(data_folder):
    yield "clean_list.csv"

@pytest.fixture(scope="module")
def dirty_list_csv(data_folder):
    yield "dirty_list.csv"

pytest.fixture(scope="module")
def clean_list_json(data_folder):
    yield "clean_list.json"
