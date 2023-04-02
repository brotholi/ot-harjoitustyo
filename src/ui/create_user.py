from tkinter import Tk, ttk, constants

class CreateUserView:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()


    def _create_user_handler(self):
        username_entry_value = self._username_entry.get()
        print(f"Uusi käyttäjä luotu: {username_entry_value}")
        

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        #root & frame?
        heading_label = ttk.Label(master=self._root, text="Luo uusi käyttäjä")
        username_label = ttk.Label(master=self._root, text="Anna käyttäjätunnus")
        self._username_entry = ttk.Entry(master=self._root)

        password_label = ttk.Label(master=self._root, text="Anna salasana")
        self._password_entry = ttk.Entry(master=self._root)
        password_again_label = ttk.Label(master=self._root, text="Salasana uudelleen")
        self._password_again_entry = ttk.Entry(master=self._root)

        create_user_button = ttk.Button(
            master=self._root,
            text="Luo uusi käyttäjä",
            command=self._create_user_handler
        )

        heading_label.grid(row=0, column=0, padx=5, pady=5)
        username_label.grid(row=1, column=0, padx=5, pady=10)
        self._username_entry.grid(row=1, column=1, sticky =(constants.E, constants.W, ), padx=5, pady=10)
        
        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky =(constants.E, constants.W), padx=5, pady=5)

        password_again_label.grid(row=3, column=0, padx=5, pady=5)
        self._password_again_entry.grid(row=3, column=1, sticky =(constants.E, constants.W), padx=5, pady=5)

        
        create_user_button.grid(row=4, column=1, padx=5, pady=5, sticky=constants.E)
        


window = Tk()
window.title("Lihasloki")

ui = CreateUserView(window)

window.mainloop()