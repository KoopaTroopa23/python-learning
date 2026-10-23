import sqlite3
import pandas as pd

# Same ETL as 01_extract_transform_load_csv.py, but with pandas.
# A DataFrame (df) is a table in memory: rows + named columns.


def main():
    # EXTRACT: read the CSV into a DataFrame
    df = pd.read_csv("app/etl/input_access.csv")
    print(df.head())   # first rows
    df.info()          # columns, types, missing values

    # TRANSFORM: whole-column operations, no loops needed
    df["name"] = df["name"].str.strip()
    df["access"] = df["access"].str.strip().str.lower()
    df["has_access"] = df["access"] == "granted"

    # Practice: filter rows and group
    print(df[df["has_access"]])                # only people with access
    print(df.groupby("access").size())         # count per access value

    # LOAD: to a CSV and to a SQL table
    df.to_csv("app/etl/output_access_pandas.csv", index=False)
    connection = sqlite3.connect("access_control.db")
    df.to_sql("users_pandas", connection, if_exists="replace", index=False)
    connection.close()
    print("Pandas ETL complete")


if __name__ == "__main__":
    main()
