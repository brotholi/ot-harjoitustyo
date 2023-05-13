from tkinter import ttk, constants, StringVar
from entities.log_entry import LogEntry
from entities.exercise import Exercise
from services.user_service import user_service
from services.logbook_service import logbook_service


class SearchListView:
    def __init__(self, root, search_results):
        self._root = root
        self._search_results = search_results
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_exercise()

    def _initialize_exercise(self):
        item_frame = ttk.Frame(master=self._frame)

        label = ttk.Label(master=item_frame, text='')
        label.grid(column=0, padx=5, pady=5, sticky=constants.W)

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)


class LogbookView:
    """Luokan konstruktori. Luo uuden kirjautuneen käyttäjän alkunäkymän.
        Args:
            root:
                TKinter-elementti, johon näkymä alustetaan.
            handle_back_to_login:
                Kutsuttava-arvo, jota kutsutaan kun siirrytään takaisin kirjautumisnäkymään.
            handle_logentry_view:
                Kutsuttava-arvo, jota kutsutaan kun siirrytään uuden treenin kirjausnäkymään.
    """
    def __init__(self, root, handle_back_to_login, handle_logentry_view):
        self._root = root
        self._handle_back_to_login = handle_back_to_login
        self._handle_logentry_view = handle_logentry_view
        self._search_list_view = None
        self._search_list_frame = None
        self._current_view = None

        self._initialize()

    def pack(self):
        """"Näyttää nykyisen näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Piilottaa error-viestin."""
        self._frame.destroy()

    def _show_error_message(self, message):
        """"Näyttää error-viestin käyttäjälle.
        Args:
            message: Merkkijonona error-viesti"""

        self._error_var.set(message)
        self._error_label.grid()

    def _hide_error(self):
        """Piilottaa error-viestin.
        """
        self._error_label.grid_remove()

    def _initialize_search_list(self):
        "Alustaa hakutulosten listauksesta vastaavan näkymän"
        keyword = self._search_entry.get()

        if self._search_list_view:
            self._exercise_list_view.destroy()
        search_results = logbook_service.find_log_by_logtitle(keyword)

        self._exercise_list_view = SearchListView(
            self._search_list_frame,
            search_results
        )

        # self._search_list_view.pack()

    def _initialize(self):
        """Alustaa näkymän."""
        self._frame = ttk.Frame(master=self._root)
        self._search_list_frame = ttk.Frame(master=self._frame)
        self._initialize_header()
        self._initialize_logs()
        self._initialize_footer()
        self._initialize_search_list()

        self._search_list_frame.grid(
            row=18,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

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

        log_header = ttk.Label(
            master=self._frame, text="Aiemmat kirjaukset", font='Helvetica 14 bold')
        log_header.grid(row=1, column=0, sticky=constants.W, padx=5, pady=5)

    def _initialize_footer(self):
        search_label = ttk.Label(
            master=self._frame, text=f'Hae treenejä', font='Arial 12 bold')
        search_label.grid(row=15, column=0, sticky=constants.W, padx=5, pady=5)

        self._search_entry = ttk.Entry(master=self._frame, width=20)
        self._search_entry.grid(
            row=16, column=0, sticky=constants.W, padx=5, pady=5)

        search_button = ttk.Button(
            master=self._frame,
            text="»",
            width=6,
            command=self._search_entry_handler
        )

        search_button.grid(
            row=16, column=0, sticky=constants.E, padx=5, pady=5)

        add_entry_button = ttk.Button(
            master=self._frame,
            text="Lisää uusi treeni",
            command=self._add_entry_handler
        )

        add_entry_button.grid(
            row=17, column=1, sticky=constants.E, padx=5, pady=5)

        self._error_var = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_var,
            foreground="black"
        )

        self._error_label.grid(row=17, column=0, padx=5,
                               pady=5, sticky=constants.W)

    def _logout_handler(self):
        self._handle_back_to_login()

    def _add_entry_handler(self):
        self._handle_logentry_view()

# oma näkymä???
# /////////
    def _search_entry_handler(self):
        """Kirjausten hakutoiminnon tapahtumakäsittelijä"""
        keyword = self._search_entry.get()
        search_results = logbook_service.find_log_by_logtitle(keyword)
        if len(search_results) == 0:
            self._show_error_message("Ei hakutuloksia")

        for log in search_results:
            log_label = ttk.Label(master=self._frame,
                                  text=f'{log.logtitle}', font='Arial 10 bold')
            log_label.grid(sticky=constants.W, padx=5, pady=5)
            date_label = ttk.Label(
                master=self._frame, text=f'Pvm:  {log.logdate}')
            date_label.grid(sticky=constants.W, padx=5, pady=5)
            log_exercises = logbook_service.find_logentry_exercises(log.id)
            print(log_exercises)
            for exercise in log_exercises:
                exercise_label = ttk.Label(
                    master=self._frame, text=f'{exercise.name}  {exercise.weight}kg  x  {exercise.reps}')
                exercise_label.grid(sticky=constants.W, padx=5, pady=5)

            separator = ttk.Separator(master=self._frame, orient='horizontal')
            separator.grid(sticky=constants.EW, columnspan=5)

    def _initialize_logs(self):
        """Alustaa käyttäjälle näytettävät viisi aiempaa kirjausta."""
        username = user_service.get_current_user()
        all_logs = logbook_service.find_user_logs(username)
        if len(all_logs) > 5:
            displayable_logs = all_logs[-5:]
        else:
            displayable_logs = all_logs

        for row in displayable_logs:
            log_label = ttk.Label(
                master=self._frame, text=f'Pvm:  {row.logdate}  Treeni:  {row.logtitle}')
            log_label.grid(sticky=constants.W, padx=5, pady=5)
