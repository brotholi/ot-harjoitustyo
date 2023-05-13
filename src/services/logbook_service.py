import uuid
from datetime import datetime
from entities.log_entry import LogEntry
from entities.exercise import Exercise
from repositories.logbook_repository import (
    logbook_repository as default_logbook_repository
)
from repositories.exercises_repository import (
    exercise_repository as default_exercise_repository
)
from services.user_service import user_service

class InvalidDateFormatError(Exception):
    pass


class LogbookService:
    """Treenikirjauksiin liittyvästä sovelluslogiikasta vastaava luokka."""

    def __init__(self, logbook_repository=default_logbook_repository,
        exercise_repository=default_exercise_repository):
        """Luokan konstruktori. Luo uuden treenikirjausten sovelluslogiikasta vastaavan palvelun.
        Args:
            logbook_repository:
                Vapaaehtoinen, oletusarvoltaan LogbookRepositoryn olio.
                Oliolla on LogbookRepository-luokkaa vastaavat metodit.
            exercise_repository:
                Vapaaehtoinen, oletusarvoltaan ExerciseRepositoryn olio.
                Oliolla on ExerciseRepository-luokkaa vastaavat metodit.
        """
        self._entry = None
        self._logbook_repository = logbook_repository
        self._exercises_repository = exercise_repository

    def create_new_entry(self, username, logtitle, time):
        """Luo uuden käyttäjän.
        Args:
            username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta.
            logtitle: Merkkijonoarvo, joka kuvaa treenin otsikkoa.
            date: päi
        Returns:
            Luotu käyttäjä LogEntry-oliona.
        """
        logentry_id = self.create_logentry_id()
        new_entry = LogEntry(username, logtitle, time, logentry_id)
        self._logbook_repository.create_new_entry(new_entry)
        return new_entry

    def find_user_logs(self, username):
        """Paluttaa yhden käyttäjän tekemät treenikirjaukset.
        Args:
            username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta.
        Returns:
            Luodut kirjaukset LogEntry-olioiden listana.
        """
        entries = self._logbook_repository.find_by_username(username)
        if len(entries) > 0:
            return entries
        return []

    def find_current_log(self, username):
        """Paluttaa treenikirjauksen, jota käyttäjä on tällä hetkellä kirjaamassa.
        Args:
            username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta.
        Returns:
            Luotu kirjaus LogEntry-oliona.
        """
        current_log = self._logbook_repository.find_newest_log(username)
        return current_log

    def find_log_by_logtitle(self, logtitle):
        """Paluttaa yhden käyttäjän treenikirjaukset, joilla on hakutekijää vastaava nimi.
        Returns:
            Samannimiset kirjaukset LogEntry-olioden listana.
        """
        username = user_service.get_current_user()
        logs_by_name = self._logbook_repository.find_by_logtitle(
            username, logtitle)
        return logs_by_name

    def create_new_exercise(self, logentry_id, exercise_name, weigth, reps):
        """Luo uuden käyttäjän.
        Args:
            username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta.
            logentry_id: Merkkijonoarvo, joka kuvaa yksilöivää treenikirjauksen tunnusta.
            exercise_name: Merkkijonoarvo, joka kuvaa liikeen nimeä.
            weigth: Merkkijonoarvo, joka kuvaa liikeen lisäpainoa.
            reps: Merkkijonoarvo, joka kuvaa liikeen toistomäärää.
        Returns:
            Luotu liike Exercise-oliona.
        """
        exercise = Exercise(exercise_name, weigth, reps)
        self._exercises_repository.create_new_exercise(logentry_id, exercise)
        return exercise

    def find_logentry_exercises(self, logentry_id):
        """Palauttaa yhden treenikirjauksen liikkeet.
        Args:
            logentry_id: Merkkijonoarvo, joka kuvaa yksilöivää treenikirjauksen tunnusta.
        Returns:
            Treenikirjauksen liikkeet Exercise-olioiden listana.
        """
        entries = self._exercises_repository.find_by_logentry_id(logentry_id)
        if len(entries) > 0:
            return entries
        return []

    def find_users_exercises_by_exercise_name(self, username, exercise_name):
        """Palauttaa yhden käyttäjän kirjaamat liikkeet.
        Args:
            username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta.
            exercise_name: Merkkijonoarvo, joka kuvaa liikkeen nimeä.
        Returns:
            Käyttäjän samannimiset liikkeet Exercise-olioiden listana.
        """
        all_entries = self._logbook_repository.find_by_username(username)
        user_entries = []
        for entry in all_entries:
            logentry_id = entry.id
            user_entries.append(logentry_id)
        user_exercises = self._exercises_repository.find_by_exercise_name_for_user(
            user_entries, exercise_name)
        return user_exercises

    def create_logentry_id(self):
        """Luo uuden treenikirjauksen id-tunnuksen.
        Returns:
            Yksilöllisen uuid-tunnuksen merkkijonona.
        """
        uusi = uuid.uuid4()
        logentry_id = str(uusi)
        return logentry_id
    
    def get_current_date(self):
        """Palauttaa kuluvan päivän.
        Returns:
            Päivämäärän merkkijonona.
        """
        current_date = datetime.now()
        date_value = current_date.strftime("%d.%m.%Y")
        return date_value

    def check_date_format(self, date):
        """Tarkastaa käyttäjän syöttämän päivämäärän muodon.
        Raises:
            InvalidCredentialsError:
                Virhe, kun käyttäjän syöttämä päivämäärä ei vastaa muotoa pp.kk.vvvv.
        Returns:
            Oikeassa muodossa olevan päivämäärän.
        """
        
        if "." not in date:
            raise InvalidDateFormatError()

        parts = date.split(".")
        if len(parts) != 3:
            raise InvalidDateFormatError()

        day = parts[0]
        month = parts[1]
        year = parts[2]

        if len(day) != 2 or len(month) != 2:
            raise InvalidDateFormatError()

        if len(year) != 4:
            raise InvalidDateFormatError()

        for part in parts:
            is_number = part.isdigit()
            if is_number is False:
                raise InvalidDateFormatError()

        return date


logbook_service = LogbookService()
