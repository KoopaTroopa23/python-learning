import logging
import pandas as pd
import pandera.pandas as pa
from pandera import Column, Check

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# A schema describes what "clean" data must look like. Running data through
# it catches bad rows before they reach a database or downstream report,
# instead of finding out later that something silently broke.
access_schema = pa.DataFrameSchema(
    {
        "name": Column(str, Check.str_length(min_value=1), nullable=False),
        "access": Column(str, Check.isin(["granted", "not granted"]), nullable=False),
        "has_access": Column(bool, nullable=False),
    }
)


def clean(df):
    df = df.copy()
    df["name"] = df["name"].str.strip()
    df["access"] = df["access"].str.strip().str.lower()
    df["has_access"] = df["access"] == "granted"
    return df


def main():
    df = clean(pd.read_csv("app/etl/input_access.csv"))

    try:
        access_schema.validate(df, lazy=True)
        logger.info("validation passed: %d rows are clean", len(df))
    except pa.errors.SchemaErrors as err:
        logger.error("validation failed:\n%s", err.failure_cases)

    # Show what a validation failure looks like, using a row a CSV could
    # realistically contain: a blank name and a typo'd access value.
    bad_df = pd.concat(
        [df, pd.DataFrame([{"name": "", "access": "granted", "has_access": True},
                            {"name": "Sam", "access": "maybe", "has_access": False}])],
        ignore_index=True,
    )
    try:
        access_schema.validate(bad_df, lazy=True)
    except pa.errors.SchemaErrors as err:
        logger.warning("expected failure caught, %d bad row(s) found:\n%s",
                        len(err.failure_cases), err.failure_cases)


if __name__ == "__main__":
    main()
