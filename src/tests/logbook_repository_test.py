import unittest
from repositories.logbook_repository import logbook_repository
from entities.log_entry import LogEntry


class TestUserRep(unittest.TestCase):
    def setUp(self):
        logbook_repository.delete_all()
        self._logentry_jalkapäivä = LogEntry(
            "maija", "jalkapäivä", "31.4.2023")
        self._logentry_selkä = LogEntry("unto", "selkä", "4.3.2023")

    def test_create_new_user(self):
        logbook_repository.create_new_entry(self._logentry_jalkapäivä)
        logbook_repository.create_new_entry(self._logentry_selkä)
        lihasloki_users = logbook_repository.find_all()
        self.assertEqual(len(lihasloki_users), 2)
