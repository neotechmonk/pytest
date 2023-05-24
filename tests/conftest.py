
import pytest


@pytest.fixture(scope="module")
def data_folder():
    yield 'tests/assets/'
