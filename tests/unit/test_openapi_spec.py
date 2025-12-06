import os
from typing import Any
import yaml
from openapi_spec_validator import validate_spec


def test_openapi_spec_is_valid():
    root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    spec_path = os.path.join(root, 'docs', 'api', 'openapi.yaml')
    assert os.path.exists(spec_path), 'openapi.yaml not found'
    with open(spec_path, 'r', encoding='utf-8') as f:
        spec = yaml.safe_load(f)
    validate_spec(spec)

