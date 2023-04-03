from tkinter import Tk, ttk, constants

#from services.gym_service import task_service, InvalidCredentialsError
class LoginView:

    def __init__(self, root):
        self._root = root
        self._current_view = None

        self._initialize()

    def pack(self):
        #näytä näkymä
        self._frame.pack(fill=constants.X)

    def destroy(self):
        #tuhoa näkymä
        self._frame.destroy()

    def _error(self):
        print("error")


    def _handle_login_button(self):
        username_entry_value = self._username_entry.get()
        password_entry_value = self._password_entry.get()
    
        print(f"Käyttäjätunnuksesi oli: {username_entry_value}")
        salasana = password_entry_value



    def _initialize(self):
    #kenttien alustus eri metodeihin?
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._root, text="Kirjautuminen")

        username_label = ttk.Label(master=self._root, text="Käyttäjätunnus")
        self._username_entry = ttk.Entry(master=self._root)

        password_label = ttk.Label(master=self._root, text="Salasana")
        self._password_entry = ttk.Entry(master=self._root)

        login_button = ttk.Button(
            master=self._root,
            text="Kirjaudu",
            command=self._handle_login_button
            )


        
        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=10, pady=10)
        username_label.grid(padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky =(constants.E, constants.W, ), padx=5, pady=5)
        password_label.grid(padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky =(constants.E, constants.W), padx=5, pady=5)

        login_button.grid(row=3, column=0, columnspan=2) 

        self._root.grid_columnconfigure(1, weight=1)
    
#Tämä eriytetään erilliseen tiedostoon?

window = Tk()
window.title("Lihasloki")

ui = LoginView(window)


window.mainloop()