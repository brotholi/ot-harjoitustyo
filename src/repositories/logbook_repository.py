import json
from config import EXERCISES_FILE_PATH


class LogbookRepository:

    def __init__(self, file_path):
        self._file_path = file_path

    def find_all(self):

        return self.read_all()

    def read_all(self):
        with open(self._file_path, encoding="utf-8") as file:
            data = file.read()
        kurssit = json.loads(data)
        print(kurssit)


logbook_repository = LogbookRepository(EXERCISES_FILE_PATH)
