class User:
    """Luokka, joka kuvaa yhtä käyttäjää
    Attributes:
        username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta.
        password: Merkkijonoarvo, joka kuvaa käyttäjän salasanaa.
    """
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
