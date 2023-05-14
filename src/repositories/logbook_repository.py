from pathlib import Path
from entities.log_entry import LogEntry
from config import LOGENTRIES_FILE_PATH


class LogbookRepository:
    """Luokka, joka vastaa sovelluksen treenikirjauksiin liittyvästä csv-tiedoston käsittelystä.
    """

    def __init__(self, file_path):
        """Luokan konstruktori.
        Args:
            file_path: Tallennettavan csv-tiedoston polku.
        """
        self._file_path = file_path

    def find_all(self):
        """Hakee kaikki csv-tiedostossa olevat treenikirjaukset."""
        return self.read_all()

    def read_all(self):
        """Palauttaa kaikki csv-tiedostossa olevat treenikirjaukset.
        Returns:
            Palauttaa listan LogEntry-olioita.
        """
        entries = []
        self.make_sure_file_exists()

        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                username = parts[0]
                log_title = parts[1]
                date = parts[2]
                logentry_id = parts[3]

                entries.append(
                    LogEntry(username, log_title, date, logentry_id))

        return entries

    def find_by_username(self, username):
        """Hakee yhden käyttäjän treenikirjaukset käyttäjätunnuksen perusteella.
        Args:
            username: Merkkijonarvo, joka vastaa käyttäjän käyttäjän käyttäjätunnusta.
        Returns:
            Lista LogEntry-olioita.
        """
        all_entires = self.find_all()
        entries_by_user = filter(
            lambda entry: entry.user == username, all_entires)
        user_entries = list(entries_by_user)

        return user_entries

    def find_newest_log(self, username):
        """Hakee yhden käyttäjän uusimman treenikirjauksen käyttäjätunnuksen perusteella.
        Args:
            username: Merkkijonarvo, joka vastaa käyttäjän käyttäjän käyttäjätunnusta.
        Returns:
           LogEntry-olio
        """
        user_logs = self.find_by_username(username)
        i = len(user_logs) - 1
        newest_log = user_logs[i]
        return newest_log

    def find_by_logtitle(self, username, logtitle):
        """Hakee yhden käyttäjän treenikirjaukset kirjauksen nimen perusteella.
        Args:
            username: Merkkijonarvo, joka vastaa käyttäjän käyttäjän käyttäjätunnusta.
            logtitle: Merkkijonoarvo, joka vastaa treenin nimeä.
        Returns:
           LogEntry-olio.
        """

        user_logs = self.find_by_username(username)
        entries_by_title = filter(
            lambda entry: entry.logtitle == logtitle, user_logs)
        logentries = list(entries_by_title)
        if len(logentries) > 0:
            return logentries
        return []

    def make_sure_file_exists(self):
        """Tarkistaa, että tiedosto on olemassa.
        """
        Path(self._file_path).touch()

    def create_new_entry(self, entry):
        """Syöttää treenikirjauksen tiedot csv-tiedostoon.
        Args:
            entry: Tallennettava kirjaus LogEntry-oliona.
        """
        entries = self.find_all()

        entries.append(entry)
        self.write(entries)

    def write(self, entries):
        """Kirjoittaa treenikirjauksen csv-tiedostoon.
        Args:
            entries: Tallennettavat kirjaukset LogEntry-olioiden listana.
        """
        self.make_sure_file_exists()
        with open(self._file_path,  "w", encoding="utf-8") as file:
            for entry in entries:
                row = f"{entry.user};{entry.logtitle};{entry.logdate};{entry.logid}"

                file.write(row+"\n")

    def delete_all(self):
        """poistaa kaikki entryt tiedostosta."""
        self.write([])


logbook_repository = LogbookRepository(LOGENTRIES_FILE_PATH)
