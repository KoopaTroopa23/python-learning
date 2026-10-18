import importlib.util
from pathlib import Path

# The ETL file name starts with a digit, so a normal import can't load it.
path = Path("app/etl/01_extract_transform_load_csv.py")
spec = importlib.util.spec_from_file_location("etl_csv", path)
etl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(etl)


def test_transform_cleans_spaces_and_case():
    rows = [{"name": " Chloe ", "access": " Granted "}]
    result = etl.transform(rows)
    assert result == [{"name": "Chloe", "access": "granted", "has_access": True}]


def test_transform_not_granted_is_false():
    rows = [{"name": "Addie", "access": "not granted"}]
    assert etl.transform(rows)[0]["has_access"] is False


def test_extract_and_load_round_trip(tmp_path):
    source = tmp_path / "in.csv"
    source.write_text("name,access\nKevin,granted\n")
    rows = etl.extract(str(source))
    assert rows == [{"name": "Kevin", "access": "granted"}]

    out = tmp_path / "out.csv"
    etl.load(str(out), etl.transform(rows))
    assert out.read_text().splitlines() == [
        "name,access,has_access",
        "Kevin,granted,True",
    ]
