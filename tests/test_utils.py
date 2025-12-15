import json

import pytest

from src.utils import create_objects
from src.utils import read_json


@pytest.fixture
def sample_json():
    return [
        {
            "name": "Category1",
            "description": "Description1",
            "products": [{"name": "Product1", "description": "Description1", "price": 10.0, "quantity": 5}],
        },
        {
            "name": "Category2",
            "description": "Description2",
            "products": [{"name": "Product2", "description": "Description2", "price": 20.0, "quantity": 3}],
        },
    ]


def test_read_json_with_tmp(tmp_path):
    test_file = tmp_path / "test_file_json"

    data = [{"key_1": "value_1", "number": 123}, {"key_2": "value_2", "number": 456}]
    with open(test_file, "w") as f:
        json.dump(data, f)

    result = read_json(str(test_file))
    assert result == data


def test_create_objects(sample_json):
    categories = create_objects(sample_json)
    assert len(categories) == 2
    assert categories[0].name == "Category1"
    assert categories[0].products_ret[0].name == "Product1"
    assert categories[1].name == "Category2"
    assert categories[1].products_ret[0].name == "Product2"
