from tkinter import ttk, constants
from login_view import LoginView
from create_user import CreateUserView


class UI:
    def _init_(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self.show_login_view()

    def _hide_current_view(self):
        self._hide_current_view

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
              self._root
        )

    def _show_logbook_view(self):
        self._hide_current_view()


    def _show_entry_view(self):
        self._hide_current_view()
        

    def _show_create_user_view(self):
        self._hide_current_view()
        self._current_view = CreateUserView(
            self._root
        )
        
    
