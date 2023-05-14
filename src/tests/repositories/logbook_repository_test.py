import unittest
from repositories.logbook_repository import logbook_repository
from entities.log_entry import LogEntry


class TestUserRep(unittest.TestCase):
    def setUp(self):
        logbook_repository.delete_all()
        self._logentry_jalkapäivä = LogEntry(
            "maija", "jalkapäivä", "31.4.2023", 12)
        self._logentry_jalkapäivä_2 = LogEntry(
            "maija", "jalkapäivä", "02.05.2023", 13)
        self._logentry_selkä = LogEntry("unto", "selkä", "4.3.2023", 24)

    def test_create_new_entry(self):
        logbook_repository.create_new_entry(self._logentry_jalkapäivä)
        logbook_repository.create_new_entry(self._logentry_selkä)
        entries = logbook_repository.find_all()
        self.assertEqual(len(entries), 2)

    def test_find_by_logtitle(self):
        logbook_repository.create_new_entry(self._logentry_jalkapäivä)
        logbook_repository.create_new_entry(self._logentry_jalkapäivä_2)
        logbook_repository.create_new_entry(self._logentry_selkä)

        legdays_maija = logbook_repository.find_by_logtitle(
            self._logentry_jalkapäivä.user, self._logentry_jalkapäivä.logtitle)
        self.assertEqual(len(legdays_maija), 2)

        legdays_pekka = logbook_repository.find_by_logtitle(
            "Pekka", self._logentry_jalkapäivä.logtitle)
        self.assertEqual(len(legdays_pekka), 0)
