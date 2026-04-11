import os

def check_etl_files():
    files = [
        "app/etl/input_access.csv",
        "app/etl/output_access.csv"
    ]
    
    for file in files:
        if os.path.exists(file):
            size = os.path.getsize(file)
            print(f"{file} exists | size: {size} bytes")
        else:
            print(f"{file} is missing!")

check_etl_files()