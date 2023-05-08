import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

LOGENTRIES_FILENAME = os.getenv("EXERCISES_FILENAME") or "logentries.csv"
LOGENTRIES_FILE_PATH = os.path.join(dirname, "..", "data", LOGENTRIES_FILENAME)

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)
