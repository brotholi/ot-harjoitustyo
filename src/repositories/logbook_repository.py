from pathlib import Path
from entities.log_entry import LogEntry
from config import EXERCISES_FILE_PATH


class LogbookRepository:

    def __init__(self, file_path):
        self._file_path = file_path

    def find_all(self):
        return self.read_all()

    def read_all(self):
        entries = []
        self.make_sure_file_exists()

        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                username = parts[0]
                log_title = parts[1]
                date = parts[2]

                entries.append(LogEntry(username, log_title, date))

        return entries

    def make_sure_file_exists(self):
        Path(self._file_path).touch()

    def create_new_entry(self, entry):
        entries = self.find_all()

        entries.append(entry)
        self.write(entries)

    def write(self, entries):
        self.make_sure_file_exists()
        with open(self._file_path,  "w", encoding="utf-8") as file:
            for entry in entries:
                row = f"{entry.user};{entry.logtitle};{entry.logdate}"
                file.write(row+"\n")

    def delete_all(self):
        self.write([])


logbook_repository = LogbookRepository(EXERCISES_FILE_PATH)
