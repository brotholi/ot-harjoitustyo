from tkinter import ttk, constants, StringVar
from services.user_service import user_service, InvalidCredentialsError


class LoginView:

    def __init__(self, root, handle_create_user, handle_logbook_view):
        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_logbook_view = handle_logbook_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _show_error_message(self, message):
        self._error_var.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _handle_login(self):
        # yritä loginia käyttäjäservicellä
        username_entry_value = self._username_entry.get()
        password_entry_value = self._password_entry.get()
        if len(username_entry_value) > 0:
            try:
                user_service.login(username_entry_value, password_entry_value)
                self._handle_logbook_view()
            except InvalidCredentialsError:
                self._show_error_message("Väärä käyttäjätunnus tai salasana")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, text="Kirjautuminen")

        username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Salasana")
        self._password_entry = ttk.Entry(master=self._frame)

        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu",
            command=self._handle_login
        )

        create_user_button = ttk.Button(
            master=self._frame,
            text="Luo käyttäjä",
            command=self._handle_create_user
        )

        self._error_var = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_var,
            foreground="red"
        )

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=10, pady=10)
        username_label.grid(padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W, ), padx=5, pady=5)
        password_label.grid(padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        login_button.grid(row=3, column=0, columnspan=2)
        create_user_button.grid(row=4, column=0, columnspan=2)

        self._error_label.grid(row=5, column=1, padx=5,
                               pady=5, sticky=constants.E)

        self._frame.grid_columnconfigure(1, weight=1)

        self._hide_error()
