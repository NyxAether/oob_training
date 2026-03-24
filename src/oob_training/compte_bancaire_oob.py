class Compte:
    def __init__(self, proprietaire: str):
        # Votre code ici
        NotImplemented

    def solde(self, demandeur: str) -> int:
        # Votre code ici
        NotImplemented

    def depot(self, demandeur: str, montant: int) -> None:
        # Votre code ici
        NotImplemented

    def retrait(self, demandeur: str, montant: int) -> None:
        # Votre code ici
        NotImplemented

    def transfert(self, other: "Compte", demandeur: str, montant: int) -> None:
        # Votre code ici
        NotImplemented


class CompteCourant(Compte):
    # Votre code ici
    pass


class CompteDepot(Compte):
    # Votre code ici
    pass


class LivretA(Compte):
    # Votre code ici
    pass


class CompteJoint(Compte):
    # Votre code ici
    pass
