from tkinter import ttk, constants, StringVar
from services.user_service import user_service, UserExistsError


class CreateUserView:
    """uuden käyttäjän rekisteröitymisestä vastaava näkymä."""

    def __init__(self, root, _handle_back_to_login):
        """Luokan konstruktori. Luo uuden rekisteröitymisnäkymän.
        Args:
            root:
                TKinter-elementti, johon näkymä alustetaan.
            handle_back_to_login:
                Kutsuttava-arvo, jota kutsutaan kun siirrytään takaisin kirjautumisnäkymään.
        """
        self._root = root
        self._handle_back_to_login = _handle_back_to_login
        self._current_view = None
        self._username_entry = None
        self._password_entry = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _create_user_handler(self):
        """Uuden käyttäjän luomisesta vastaava tapahtumankäsittelijä."""
        username_entry_value = self._username_entry.get()
        password_entry_value = self._password_entry.get()
        password_check_value = self._password_again_entry.get()

        if len(username_entry_value) < 5:
            self._show_error_message(
                "Käyttäjätunnus liian lyhyt (oltava vähintään 5 merkkiä)")
            return

        if len(password_entry_value) < 1:
            self._show_error_message("Syötä salasana")
            return

        if password_entry_value != password_check_value:
            self._show_error_message("Salasanat eivät täsmää")
            return
        try:
            user_service.create_new_user(
                username_entry_value, password_entry_value)
            self._show_error_message(
                f'Käyttäjätunnus  {username_entry_value} luotu')
            self._handle_back_to_login()

        except UserExistsError:
            self._show_error_message("Käyttäjä on jo olemassa")

    def _return_handler(self):
        """Palauttaa kirjautumisnäkymän."""
        self._handle_back_to_login()

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

    def _initialize(self):
        "Alustaa käyttäjän luonti -näkymän."
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, text="Luo uusi käyttäjä")
        username_label = ttk.Label(
            master=self._frame, text="Anna käyttäjätunnus")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Anna salasana")
        self._password_entry = ttk.Entry(master=self._frame)
        password_again_label = ttk.Label(
            master=self._frame, text="Salasana uudelleen")
        self._password_again_entry = ttk.Entry(master=self._frame)

        create_user_button = ttk.Button(
            master=self._frame,
            text="Luo uusi käyttäjä",
            command=self._create_user_handler
        )

        return_button = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._return_handler
        )

        self._error_var = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_var,
            foreground="blue"
        )

        heading_label.grid(row=0, column=0, padx=5, pady=5)
        username_label.grid(row=1, column=0, padx=5, pady=10)
        self._username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W, ), padx=5, pady=10)

        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        password_again_label.grid(row=3, column=0, padx=5, pady=5)
        self._password_again_entry.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        create_user_button.grid(row=4, column=1, padx=5,
                                pady=5, sticky=constants.E)

        return_button.grid(row=4, column=0, padx=5,
                           pady=5, sticky=constants.W)

        self._error_label.grid(row=5, column=1, padx=5,
                               pady=5, sticky=constants.E)

        self._hide_error()
