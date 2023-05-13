class Exercise:
    """Luokka, joka kuvaa yksittäistä liikettä.

    Attributes:
        name: Merkkijonoarvo, joka kuvaa liikkeen nimeä.
        weigth: Merkkijonoarvo, joka kuvaa liikkeen lisäpainoa.
        reps: Merkkijonoarvo, joka kuvaa liikkeen toistoja.
    """
    def __init__(self, exercise_name: str, weigth: str, reps: str):
        """Luokan konstruktori, joka luo uuden liikkeen.
        Args:
            exercise_name: Merkkijonoarvo, joka kuvaa liikkeen nimeä.
            weigth: Merkkijonoarvo, joka kuvaa liikkeen lisäpainoa.
            reps: Merkkijonoarvo, joka kuvaa liikkeen toistoja.
        """
        self.name = exercise_name
        self.weight = weigth
        self.reps = reps
