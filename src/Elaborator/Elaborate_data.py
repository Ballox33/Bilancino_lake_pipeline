import pandas as pd
from sqlalchemy import create_engine
from config import *


def load_data(base_file_path):
    try:
        available_years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
        my_list = []

        for year in available_years:
            file_path = f"{base_file_path}{year}.csv"
            data = pd.read_csv(file_path, sep=";")
            my_list.append(data)

        df = pd.concat(my_list, ignore_index=True)
        return df

    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def connect_to_db(user, password, host, port, db_name):
    try:
        engine = create_engine(
            f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"
        )
        return engine

    except Exception as e:
        print(f"Error connecting to DB: {e}")
        return None

def write_to_db(engine, dataframe, table_name):
    if engine is None or dataframe is None:
        print("Engine or DataFrame is None, aborting.")
        return False

    try:
        dataframe.to_sql(
            table_name,
            engine,
            if_exists="append",
            index=False
        )

        print(f"Data successfully written to '{table_name}'")
        return True

    except Exception as e:
        print(f"Error writing to DB: {e}")
        return False


def main():
    print("Starting pipeline...")

    df = load_data(BASE_FILE_PATH)

    engine = connect_to_db(
        PG_USER,
        PG_PASSWORD,
        PG_HOST,
        PG_PORT,
        DB_NAME
    )

    write_to_db(engine, df, TABLE_NAME)


if __name__ == "__main__":
    main()