from tkinter import Tk, ttk, constants


class LogbookView:

    def __init__(self, root, _handle_logbook_view):
        self._root = root
        self._handle_logbook_view = _handle_logbook_view
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _error(self):
        print("error")

    def _hide_error(self):
        self._error_label.grid_remove()

    