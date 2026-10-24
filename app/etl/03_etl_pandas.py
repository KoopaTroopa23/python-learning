import logging
import sqlite3
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# Same ETL as 01_extract_transform_load_csv.py, but with pandas.
# A DataFrame (df) is a table in memory: rows + named columns.


def main():
    # EXTRACT: read the CSV into a DataFrame
    df = pd.read_csv("app/etl/input_access.csv")
    logger.info("loaded %d rows\n%s", len(df), df.head())

    # TRANSFORM: whole-column operations, no loops needed
    df["name"] = df["name"].str.strip()
    df["access"] = df["access"].str.strip().str.lower()
    df["has_access"] = df["access"] == "granted"

    # Practice: filter rows and group
    logger.info("users with access:\n%s", df[df["has_access"]])
    logger.info("count per access value:\n%s", df.groupby("access").size())

    # LOAD: to a CSV and to a SQL table
    df.to_csv("app/etl/output_access_pandas.csv", index=False)
    connection = sqlite3.connect("access_control.db")
    df.to_sql("users_pandas", connection, if_exists="replace", index=False)
    connection.close()
    logger.info("Pandas ETL complete")


if __name__ == "__main__":
    main()
