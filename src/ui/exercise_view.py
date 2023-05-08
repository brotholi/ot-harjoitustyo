from tkinter import ttk, constants
from entities.log_entry import LogEntry
from services.user_service import user_service
from services.logbook_service import logbook_service


class ExerciseView:

    def __init__(self, root, handle_logentry_view):
        self._root = root
        self._handle_logentry_view = handle_logentry_view
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

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        
        self.__initialize_header()
        self._inilialize_footer()
    
        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

    def __initialize_header(self):
        #tähän tuodaan otsikko, joka annettiin äsken treenille
        username = user_service.get_current_user()
        log = logbook_service.find_current_log(username)
        
        title = ttk.Label(
            master=self._frame, text=f'{log.logtitle}')
        
        title.grid(
            row=0, column=0, sticky=constants.W, padx=5, pady=5)
        
        date = ttk.Label(
            master=self._frame, text=f'{log.logdate}')
        
        date.grid(
            row=0, column=2, sticky=constants.E, padx=5, pady=5)
        

    def _inilialize_footer(self):
        return_button = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._return_handler
        )

        return_button.grid(row=6, column=0, padx=5,
                pady=5, sticky=constants.W)

    

