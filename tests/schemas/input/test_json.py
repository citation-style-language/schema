import json
import pathlib

import jsonschema

import pytest

"""
The following section defines pytest fixtures, which can be used as arguments
to tests, causing those tests to be run for all fixture values.
"""

root = pathlib.Path(__file__).parent.parent.parent.parent
json_paths = list(root.glob('**/*.json'))


@pytest.fixture(params=json_paths, ids=[x.name for x in json_paths])
def json_path(request):
    """
    Paths that correspond to JSON files.
    """
    return root.joinpath(request.param)


@pytest.fixture(params=[
    'schemas/input/csl-citation.json',
    'schemas/input/csl-data.json',
])
def json_schema(request):
    """
    JSON objects that correspond to JSON schemas.
    """
    path = root.joinpath(request.param)
    text = path.read_text()
    schema = json.loads(text)
    return schema


@pytest.fixture
def csl_data_validator():
    text = root.joinpath('schemas/input/csl-data.json').read_text()
    schema = json.loads(text)
    Validator = jsonschema.validators.validator_for(schema)
    return Validator(schema)


@pytest.fixture
def csl_citation_validator():
    text = root.joinpath('schemas/input/csl-citation.json').read_text()
    schema = json.loads(text)
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


def test_basic_citation_schema_validates(csl_citation_validator):
    cite = {
      "schema": "https://resource.citationstyles.org/schema/latest/input/json/csl-citation.json",
      "citationID": "item1",
      "citationItems": [
          {
            "id": "item1",
            "itemData": {
            "id": "item1",
            "type": "book",
            "title": "test title"
          }
        }
      ]
    }
    csl_citation_validator.validate(cite)


def test_basic_data_schema_with_author_validates(csl_data_validator):
    csl = [{
        'id': 'example-id',
        'type': 'report',
        "author": [
            {"given": "Jane", "family": "Roe"},
            {"literal": "John Doe"}
        ],
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

def test_data_schema_with_empty_date_parts(csl_data_validator):
    """
    empty arrays in date-parts can cause downstream citeproc failures
    https://github.com/citation-style-language/schema/pull/158
    """
    csl = [{
        'id': 'example-id',
        'type': 'report',
        'issued': {
            "date-parts": []
        },
    }]
    with pytest.raises(jsonschema.exceptions.ValidationError):
        csl_data_validator.validate(csl)
