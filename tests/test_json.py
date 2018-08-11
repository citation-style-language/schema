import json
import pathlib

import pytest

"""
The following section defines pytest fixtures, which can be used as arguments
to tests, causing those tests to be run for all fixture values.
"""

root = pathlib.Path(__file__).parent.parent
json_paths = list(root.glob('*.json'))


@pytest.fixture(params=json_paths, ids=[x.name for x in json_paths])
def json_path(request):
    """
    Paths that correspond to JSON files
    """
    return root.joinpath(request.param)


@pytest.fixture(params=[
    'csl-citation.json',
    'csl-data.json',
])
def json_schema_path(request):
    """
    Paths that correspond to JSON schemas
    """
    return root.joinpath(request.param)


"""
The following section contains the tests.
"""


def test_read_json(json_path):
    """
    Test that a JSON file can be read into Python
    """
    text = json_path.read_text()
    json.loads(text)


def test_schema_property_specified(json_schema_path):
    """
    Test that JSON schemas set the $schema property
    """
    text = json_schema_path.read_text()
    schema = json.loads(text)
    schema['$schema']
