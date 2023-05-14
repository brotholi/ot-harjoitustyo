from datetime import datetime


class LogEntry:
    """Luokka, joka kuvaa yksittäistä treenikirjausta.

    Attributes:
        user: Merkkijonoarvo, joka kuvaa kirjausta tehneen käyttäjän käyttäjätunnusta.
        logtitle: Merkkijonoarvo, joka kuvaa kirjausta otsikkoa.
        logdate: Merkkijonoarvo, joka kuvaa kirjauksen päivämäärää.
    """

    def __init__(self, user: str, logtitle: str, logdate: datetime, logentry_id: str):
        """Luokan konstruktori, joka luo uuden kirjauksen.
        Args:
            user: Merkkijonoarvo, joka kuvaa kirjausta tehneen käyttäjän käyttäjätunnusta.
            logtitle: Merkkijonoarvo, joka kuvaa kirjausta otsikkoa.
            logtitle: Merkkijonoarvo, joka kuvaa kirjausta otsikkoa.
            logdate: Merkkijonoarvo, joka kuvaa kirjauksen päivämäärää.
        """
        self.user = user
        self.logtitle = logtitle
        self.logdate = logdate
        self.logid = logentry_id
