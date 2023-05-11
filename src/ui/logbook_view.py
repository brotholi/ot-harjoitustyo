from tkinter import ttk, constants
from entities.log_entry import LogEntry
from entities.exercise import Exercise
from services.user_service import user_service
from services.logbook_service import logbook_service


class LogbookView:

    def __init__(self, root, handle_back_to_login, handle_logentry_view):
        self._root = root
        self._handle_back_to_login = handle_back_to_login
        self._handle_logentry_view = handle_logentry_view
        self._current_view = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _error(self):
        print("error")

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_header()
        self._initialize_logs()
        self._initialize_footer()

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

    def _initialize_header(self):
        username = user_service.get_current_user()
        heading_label = ttk.Label(
            master=self._frame, text=f'Kirjautuneena: {username}')
        heading_label.grid(row=0, column=0, sticky=constants.W, padx=5, pady=5)

        logout_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu ulos",
            command=self._logout_handler
        )

        logout_button.grid(row=0, column=1, sticky=constants.E, padx=5, pady=5)

    def _initialize_footer(self):
        add_entry_button = ttk.Button(
            master=self._frame,
            text="Lisää uusi treeni",
            command=self._add_entry_handler
        )

        add_entry_button.grid(sticky=constants.E, padx=5, pady=5)

    def _logout_handler(self):
        self._handle_back_to_login()

    def _add_entry_handler(self):
        self._handle_logentry_view()

    def _initialize_logs(self):
        username = user_service.get_current_user()
        displayable_logs = logbook_service.find_user_logs(username)
 
        for row in displayable_logs:
            log_label = ttk.Label(
                master=self._frame, text=f'{row.logdate} ------ {row.logtitle}')
            log_label.grid(sticky=constants.W, padx=5, pady=5)
            #exercises = logbook_service.find_logentry_exercises(row.id)
            #for exercise in exercises:
            #    exercise_label = ttk.Label(master=self._frame, text=f'{exercise.name} -- {exercise.weight} -- {exercise.reps}')
            #    exercise_label.grid(sticky=constants.E, padx=5, pady=5)
