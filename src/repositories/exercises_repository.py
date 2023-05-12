import sqlite3
import sys
from entities.exercise import Exercise
from database_connection import create_database_connection


class DatabaseDoesNotExistError(Exception):
    pass


class ExerciseRepository:
    """Luokka, joka vastaa yksittäisiin liikkeisiin liittyvistä tietokantaoperaatioista.
    """

    def __init__(self, connection):
        """Luokan konstruktori.
        Args:
            connection: Tietokantayhteyteen liittyvä Connection-olio
        """
        self._connection = connection

    def find_all(self):
        """Palauttaa kaikki tietokannassa olevat liikkeet.
        Returns:
            Palauttaa listan User-olioita.
        """
        cursor = self._connection.cursor()
        try:
            cursor.execute("select * from lihasloki_exercises")
        except sqlite3.OperationalError:
            self._handle_nonexistent_database_error()
        rows = cursor.fetchall()
        if len(rows) > 0:
            return [Exercise(row["name"], row["weight"], row["reps"]) for row in rows]
        return []

    def delete_all(self):
        """Poistaa kaikki liikkeet.
        """
        cursor = self._connection.cursor()
        cursor.execute("delete from lihasloki_exercises")
        self._connection.commit()

    def create_new_exercise(self, logentry_id, exercise):
        """Syöttää käyttäjän tiedot tauluun.

        Args:
            todo: Tallennettava liike Exercise-oliona ja 
            logentry_id, joka liittää liikkeen tiettyyn kirjaukseen.

        Returns:
            Tallennettu käyttäjä Exercise-oliona.
        """
        all = self.find_all()
        id = len(all)

        cursor = self._connection.cursor()

        try:
            cursor.execute("""insert into lihasloki_exercises
             (exercise_id, logentry_id, name, weight, reps) values (?, ?, ?, ?, ?)""",
                           (id, logentry_id, exercise.name,
                            exercise.weight, exercise.reps)
                           )
        except sqlite3.OperationalError:
            self._handle_nonexistent_database_error()
        self._connection.commit()
        return exercise

    def find_by_logentry_id(self, logentry_id):
        """Hakee yhden treenin tiedot logentry_id:n perusteella.
        Args:
            username: Käyttäjätunnus, jonka omaava käyttäjä palautetaan.
        Returns:
            Palauttaa Exerices-oliot, jos logentry_id on tietokannassa.
            Muutoin palauttaa None.
        """

        cursor = self._connection.cursor()
        try:
            cursor.execute("select * from lihasloki_exercises where logentry_id = ?",
                           (logentry_id,))
        except sqlite3.OperationalError:
            self._handle_nonexistent_database_error()
        rows = cursor.fetchall()

        if len(rows) == 0:
            return []

        exercises = []
        for row in rows:
            exercise = Exercise(row["name"], row["weight"], row["reps"])
            exercises.append(exercise)

        return exercises

    def find_by_exercise_name_for_user(self, logentry_ids, exercise_name):
        """Hakee yhden käyttäjän kaikki samannimiset liikkeet.
            Saa parametreina kaikki käyttäjän logentry_id:t listana ja liikkeen nimen.
            Palogentry_idlauttaa kaikki liikkeet listana
        """
        exercises = []
        for entry_id in logentry_ids:
            cursor = self._connection.cursor()
            cursor.execute("select * from lihasloki_exercises where logentry_id = ? and name = ?",
                           (entry_id, exercise_name,))
            row = cursor.fetchone()
            exercise = Exercise(row["name"], row["weight"], row["reps"])
            exercises.append(exercise)

        return exercises

    def _handle_nonexistent_database_error(self):
        """Jos tietokantaa ei ole alustettu, lopettaa sovelluksen.
        """
        print("Tietokantaa ei ole olemassa,tee ensin alustukset komennolla poetry run invoke build")
        sys.exit()


exercise_repository = ExerciseRepository(create_database_connection())
