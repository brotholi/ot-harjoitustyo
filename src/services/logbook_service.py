from datetime import datetime
import uuid
from entities.log_entry import LogEntry
from entities.exercise import Exercise
from repositories.logbook_repository import (
    logbook_repository as default_logbook_repository
)
from repositories.exercises_repository import (
    exercise_repository as default_exercise_repository
)


class LogbookService:

    def __init__(self, logbook_repository=default_logbook_repository, exercise_repository=default_exercise_repository):
        self._entry = None
        self._logbook_repository = logbook_repository
        self._exercises_repository = exercise_repository

    def create_new_entry(self, username, title, time):
        logentry_id = self.create_logentry_id()
        new_entry = LogEntry(username, title, time, logentry_id)
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
    
    def create_new_exercise(self, logentry_id, exercise_name, weigth, reps):
        exercise = Exercise(exercise_name, weigth, reps)
        self._exercises_repository.create_new_exercise(logentry_id, exercise)
        return exercise
    
    def find_logentry_exercises(self, logentry_id):
        entries = self._exercises_repository.find_by_logentry_id(logentry_id)
        if len(entries) > 0:
            return entries
        return []
    
    def find_users_exercises_by_exercise_name(self, username, exercise_name):
        all_entries = self._logbook_repository.find_by_username(username)
        user_entries = []
        for entry in all_entries:
            logentry_id = entry.id
            user_entries.append(logentry_id)
        user_exercises = self._exercises_repository.find_by_exercise_name_for_user(user_entries, exercise_name)
        return user_exercises
    
    def create_logentry_id(self):
        logentry_id = uuid.uuid4()
        return logentry_id
        #id_check = True
        #while (id_check == True):
        #    id = randint
        #    id_check = self.check_if_id_exists(id)
        #return id
    
    #def check_if_id_exists(self, logentry_id):
    #    #haetaan logentry_id:tä tietokannasta!
    #    existing_id = self._exercises_repository.find_by_logentry_id(logentry_id)
    #    if existing_id:
    #        return True
    #    
    #    return False


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
    

    #def order_logs_by_date(self, username):
    #    all_entries = self.find_user_logs(username)
    #    dates = []
    #    for entry in all_entries:
    #        date1 = entry.logdate
    #        dates.append(date1)
    #    sorted_dates = dates.sort(key=lambda date: datetime.strftime(date, "%d.%m.%Y"))
    #    print(sorted_dates)
    #    return []

    

logbook_service = LogbookService()
