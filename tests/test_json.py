import json
import pathlib

import jsonref
import jsonschema

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
    Paths that correspond to JSON files.
    """
    return root.joinpath(request.param)


@pytest.fixture(params=[
    'csl-citation.json',
    'csl-data.json',
])
def json_schema(request):
    """
    JSON objects that correspond to JSON schemas.
    """
    path = root.joinpath(request.param)
    text = path.read_text()
    # Dereference schemas as workaround for https://github.com/Julian/jsonschema/issues/447
    schema = jsonref.loads(text, jsonschema=True)
    return schema


@pytest.fixture
def csl_data_validator():
    text = root.joinpath('csl-data.json').read_text()
    schema = jsonref.loads(text, jsonschema=True)
    Validator = jsonschema.validators.validator_for(schema)
    return Validator(schema)


"""
The following section contains the tests.
"""


def test_read_json(json_path):
    """
    Test that a JSON file can be read into Python.
    """
    text = json_path.read_text()
    json.loads(text)


def test_schema_property_specified(json_schema):
    """
    Test that JSON schemas set the $schema property.
    https://json-schema.org/understanding-json-schema/reference/schema.html
    https://github.com/citation-style-language/schema/pull/153
    """
    json_schema['$schema']


def test_schema_is_valid(json_schema):
    """
    Infer the JSON Schema draft from $schema and then check that the input
    schema is valid.
    """
    Validator = jsonschema.validators.validator_for(json_schema)
    Validator.check_schema(json_schema)


def test_basic_data_schema_validates(csl_data_validator):
    csl = [{
        'id': 'example-id',
        'type': 'report',
    }]
    csl_data_validator.validate(csl)


def test_data_schema_with_extra_property_fails(csl_data_validator):
    csl = [{
        'id': 'example-id',
        'type': 'report',
        'not-a-csl-key': None,
    }]
    with pytest.raises(jsonschema.exceptions.ValidationError):
        csl_data_validator.validate(csl)
