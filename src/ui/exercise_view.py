from tkinter import ttk, constants
from entities.log_entry import LogEntry
from services.user_service import user_service
from services.logbook_service import logbook_service


class ExerciseView:

    def __init__(self, root, handle_logentry_view, handle_logbook_view):
        self._root = root
        self._handle_logentry_view = handle_logentry_view
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
        self._handle_logentry_view()

    def _create_exercise_handler(self):
        username = user_service.get_current_user()
        log = logbook_service.find_current_log(username)

        name_entry_value = self._title_entry.get()
        weigth_entry_value = self._weigth_entry_1.get()
        reps_entry_value = self._reps_entry_1.get()

        new_exercise = logbook_service.create_new_exercise(
            log.id, name_entry_value, weigth_entry_value, reps_entry_value)

        return new_exercise

    def _save_logentry_handler(self):
        self._handle_logbook_view()
    
    def _row_done_handler(self, button):
        if button == "button a":
            self._hide_row_entries()
        

    def _hide_row_entries(self):
        self._title_entry.grid_remove()
        self._weigth_entry.grid_remove()
        self._reps_entry.grid_remove()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self.__initialize_header()
        self._initialize_add_exercise()
        self.__inilialize_footer()

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

    def __initialize_header(self):
        # tähän tuodaan otsikko, joka annettiin äsken treenille
        username = user_service.get_current_user()
        log = logbook_service.find_current_log(username)

        title = ttk.Label(
            master=self._frame, text=f'{log.logtitle}', width=10)

        title.grid(
            row=0, column=0, sticky=constants.W, padx=5, pady=5)

        date = ttk.Label(
            master=self._frame, text=f'{log.logdate}')

        date.grid(
            row=0, column=1, sticky=constants.E, padx=5, pady=5)

    def _initialize_add_exercise(self):
        title_entry_label = ttk.Label(master=self._frame, text="Liike:")
        self._title_entry = ttk.Entry(master=self._frame, width=8)

        title_entry_label.grid(
            row=1, column=0, sticky=constants.W, padx=5, pady=5)
        

        self._title_entry.grid(row=1, column=1, sticky=constants.W, padx=5, pady=5)

        set_heading_label = ttk.Label(master=self._frame, text= 'sarja')
        weight_heading_label = ttk.Label(master=self._frame, text= 'kg')
        reps_heading_label = ttk.Label(master=self._frame, text= 'toistot')


        set_heading_label.grid(row=2, column=0, padx=5,pady=5, sticky=constants.W)
        weight_heading_label.grid(row=2, column=0, padx=5,pady=5, sticky=constants.E)
        reps_heading_label.grid(row=2, column=1, padx=5,pady=5, sticky=constants.W)

        self.initialize_exercise_rows()
        

    def initialize_exercise_rows(self):
        set_label_1 = ttk.Label(master=self._frame, text="1", width=2)
        self._weigth_entry_1 = ttk.Entry(master=self._frame, width=4)
        self._reps_entry_1 = ttk.Entry(master=self._frame, width=4)

        set_label_1.grid(row=3, column=0, padx=5,pady=5, sticky=constants.W)
        self._weigth_entry_1.grid(row=3, column=0, padx=5,pady=5, sticky=constants.E)
        self._reps_entry_1.grid(row=3, column=1, padx=5,pady=5, sticky=constants.W)

        set_label_2 = ttk.Label(master=self._frame, text="2", width=2)
        self._weigth_entry_2 = ttk.Entry(master=self._frame, width=4)
        self._reps_entry_2 = ttk.Entry(master=self._frame, width=4)

        set_label_2.grid(row=4, column=0, padx=5,pady=5, sticky=constants.W)
        self._weigth_entry_2.grid(row=4, column=0, padx=5,pady=5, sticky=constants.E)
        self._reps_entry_2.grid(row=4, column=1, padx=5,pady=5, sticky=constants.W)

        set_label_3 = ttk.Label(master=self._frame, text="3", width=2)
        self._weigth_entry_3 = ttk.Entry(master=self._frame, width=4)
        self._reps_entry_3 = ttk.Entry(master=self._frame, width=4)

        set_label_3.grid(row=5, column=0, padx=5,pady=5, sticky=constants.W)
        self._weigth_entry_3.grid(row=5, column=0, padx=5,pady=5, sticky=constants.E)
        self._reps_entry_3.grid(row=5, column=1, padx=5,pady=5, sticky=constants.W)


    def __inilialize_footer(self):

        add_exercise_button = ttk.Button(
            master=self._frame,
            text="Lisää",
            command=self._create_exercise_handler
        )

        save_button = ttk.Button(
            master=self._frame,
            text="Tallenna treeni",
            command=self._save_logentry_handler
        )

        return_button = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._return_handler
        )

        add_exercise_button.grid(column=1, padx=5,
                                 pady=5, sticky=constants.E)

        save_button.grid(row=20, column=1, padx=5,
                         pady=5, sticky=constants.E)

        return_button.grid(row=20, column=0, padx=5,
                           pady=5, sticky=constants.W)
