from tkinter import ttk, constants, StringVar
from datetime import datetime
from services.user_service import user_service
from services.logbook_service import logbook_service


class LogentryView:

    def __init__(self, root, handle_logbook_view, handle_exercise_view):
        self._root = root
        self._handle_logbook_view = handle_logbook_view
        self._handle_exercise_view = handle_exercise_view
        self._current_view = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _show_error_message(self, message):
        """"Näyttää error-viestin käyttäjälle.
        Args:
            message: Merkkijonona error-viesti"""

        self._error_var.set(message)
        self._error_label.grid()

    def _show_date_entry(self):
        self._date_entry.grid()

    def _hide_error(self):
        """Piilottaa error-viestin.
        """
        self._error_label.grid_remove()

    def _hide_change_date_button(self):
        self._change_date_button.grid_forget()


    def _hide_date_entry(self):
        """Piilottaa päivämäärän syöttökentän.
        """
        self._date_entry.grid_remove()

    def _hide_current_date(self):
        self.current_date_label.grid_forget()

    def _return_handler(self):
        self._handle_logbook_view()

    def _create_entry_handler(self):
        username = user_service.get_current_user()
        title_entry_value = self._title_entry.get()
        date_entry_value = self._date_entry.get()

        if len(title_entry_value) <= 0:
            self._show_error_message("Syötä otsikko")
            return
        
        if len(date_entry_value) == 0:
            date = datetime.now()
            date_entry_value = date.strftime("%d.%m.%Y")

        date_format = logbook_service.check_date_format(date_entry_value)

        if date_format == False:
            self._show_error_message("Syötä päivämäärä muodossa pp.kk.vvvv")
            return

        logbook_service.create_new_entry(
            username, title_entry_value, date_entry_value)

        self._handle_exercise_view()

    def _change_date_handler(self):
        self._hide_change_date_button()
        self._hide_current_date()
        self._show_date_entry()


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self.initialize_header()

        title_entry_label = ttk.Label(master=self._frame, text="Otsikko:")
        self._title_entry = ttk.Entry(master=self._frame)

        date_label = ttk.Label(master=self._frame, text="Päivämäärä:")
        current_date = datetime.now()

        self.current_date_label = ttk.Label(master=self._frame, text=f'{current_date.day}.{current_date.month}.{current_date.year}')

        self._change_date_button = ttk.Button(
            master=self._frame,
            text="Muuta päivämäärää",
            command=self._change_date_handler
        )

        self._date_entry = ttk.Entry(master=self._frame)

        title_entry_label.grid(row=3, column=0, sticky=constants.W, padx=5, pady=5)
        self._title_entry.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        date_label.grid(row=4, column=0, sticky=constants.W, padx=5, pady=5)
        self.current_date_label.grid(row=4, column=1, sticky=constants.E, padx=5, pady=5)

        self._change_date_button.grid(row=5, column=1, padx=5,
            pady=5, sticky=constants.E)

        self._date_entry.grid(row=4, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        
        self.initialize_footer()
        self._hide_error()
        self._hide_date_entry()
        self._root.grid_columnconfigure(1, weight=1)


    def initialize_header(self):
        label = ttk.Label(master=self._frame, text=f'Uusi treeni')

        return_button = ttk.Button(
            master=self._frame,
            text="Peruuta",
            command=self._return_handler
        )

        label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)

        return_button.grid(row=0, column=1, padx=5,
            pady=5, sticky=constants.E)
        
    def initialize_footer(self):
        save_entry_button = ttk.Button(
            master=self._frame,
            text="Ok",
            command=self._create_entry_handler
        )

        ok_label = ttk.Label(
            master=self._frame, text="Siirry syöttämään liikkeet")
        
        self._error_var = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_var,
            foreground="red"
        )

        save_entry_button.grid(row=6, column=0, padx=5,
            pady=5, sticky=constants.W)
        
        ok_label.grid(row=7, column=0, padx=5, pady=5, sticky=constants.W)

        self._error_label.grid(row=8, column=0, padx=5,
            pady=5, sticky=constants.W)


