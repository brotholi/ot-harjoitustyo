from pathlib import Path
from entities.log_entry import LogEntry
from config import LOGENTRIES_FILE_PATH


class LogbookRepository:

    def __init__(self, file_path):
        self._file_path = file_path

    def find_all(self):
        # etsii kaikki entryt
        return self.read_all()

    def read_all(self):
        # palauttaa kaikki csv-tiedoston entryt logentry-olioiden listana
        entries = []
        self.make_sure_file_exists()

        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                username = parts[0]
                log_title = parts[1]
                date = parts[2]
                id = parts[3]

                entries.append(LogEntry(username, log_title, date, id))

        return entries

    def find_by_username(self, username):
        # palauttaa kaikki yhden käyttäjän entryt logentry-olioiden listana
        all_entires = self.find_all()
        entries_by_user = filter(
            lambda entry: entry.user == username, all_entires)
        user_entries = list(entries_by_user)

        return user_entries

    def find_newest_log(self, username):
        # etsii uusimman entryn
        user_logs = self.find_by_username(username)
        i = len(user_logs) - 1
        newest_log = user_logs[i]
        return newest_log
    
    def find_by_logtitle(self, username, logtitle):
        user_logs = self.find_by_username(username)
        entries_by_title = filter(
            lambda entry: entry.logtitle == logtitle, user_logs)
        logentries = list(entries_by_title)
        if len(logentries) > 0:
            return logentries
        else:
            return []

    def make_sure_file_exists(self):
        # tarkistaa, että tiedosto on olemassa
        Path(self._file_path).touch()

    def create_new_entry(self, entry):
        # luo uuden entryn
        entries = self.find_all()

        entries.append(entry)
        self.write(entries)

    def write(self, entries):
        # kirjoittaa entryn tietokantaan
        self.make_sure_file_exists()
        with open(self._file_path,  "w", encoding="utf-8") as file:
            for entry in entries:
                row = f"{entry.user};{entry.logtitle};{entry.logdate};{entry.id}"

                file.write(row+"\n")

    def delete_all(self):
        # poistaa kaikki entryt tiedostosta
        self.write([])


logbook_repository = LogbookRepository(LOGENTRIES_FILE_PATH)
