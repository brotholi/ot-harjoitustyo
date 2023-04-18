from tkinter import Tk, ttk, constants


class LoginView:

    def __init__(self, root, handle_create_user):
        self._root = root
        self._handle_create_user = handle_create_user
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _error(self):
        print("error")

    def _handle_login(self):
        # yritä loginia käyttäjäservicellä
        username_entry_value = self._username_entry.get()
        password_entry_value = self._password_entry.get()
        if len(username_entry_value) > 0:
            print(f"Käyttäjätunnuksesi oli: {username_entry_value}")

    # def _handle_create_user(self):
        # print("Luodaan uusi käyttäjä")

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

        self._frame.grid_columnconfigure(1, weight=1)
