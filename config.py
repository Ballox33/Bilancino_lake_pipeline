import os
from dotenv import load_dotenv

load_dotenv()

DATA_2025_URL = "https://data.comune.fi.it/datastore/download.php?id=7752&type=99&format=url&file_format=csv&file_id=22717"
DATA_2025_PATH = "Data/livelli_bilancino_2025.csv"
DATA_2026_URL = "https://data.comune.fi.it/datastore//download.php?id=7832&type=99&format=url&file_format=csv&file_id=22958"
DATA_2026_PATH = "Data/livelli_bilancino_2026.csv"
BASE_FILE_PATH = "Data/livelli_bilancino_"
PG_USER = "metabase_user" 
PG_PASSWORD = os.getenv("METABASE_PSW")
PG_HOST = "localhost"
PG_PORT = 5432
DB_NAME = "bilancino"
TABLE_NAME = "livelli"