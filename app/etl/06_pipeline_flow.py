import importlib.util
import logging
import os
from pathlib import Path

# Quiet Prefect's anonymous telemetry -- it's a background write to its own
# local SQLite file that can log a harmless "database is locked" error on
# short-lived runs like this script. Set before importing prefect so it
# takes effect for this process, regardless of machine or CI environment.
os.environ.setdefault("PREFECT_SERVER_ANALYTICS_ENABLED", "false")

from prefect import flow, task

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

# Reuse the plain functions from 01_extract_transform_load_csv.py -- the
# filename starts with a digit, so it can't be imported with a normal
# "import" statement (same trick tests/test_etl.py uses).
_path = Path(__file__).parent / "01_extract_transform_load_csv.py"
_spec = importlib.util.spec_from_file_location("etl_csv", _path)
_etl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_etl)


# A task is one unit of work in the pipeline. Wrapping it like this gives
# you retries, logging, and a visible run history for free -- the things a
# bare function call doesn't have.
@task(retries=2, retry_delay_seconds=1)
def extract_task(file_path):
    return _etl.extract(file_path)


@task
def transform_task(rows):
    return _etl.transform(rows)


@task
def load_task(file_path, rows):
    _etl.load(file_path, rows)
    return len(rows)


# A flow is the DAG: it calls tasks in order and Prefect tracks which task
# depends on which task's output.
@flow(name="access-control-etl")
def etl_flow(input_file="app/etl/input_access.csv", output_file="app/etl/output_access.csv"):
    raw_rows = extract_task(input_file)
    cleaned_rows = transform_task(raw_rows)
    row_count = load_task(output_file, cleaned_rows)
    return row_count


if __name__ == "__main__":
    etl_flow()
