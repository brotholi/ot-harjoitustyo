import unittest
import datetime
from repositories.user_repository import user_repository
from services.logbook_service import LogbookService, InvalidDateFormatError
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
            lambda exercise: exercise[0] == logentry_id,
            self.exercises
        )
        list_matching = list(matching_exercises)

        if len(list_matching) > 0:
            return list_matching[0]

        return None


class FakeTestLogbookRep:
    def __init__(self, logentries=None):
        self.logentries = logentries or []

    def create_new_entry(self, new_entry):
        self.logentries.append(new_entry)

        return new_entry

    def find_newest_log(self, username):
        list_matching = self.find_by_username(username)

        if list_matching:
            last = len(list_matching)-1
            return list_matching[last]
        return []

    def find_by_username(self, username):
        matching_entries = filter(
            lambda logentry: logentry.user == username,
            self.logentries
        )

        list_matching = list(matching_entries)

        if len(list_matching) > 0:
            return list_matching

        return []

    def find_by_logtitle(self, username, logtitle):
        user_entries = self.find_by_username(username)
        matching_entries = filter(
            lambda logentry: logentry.logtitle == logtitle,
            user_entries
        )

        list_matching = list(matching_entries)

        if list_matching:
            return list_matching

        return []


class TestLogbookService(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.logbook_service = LogbookService(
            FakeTestLogbookRep(), FakeTestExercisesRep())
        self._logentry_jalkapäivä = LogEntry(
            "Mollamaija", "jalkapäivä", "31.5.2023", 12)
        self._logentry_selkä = LogEntry("unto", "selkä", "4.3.2023", 24)

        self.user_maija = User("Mollamaija", "Sal4san4")
        self._exercise_squat = Exercise("Squat", "80", "8")
        self._exercise_benchpress = Exercise("Bench Press", "50", "7")

    def test_find_current_log(self):
        self.logbook_service.create_new_entry(
            "ruusa", "ylävartalo", "18.5.2023")
        self.logbook_service.create_new_entry(
            "ruusa", "kokovartalo", "11.5.2023")
        new_log = self.logbook_service.create_new_entry(
            "ruusa", "kokovartalo", "12.5.2023")
        current_log = self.logbook_service.find_current_log("ruusa")

        self.assertEqual(new_log, current_log)

    def test_find_user_logs(self):
        self.logbook_service.create_new_entry(
            self._logentry_jalkapäivä.user, self._logentry_jalkapäivä.logtitle, self._logentry_jalkapäivä.logdate)
        self.logbook_service.create_new_entry(
            "Mollamaija", "ylävartalo", "18.5.2023")
        self.logbook_service.create_new_entry(
            "Mollamaija", "kokovartalo", "11.5.2023")
        user_logs_maija = self.logbook_service.find_user_logs("Mollamaija")
        user_logs_pekka = self.logbook_service.find_user_logs("Pekka")

        self.assertEqual(len(user_logs_maija), 3)
        self.assertEqual(len(user_logs_pekka), 0)

    def test_find_by_logtitle(self):
        self.logbook_service.create_new_entry(
            "ruusa", "ylävartalo", "18.5.2023")
        self.logbook_service.create_new_entry(
            "ruusa", "kokovartalo", "11.5.2023")
        self.logbook_service.create_new_entry(
            "ruusa", "kokovartalo", "12.5.2023")

        similar_logs = self.logbook_service.find_log_by_logtitle(
            "ruusa", "kokovartalo")

        self.assertEqual(len(similar_logs), 2)

    def test_find_logentry_exercises(self):
        new_entry = self.logbook_service.create_new_entry(
            "ruusa", "kokovartalo", "11.5.2023")
        second_entry = self.logbook_service.create_new_entry(
            "ruusa", "jalkapäivä", "11.5.2023")
        self.logbook_service.create_new_exercise(
            new_entry, self._exercise_squat.name, self._exercise_squat.weight, self._exercise_squat.reps)
        self.logbook_service.create_new_exercise(
            new_entry, self._exercise_benchpress.name, self._exercise_benchpress.weight, self._exercise_benchpress.reps)

        new_logentry_exercises = self.logbook_service.find_logentry_exercises(
            new_entry.logid)
        self.assertAlmostEqual(len(new_logentry_exercises), 2)

        second_logentry_exercises = self.logbook_service.find_logentry_exercises(
            second_entry.logid)
        self.assertAlmostEqual(len(second_logentry_exercises), 0)

    def test_create_logentry_id(self):
        first_id = self.logbook_service.create_logentry_id()
        second_id = self.logbook_service.create_logentry_id()

        self.assertNotEqual(first_id, second_id)

    def test_create_new_entry(self):
        self.logbook_service.create_new_entry(
            self._logentry_jalkapäivä.user, self._logentry_jalkapäivä.logtitle, self._logentry_jalkapäivä.logdate)
        self.assertEqual(self._logentry_jalkapäivä.logtitle, "jalkapäivä")
        self.assertEqual(self._logentry_jalkapäivä.logdate, "31.5.2023")
        self.assertEqual(self._logentry_jalkapäivä.user, "Mollamaija")

    def test_create_new_exercise(self):
        self.logbook_service.create_new_exercise(
            self._logentry_jalkapäivä, self._exercise_squat.name, self._exercise_squat.weight, self._exercise_squat.reps)
        self.assertEqual(self._exercise_squat.name, "Squat")
        self.assertEqual(self._exercise_squat.weight, "80")
        self.assertEqual(self._exercise_squat.reps, "8")

    def test_check_date_format(self):
        date_1 = "02032022"
        date_2 = "123.23.2022"
        date_3 = "12.05.2022.12.00"
        date_4 = "12.23.20222"
        date_5 = "pv.02.2023"
        date_6 = "02.02.2023"

        try:
            self.logbook_service.check_date_format(date_1)
        except:
            self.assertRaises(InvalidDateFormatError)

        try:
            self.logbook_service.check_date_format(date_2)
        except:
            self.assertRaises(InvalidDateFormatError)

        try:
            self.logbook_service.check_date_format(date_3)
        except:
            self.assertRaises(InvalidDateFormatError)

        try:
            self.logbook_service.check_date_format(date_4)
        except:
            self.assertRaises(InvalidDateFormatError)

        try:
            self.logbook_service.check_date_format(date_5)
        except:
            self.assertRaises(InvalidDateFormatError)

        correct_date = self.logbook_service.check_date_format(date_6)
        self.assertEqual(correct_date, date_6)
