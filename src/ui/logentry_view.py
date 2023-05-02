from tkinter import ttk, constants
from services.user_service import user_service
from services.logbook_service import logbook_service


class LogentryView:

    def __init__(self, root, handle_logbook_view):
        self._root = root
        self._handle_logbook_view = handle_logbook_view
        self._current_view = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _error(self):
        print("error")

    def _return_handler(self):
        self._handle_logbook_view()

    def _create_entry_handler(self):
        username = user_service.get_current_user()
        title_entry_value = self._title_entry.get()
        date_entry_value = self._date_entry.get()
        logbook_service.create_new_entry(
            username, title_entry_value, date_entry_value)

        self._handle_logbook_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text=f'Treenin kirjaus')

        title_label = ttk.Label(
            master=self._frame, text="Nimi:")
        self._title_entry = ttk.Entry(master=self._frame)

        date_label = ttk.Label(
            master=self._frame, text="Päivämäärä:")
        self._date_entry = ttk.Entry(master=self._frame)

        exercises_label = ttk.Label(
            master=self._frame, text=f'liike1....')

        save_entry_button = ttk.Button(
            master=self._frame,
            text="Tallenna",
            command=self._create_entry_handler
        )

        return_button = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._return_handler
        )

        label.grid(row=0, column=0, sticky=constants.W, padx=5, pady=5)

        title_label.grid(row=3, column=0, padx=5, pady=5)
        self._title_entry.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        date_label.grid(row=4, column=0, padx=5, pady=5)
        self._date_entry.grid(row=4, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        exercises_label.grid(
            row=5, column=0, sticky=constants.W, padx=5, pady=5)

        save_entry_button.grid(row=6, column=1, padx=5,
                               pady=5, sticky=constants.E)

        return_button.grid(row=6, column=0, padx=5,
                           pady=5, sticky=constants.W)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
