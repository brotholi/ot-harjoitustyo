from tkinter import ttk, constants
#from services.user_service import user_service

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

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text=f'Uusi treeni')
        label.grid(row=0, column=0, sticky=constants.W, padx=5, pady=5)
        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

