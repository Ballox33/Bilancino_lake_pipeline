import os
from secret import SECRET_PG_PASSWORD

DATA_2025_URL = "https://data.comune.fi.it/datastore/download.php?id=7752&type=99&format=url&file_format=csv&file_id=22717"
DATA_2025_PATH = "Data/livelli_bilancino_2025.csv"
BASE_FILE_PATH = "Data/livelli_bilancino_"
PG_USER = "giacomo" 
PG_PASSWORD = SECRET_PG_PASSWORD
PG_HOST = "localhost"
PG_PORT = 5432
DB_NAME = "bilancino"
TABLE_NAME = "livelli"