import importlib.util
from pathlib import Path

import pandas as pd
import pandera.pandas as pa

_path = Path("app/etl/05_data_quality.py")
_spec = importlib.util.spec_from_file_location("data_quality", _path)
data_quality = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(data_quality)


def test_clean_data_passes_schema():
    df = data_quality.clean(
        pd.DataFrame([{"name": " Kevin ", "access": " Granted "}])
    )
    # Should not raise
    data_quality.access_schema.validate(df, lazy=True)


def test_blank_name_fails_schema():
    df = pd.DataFrame([{"name": "", "access": "granted", "has_access": True}])
    try:
        data_quality.access_schema.validate(df, lazy=True)
        assert False, "expected a SchemaErrors to be raised"
    except pa.errors.SchemaErrors as err:
        assert len(err.failure_cases) >= 1


def test_invalid_access_value_fails_schema():
    df = pd.DataFrame([{"name": "Sam", "access": "maybe", "has_access": False}])
    try:
        data_quality.access_schema.validate(df, lazy=True)
        assert False, "expected a SchemaErrors to be raised"
    except pa.errors.SchemaErrors as err:
        assert len(err.failure_cases) >= 1
