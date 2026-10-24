import importlib.util
from pathlib import Path

import pandas as pd

_path = Path("app/etl/04_etl_parquet.py")
_spec = importlib.util.spec_from_file_location("etl_parquet", _path)
etl_parquet = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(etl_parquet)


def test_parquet_round_trip_preserves_data(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "app" / "etl").mkdir(parents=True)
    (tmp_path / "app" / "etl" / "input_access.csv").write_text(
        "name,access\nKevin,granted\nAddie,not granted\n"
    )

    etl_parquet.main()

    result = pd.read_parquet("app/etl/output_access_parquet", engine="pyarrow")
    assert len(result) == 2
    assert set(result["name"]) == {"Kevin", "Addie"}
    kevin_row = result[result["name"] == "Kevin"].iloc[0]
    assert bool(kevin_row["has_access"]) is True
