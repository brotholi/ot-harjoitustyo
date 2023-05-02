from entities.log_entry import LogEntry
from repositories.logbook_repository import (
    logbook_repository as default_logbook_repository
)


class LogbookService:

    def __init__(self, logbook_repository=default_logbook_repository):
        self._entry = None
        self._logbook_repository = logbook_repository

    def create_new_entry(self, username, title, time):
        new_entry = LogEntry(username, title, time)
        self._logbook_repository.create_new_entry(new_entry)
        return new_entry


logbook_service = LogbookService()
