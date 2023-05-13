import unittest
import datetime
from repositories.user_repository import user_repository
from services.logbook_service import LogbookService, InvalidDateFormatError
from services.user_service import user_service
from entities.user import User
from entities.exercise import Exercise
from entities.log_entry import LogEntry


class FakeTestExercisesRep:
    def __init__(self, lihasloki_exercises=None):
        self.exercises = lihasloki_exercises or []

    def create_new_exercise(self, logentry_id, exercise):
        exercise_row = [logentry_id, exercise]
        self.exercises.append(exercise_row)
        return exercise

    def find_by_logentry_id(self, logentry_id):
        matching_exercises = filter(
            lambda exercise: exercise.logentry_id == logentry_id,
            self.exercises
        )
        list_matching = list(matching_exercises)

        if len(list_matching) > 0:
            return list_matching[0]

        return None

    def find_by_exercise_name_for_user(self, logentry_ids, exercise_name):
        all_matches = []

        for id in logentry_ids:
            exercises = self.find_by_logentry_id(id)

            matching_exercises = filter(
                lambda exercise: exercise.name == exercise_name,
                exercises
            )
            list_matching = list(matching_exercises)
            if len(list_matching) > 0:
                all_matches.append(list_matching)

        if len(all_matches) > 0:
            return all_matches[0]

        return None


class FakeTestLogbookRep:
    def __init__(self, logentries=None):
        self.logentries = logentries or []

    def create_new_entry(self, new_entry):
        self.logentries.append(new_entry)

        return new_entry
    
    def find_newest_log(self, username):
        list_matching = self.find_by_username(username)

        if len(list_matching) > 0:
            last = len(list_matching)-1
            return list_matching[last]

        return None
    
    def find_by_username(self, username):
        matching_entries = filter(
        lambda logentry: logentry.user == username,
        self.logentries
        )

        list_matching = list(matching_entries)

        if len(list_matching) > 0:
            return list_matching

        return None


class TestLogbookService(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.logbook_service = LogbookService(FakeTestLogbookRep(), FakeTestExercisesRep())
        self._logentry_jalkapäivä = LogEntry(
            "Mollamaija", "jalkapäivä", "31.5.2023", 12)
        self._logentry_selkä = LogEntry("unto", "selkä", "4.3.2023", 24)

        self.user_maija = User("Mollamaija", "Sal4san4")
        self._exercise_squat = Exercise("Squat", "80", "8")
        self._exercise_benchpress = Exercise("Bench Press", "50", "7")
    
    def test_find_user_logs(self):
        self.logbook_service.create_new_entry(
            self._logentry_jalkapäivä.user, self._logentry_jalkapäivä.logtitle, self._logentry_jalkapäivä.logdate)
        self.logbook_service.create_new_entry("Mollamaija", "ylävartalo", "18.5.2023")
        self.logbook_service.create_new_entry("Mollamaija", "kokovartalo", "11.5.2023")
        user_logs = self.logbook_service.find_user_logs("Mollamaija")
        self.assertEqual(len(user_logs), 3)

    def test_find_by_logtitle(self):
        self.logbook_service.create_new_entry("ruusa", "ylävartalo", "18.5.2023")
        self.logbook_service.create_new_entry("ruusa", "kokovartalo", "11.5.2023")
        self.logbook_service.create_new_entry("ruusa", "kokovartalo", "11.5.2023")

        self.assertCountEqual()

    def test_create_logentry_id(self):
        first_id = self.logbook_service.create_logentry_id()
        second_id = self.logbook_service.create_logentry_id()

        self.assertNotEqual(first_id, second_id)

    #def test_find_current_log


    def test_create_new_entry(self):
        self.logbook_service.create_new_entry(
            self._logentry_jalkapäivä.user, self._logentry_jalkapäivä.logtitle, self._logentry_jalkapäivä.logdate)

        self.assertEqual(self._logentry_jalkapäivä.logtitle, "jalkapäivä")
        self.assertEqual(self._logentry_jalkapäivä.logdate, "31.5.2023")
        self.assertEqual(self._logentry_jalkapäivä.user, "Mollamaija")

    def get_current_date(self):
        today = datetime.now()
        today_formatted = today.strftime("%d.%m.%Y")
        date = self.logbook_service.get_current_date()
        self.assertAlmostEqual(len(date), 10)
        self.assertAlmostEqual(today_formatted, date)

    def test_create_new_exercise(self):
        self.logbook_service.create_new_exercise(self._logentry_jalkapäivä, self._exercise_squat.name, self._exercise_squat.weight, self._exercise_squat.reps)
        self.assertEqual(self._exercise_squat.name, "Squat")
        self.assertEqual(self._exercise_squat.weight, "80")
        self.assertEqual(self._exercise_squat.reps, "8")

    def test_check_date_format(self):
        date = "123.23.2022"
        try:
            self.logbook_service.check_date_format(date)
        except:
            self.assertRaises(InvalidDateFormatError)

