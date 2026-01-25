import pandas as pd
from sqlalchemy import create_engine, text
import psycopg2
import sys
from config import *
def load_data(base_file_path):
    try:
        available_years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
        my_list = []
        for i in available_years:
            data = pd.read_csv(base_file_path + str(i) + ".csv", sep=";")
            my_list.append(data)
        my_dataframe = pd.concat(my_list, ignore_index=True)
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
        return None
    return my_dataframe

def connect_to_db(pg_user, pg_password, pg_host, pg_port, db_name):
    try:
        engine = create_engine(f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}:{pg_port}/postgres')
        with engine.connect() as conn:
            conn.execute(text(f'commit'))
            result = conn.execute(text(f"SELECT 1 FROM pg_database WHERE datname='{db_name}'"))
            exists = result.scalar()
            if not exists:
                conn.execute(text(f'CREATE DATABASE {db_name}'))
                print(f"Database '{db_name}' creato!")
        engine = create_engine(f"postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{db_name}")
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")
        return None
    return engine

def write_to_db(engine, dataframe, table_name):
    if engine is None or dataframe is None:
        print("Engine or DataFrame is None, aborting write.")
        return False
    try:
        dataframe.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data successfully written to table '{table_name}'")
    except Exception as e:
        print(f"An error occurred while writing data to the database: {e}")
        return False
    return True



def main():
    base_file_path = BASE_FILE_PATH
    data_2025_path = DATA_2025_PATH
    data_2025_url = DATA_2025_URL
    pg_user = PG_USER 
    pg_password = PG_PASSWORD
    pg_host = PG_HOST
    pg_port = PG_PORT
    db_name = DB_NAME
    table_name = TABLE_NAME

    print("This is the starting point..")

    my_dataframe = load_data(base_file_path)
    engine = connect_to_db(pg_user, pg_password, pg_host, pg_port, db_name)
    write_to_db(engine, my_dataframe, table_name)


    

if __name__ == "__main__":
    main()
