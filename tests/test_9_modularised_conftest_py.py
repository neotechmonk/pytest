"""
    Automically imports imports fixtures from tests/conftest.py

    Conftest.py imports fixtures from other modules using pytest_plugins keyword
"""

import pytest
from src.aggregate import get_age_stat


@pytest.mark.parametrize("last_name, stat, result", [
    ('Thomas', 'mean',  33.5),
    ('Thomas', 'median', 32.5),
    ('Clark', 'mean', 37),
    ('Clark', 'median', 37)
])
def test_age_stats(process_data, clean_list_csv, last_name, stat, result):
    """
        process_data() is from tests/conftest.py
        clean_list_csv() is from tests/utils/assets.py
    """
    data = process_data(file_name_or_type = clean_list_csv)
    stat_result = get_age_stat(data, last_name, stat)
    assert stat_result == {'LastName': last_name, stat: result}
