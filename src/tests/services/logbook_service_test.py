import unittest
import uuid
from repositories.user_repository import user_repository
from services.logbook_service import LogbookService
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

    def test_create_new_exercise(self):
        logentry_id = self.logbook_service.create_logentry_id
        self.logbook_service.create_new_exercise(
            logentry_id, self._exercise_squat.name, self._exercise_squat.weight, self._exercise_squat.reps)
        self.assertEqual(self._exercise_squat.name, "Squat")
        self.assertEqual(self._exercise_squat.weight, "80")
        self.assertEqual(self._exercise_squat.reps, "8")

    def test_create_new_entry(self):
        self.logbook_service.create_new_entry(
            self._logentry_jalkapäivä.user, self._logentry_jalkapäivä.logtitle, self._logentry_jalkapäivä.logdate)

        self.assertEqual(self._logentry_jalkapäivä.logtitle, "jalkapäivä")
        self.assertEqual(self._logentry_jalkapäivä.logdate, "31.5.2023")
        self.assertEqual(self._logentry_jalkapäivä.user, "Mollamaija")
