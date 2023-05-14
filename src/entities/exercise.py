class Exercise:
    """Luokka, joka kuvaa yksittäistä liikettä.

    Attributes:
        name: Merkkijonoarvo, joka kuvaa liikkeen nimeä.
        weight: Merkkijonoarvo, joka kuvaa liikkeen lisäpainoa.
        reps: Merkkijonoarvo, joka kuvaa liikkeen toistoja.
    """

    def __init__(self, exercise_name: str, weight: str, reps: str):
        """Luokan konstruktori, joka luo uuden liikkeen.
        Args:
            exercise_name: Merkkijonoarvo, joka kuvaa liikkeen nimeä.
            weight: Merkkijonoarvo, joka kuvaa liikkeen lisäpainoa.
            reps: Merkkijonoarvo, joka kuvaa liikkeen toistoja.
        """
        self.name = exercise_name
        self.weight = weight
        self.reps = reps
