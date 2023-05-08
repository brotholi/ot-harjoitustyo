from datetime import datetime
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

    def find_user_logs(self, username):
        entries = self._logbook_repository.find_by_username(username)
        if len(entries) > 0:
            return entries
        return []
    
    def find_current_log(self, username):
        current_log = self._logbook_repository.find_newest_log(username)

        return current_log
        

    def order_logs_by_date(self, username):
        all_entries = self.find_user_logs(username)
        dates = []
        for entry in all_entries:
            date1 = entry.logdate
            dates.append(date1)
        sorted_dates = dates.sort(key=lambda date: datetime.strftime(date, "%d.%m.%Y"))
        print(sorted_dates)

        return []
        


    def check_date_format(self, date):
        if "." not in date:
            return False
        
        parts = date.split(".")
        if len(parts) != 3:
            return False
        
        day = parts[0]
        month = parts[1]
        year = parts[2]

        if len(day) != 2 or len(month) != 2:
            return False
        
        if len(year) != 4:
            return False
        
        for part in parts:
            is_number = any(char.isdigit() for char in part)
            if is_number == False:
                return False
            
        return True

    

logbook_service = LogbookService()
