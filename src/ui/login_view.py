from tkinter import Tk, ttk
#from services.gym_service import task_service, InvalidCredentialsError
class UI:

    def __init__(self, root):
        self._root = root

    def start(self):
        #label_label = ttk.Label(master=self._root, text = "Lihasloki")
        heading_label = ttk.Label(master=self._root, text="Kirjaudu")

        username_label = ttk.Label(master=self._root, text="Käyttäjätunnus")
        username_entry = ttk.Entry(master=self._root)

        password_label = ttk.Label(master=self._root, text="Salasana")
        password_entry = ttk.Entry(master=self._root)

        login_button = ttk.Button(master=self._root, text="Kirjaudu")


        #label_label.pack()
        heading_label.grid(row=0, column=0, columnspan=2)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)
        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)

        login_button.grid(row=3, column=0, columnspan=2)

    

window = Tk()
window.title("LihasLoki")

ui = UI(window)
ui.start()

window.mainloop()

