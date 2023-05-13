from tkinter import ttk, constants, StringVar
from entities.log_entry import LogEntry
from services.user_service import user_service
from services.logbook_service import logbook_service


class ExerciseListView:
    """Treenille kirjattujen liikkeiden listauksesta vastaava näkymä."""


    def __init__(self, root, exercises):
        """Luokan konstruktori. Luo uuden aiemmin treenille kirjattujen liikkeiden listaamisesta vastaavan näkymän.
        Args:
            root:
                TKinter-elementti, johon näkymä alustetaan.
            exercises:
               Lista näytettävitä liikkeistä.
        """
        self._root = root
        self._exercises = exercises
        self._frame = None

        self._initialize()

    def pack(self):
        """"Näyttää nykyisen näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """"Tuhoaa nykyisen näkymän."""
        self._frame.destroy()

    def _initialize_exercise(self, exercise, set_number):
        """Alustaa yhden listattavan liikkeen."""
        item_frame = ttk.Frame(master=self._frame)
        if set_number == 1:
            separator = ttk.Separator(master=item_frame, orient='horizontal')
            separator.grid(sticky=constants.EW, columnspan=5)

            exercise_label = ttk.Label(
                master=item_frame, text=f'{exercise.name}')
            exercise_label.grid(row=3, column=0, padx=5,
                                pady=5, sticky=constants.W)

        label = ttk.Label(
            master=item_frame, text=f'{set_number}.  {exercise.weight}kg  x  {exercise.reps}')
        label.grid(row=4, column=0, padx=5, pady=5, sticky=constants.W)

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

    def _initialize(self):
        """Alustaa listausnäkymän."""
        self._frame = ttk.Frame(master=self._root)
        previous_name = ''
        set_number = 1

        for exercise in self._exercises:
            name = exercise.name
            if name != previous_name:
                set_number = 1
            self._initialize_exercise(exercise, set_number)
            previous_name = name
            set_number += 1


class ExerciseView:
    """Yksittäisten liikkeiden kirjaamisesta vastaava näkymä."""

    def __init__(self, root, handle_logbook_view):
        """Luokan konstruktori. Luo uuden yksittäiden liikkeiden kirjaamisesta vastaavan näkymän
        Args:
            root:
                TKinter-elementti, johon näkymä alustetaan.
            handle_logbook_view:
                Kutsuttava-arvo, jota kutsutaan kun siirrytään takaisin alkunäkymään.
            handle_exercise_view:
                Kutsuttava-arvo, jota kutsutaan kun siirrytään yksittäisten liikkeiden kirjausnäkymään.
        """
        self._root = root
        self._handle_logbook_view = handle_logbook_view
        self._current_view = None
        self._exercise_list_view = None
        self._exercise_list_frame = None

        self._initialize()

    def pack(self):
        """"Näyttää nykyisen näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """"Tuhoaa nykyisen näkymän."""
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

    def _set_exercise_done(self, set_number):
#////////pois????
        if set_number == 1:
            self._weigth_entry_1.grid_remove()
            self._reps_entry_1.grid_remove()

        if set_number == 2:
            self._weigth_entry_2.grid_remove()

        if set_number == 3:
            self._weigth_entry_3.grid_remove()

    def _create_exercise_handler(self):
        """Uuden liikkeen luomisesta vastaava tapahtumankäsittelijä"""

        for i in range(0, 3):
            name_entry_value = self._title_entry.get()
            if len(name_entry_value) == 0:
                self._show_error_message("Syötä liikkeen nimi")
                return

            if i == 0:
                weigth_entry_value = self._weigth_entry_1.get()
                reps_entry_value = self._reps_entry_1.get()

            if i == 1:
                weigth_entry_value = self._weigth_entry_2.get()
                reps_entry_value = self._reps_entry_2.get()

            if i == 2:
                weigth_entry_value = self._weigth_entry_3.get()
                reps_entry_value = self._reps_entry_3.get()

            weight_number = weigth_entry_value.isdigit()
            reps_number = reps_entry_value.isdigit()

            if weight_number == False or reps_number == False:
                self._show_error_message("Syötä paino ja toistot numeroina")
                return
            logbook_service.create_new_exercise(name_entry_value, weigth_entry_value, reps_entry_value)

        self._title_entry.delete(0, constants.END)
        self._weigth_entry_1.delete(0, constants.END)
        self._reps_entry_1.delete(0, constants.END)
        self._weigth_entry_2.delete(0, constants.END)
        self._reps_entry_2.delete(0, constants.END)
        self._weigth_entry_3.delete(0, constants.END)
        self._reps_entry_3.delete(0, constants.END)

        self._hide_error()
        self._initialize_exercise_list()

        return

    def _save_logentry_handler(self):
        self._handle_logbook_view()

    def __initialize_header(self):
        username = user_service.get_current_user()
        log = logbook_service.find_current_log(username)

        title = ttk.Label(
            master=self._frame, text=f'{log.logtitle}')

        title.grid(
            row=0, column=0, sticky=constants.W, padx=5, pady=5)

        date = ttk.Label(
            master=self._frame, text=f'{log.logdate}')

        date.grid(
            row=0, column=1, sticky=constants.E, padx=5, pady=5)

    def _initialize_exercise_list(self):
        """Alustaa listanäkymän, johon viedään nykyiselle kirjaukselle kirjatut liikeet."""
        if self._exercise_list_view:
            self._exercise_list_view.destroy()

        username = user_service.get_current_user()
        log = logbook_service.find_current_log(username)

        exercises = logbook_service.find_logentry_exercises(log.id)

        self._exercise_list_view = ExerciseListView(
            self._exercise_list_frame,
            exercises
        )

        self._exercise_list_view.pack()

    def _initialize_add_exercise(self):
        """Alustaa treenin kirjaamiseen liittyvät tkinter-elementit."""
        separator = ttk.Separator(master=self._frame, orient='horizontal')
        separator.grid(row=2, sticky=constants.EW, columnspan=5)

        title_entry_label = ttk.Label(master=self._frame, text="Liike:")
        self._title_entry = ttk.Entry(master=self._frame, width=20)

        title_entry_label.grid(
            row=3, column=0, sticky=constants.W, padx=5, pady=5)

        self._title_entry.grid(
            row=3, column=1, sticky=constants.W, padx=5, pady=5)

        set_heading_label = ttk.Label(master=self._frame, text='sarja')
        weight_heading_label = ttk.Label(master=self._frame, text='kg')
        reps_heading_label = ttk.Label(master=self._frame, text='toistot')

        set_heading_label.grid(row=4, column=0, padx=5,
                               pady=5, sticky=constants.W)
        weight_heading_label.grid(
            row=4, column=0, padx=5, pady=5, sticky=constants.E)
        reps_heading_label.grid(row=4, column=1, padx=5,
                                pady=5, sticky=constants.W)

        self._initialize_exercise_rows()

    def _initialize_exercise_rows(self):
        """Alustaa entry-kentät, joihin kirjataan kolmen sarjan liikkeiden tiedot."""
        set_label_1 = ttk.Label(master=self._frame, text="1", width=2)
        self._weigth_entry_1 = ttk.Entry(master=self._frame, width=4)
        self._reps_entry_1 = ttk.Entry(master=self._frame, width=4)

        done_button_1 = ttk.Button(
            master=self._frame,
            text="✓",
            command=self._set_exercise_done(1)
        )

        set_label_1.grid(row=5, column=0, padx=5, pady=5, sticky=constants.W)
        self._weigth_entry_1.grid(
            row=5, column=0, padx=5, pady=5, sticky=constants.E)
        self._reps_entry_1.grid(row=5, column=1, padx=5,
                                pady=5, sticky=constants.W)
        done_button_1.grid(row=5, column=1, padx=5, pady=5, sticky=constants.E)

        set_label_2 = ttk.Label(master=self._frame, text="2", width=2)
        self._weigth_entry_2 = ttk.Entry(master=self._frame, width=4)
        self._reps_entry_2 = ttk.Entry(master=self._frame, width=4)

        done_button_2 = ttk.Button(
            master=self._frame,
            text="✓",
            command=self._set_exercise_done(2)
        )

        set_label_2.grid(row=6, column=0, padx=5, pady=5, sticky=constants.W)
        self._weigth_entry_2.grid(
            row=6, column=0, padx=5, pady=5, sticky=constants.E)
        self._reps_entry_2.grid(row=6, column=1, padx=5,
                                pady=5, sticky=constants.W)
        done_button_2.grid(row=6, column=1, padx=5, pady=5, sticky=constants.E)

        set_label_3 = ttk.Label(master=self._frame, text="3", width=2)
        self._weigth_entry_3 = ttk.Entry(master=self._frame, width=4)
        self._reps_entry_3 = ttk.Entry(master=self._frame, width=4)

        done_button_3 = ttk.Button(
            master=self._frame,
            text="✓",
            command=self._set_exercise_done(3)
        )

        set_label_3.grid(row=7, column=0, padx=5, pady=5, sticky=constants.W)
        self._weigth_entry_3.grid(
            row=7, column=0, padx=5, pady=5, sticky=constants.E)
        self._reps_entry_3.grid(row=7, column=1, padx=5,
                                pady=5, sticky=constants.W)
        done_button_3.grid(row=7, column=1, padx=5, pady=5, sticky=constants.E)

    def __inilialize_footer(self):
        add_exercise_button = ttk.Button(
            master=self._frame,
            text="Lisää liike",
            command=self._create_exercise_handler
        )

        save_button = ttk.Button(
            master=self._frame,
            text="Tallenna treeni",
            command=self._save_logentry_handler
        )

        self._error_var = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_var,
            foreground="red"
        )

        add_exercise_button.grid(column=1, padx=5,
                                 pady=5, sticky=constants.E)

        save_button.grid(row=20, column=1, padx=5,
                         pady=5, sticky=constants.E)

        self._error_label.grid(row=7, column=1, padx=5,
                               pady=5, sticky=constants.E)

        self._hide_error()

    def _initialize(self):
        """Alustaa näkymän."""
        self._frame = ttk.Frame(master=self._root)
        self._exercise_list_frame = ttk.Frame(master=self._frame)

        self.__initialize_header()
        self._initialize_exercise_list()
        self._initialize_add_exercise()
        self.__inilialize_footer()

        self._exercise_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
