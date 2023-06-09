from tkinter import Tk
from ui.login_view import LoginView
from ui.create_user import CreateUserView
from ui.logbook_view import LogbookView
from ui.logentry_view import LogentryView
from ui.exercise_view import ExerciseView


class UI:
    """Luokka, joka vastaa sovelluksen käyttöliittymästä."""

    def __init__(self, root):
        """Luokan konstruktori. Luo uuden käyttöliittymä-luokan.
        Args:
            root:
                TKinter-elementti, johon käyttöliittymä alustetaan.
        """
        self._root = root
        self._current_view = None

    def start(self):
        """Käynnistää käyttöliittymän ja näyttää login-näkymän."""
        self._show_login_view()

    def _hide_current_view(self):
        """Piilottaa nykyisen näkymän ja tuhoaa sen."""
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _handle_create_user(self):
        self._show_create_user_view()

    def _handle_back_to_login(self):
        self._show_login_view()

    def _handle_logbook_view(self):
        self._show_logbook_view()

    def _handle_logentry_view(self):
        self._show_logentry_view()

    def _handle_exercise_view(self):
        self._show_exercise_view()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._handle_create_user,
            self._handle_logbook_view
        )

        self._current_view.pack()

    def _show_create_user_view(self):
        self._hide_current_view()
        self._current_view = CreateUserView(
            self._root,
            self._handle_back_to_login
        )
        self._current_view.pack()

    def _show_logbook_view(self):
        self._hide_current_view()
        self._current_view = LogbookView(
            self._root,
            self._handle_back_to_login,
            self._handle_logentry_view

        )
        self._current_view.pack()

    def _show_logentry_view(self):
        self._hide_current_view()
        self._current_view = LogentryView(
            self._root,
            self._handle_logbook_view,
            self._handle_exercise_view

        )
        self._current_view.pack()

    def _show_exercise_view(self):
        self._hide_current_view()
        self._current_view = ExerciseView(
            self._root,
            self._handle_logbook_view

        )
        self._current_view.pack()
