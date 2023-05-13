import unittest
from repositories.exercises_repository import exercise_repository
from entities.exercise import Exercise


class TestExerciseRepository(unittest.TestCase):
    def setUp(self):
        exercise_repository.delete_all()
        self._exercise_squat = Exercise("Squat", "80", "8")
        self._exercise_benchpress = Exercise("Bench Press", "50", "7")

    def test_create_new_exercise(self):
        exercise_repository.create_new_exercise("23", self._exercise_squat)
        lihasloki_exercises = exercise_repository.find_all()
        self.assertEqual(len(lihasloki_exercises), 1)

    def test_find_all(self):
        exercise_repository.create_new_exercise("44", self._exercise_squat)
        exercise_repository.create_new_exercise(
            "50", self._exercise_benchpress)
        lihasloki_exercises = exercise_repository.find_all()
        self.assertEqual(len(lihasloki_exercises), 2)

    def test_find_by_logentry_id(self):
        exercise_repository.create_new_exercise("15", self._exercise_squat)
        exercise_repository.create_new_exercise(
            "15", self._exercise_benchpress)
        exercise_repository.create_new_exercise(
            "84", self._exercise_benchpress)

        logentry_exercises = exercise_repository.find_by_logentry_id("15")
        self.assertEqual(len(logentry_exercises), 2)

    def test_find_by_empty_logentry_id(self):
        logentry_exercises = exercise_repository.find_by_logentry_id("98989")
        self.assertEqual(len(logentry_exercises), 0)

