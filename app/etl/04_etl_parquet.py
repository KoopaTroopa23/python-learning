import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# Parquet is a columnar binary format: it stores each column contiguously
# and keeps the schema (column names + types) inside the file itself, so
# reads can be much faster and smaller than CSV, especially when you only
# need a few columns out of many.


def main():
    # EXTRACT: same raw CSV as the other ETL scripts
    df = pd.read_csv("app/etl/input_access.csv")

    # TRANSFORM: same cleaning as 03_etl_pandas.py
    df["name"] = df["name"].str.strip()
    df["access"] = df["access"].str.strip().str.lower()
    df["has_access"] = df["access"] == "granted"

    # LOAD: write as Parquet, partitioned by "access" -- this creates one
    # subfolder per distinct access value (e.g. access=granted/, access=not
    # granted/), which is how large datasets get split into smaller files
    # that a query engine can skip over entirely if it doesn't need them.
    output_dir = "app/etl/output_access_parquet"
    df.to_parquet(output_dir, engine="pyarrow", partition_cols=["access"], index=False)
    logger.info("wrote %d rows to %s, partitioned by access", len(df), output_dir)

    # Read it back to prove the round trip preserves data and types.
    result = pd.read_parquet(output_dir, engine="pyarrow")
    logger.info("read back %d rows:\n%s", len(result), result.dtypes)

    logger.info("Parquet ETL complete")


if __name__ == "__main__":
    main()
