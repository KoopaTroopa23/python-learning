import csv
import logging
import sqlite3

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# ELT = Extract -> Load -> Transform
# Raw data goes into the database FIRST, then SQL cleans it.


# EXTRACT: read raw rows from the CSV (no cleaning here)
def extract(file_path):
    with open(file_path, "r", newline="") as file:
        return [(row["name"], row["access"]) for row in csv.DictReader(file)]


# LOAD: dump the raw rows into a staging table exactly as they came in
def load_raw(connection, rows):
    connection.execute("DROP TABLE IF EXISTS raw_access")
    connection.execute("CREATE TABLE raw_access (name TEXT, access TEXT)")
    connection.executemany("INSERT INTO raw_access VALUES (?, ?)", rows)


# TRANSFORM: SQL does the cleaning inside the database
def transform_in_sql(connection):
    connection.execute("DROP TABLE IF EXISTS clean_access")
    connection.execute("""
        CREATE TABLE clean_access AS
        SELECT TRIM(name) AS name,
               LOWER(TRIM(access)) AS access,
               CASE WHEN LOWER(TRIM(access)) = 'granted' THEN 1 ELSE 0 END AS has_access
        FROM raw_access
    """)


def main():
    connection = sqlite3.connect("access_control.db")
    rows = extract("app/etl/input_access.csv")   # E
    load_raw(connection, rows)                   # L
    transform_in_sql(connection)                 # T
    connection.commit()
    logger.info("clean_access: %s", connection.execute("SELECT * FROM clean_access").fetchall())
    connection.close()
    logger.info("ELT complete")


if __name__ == "__main__":
    main()
