from oob_training.structures import TypeCompte


Compte = tuple[TypeCompte, int, str, str | None]


def creer_compte(
    type_compte: TypeCompte, proprietaire: str, proprietaire2: str | None = None
) -> Compte:
    # Votre code ici
    pass


def depot(compte: Compte, demandeur: str, montant: int) -> Compte:
    # Votre code ici
    pass


def retrait(compte: Compte, demandeur: str, montant: int) -> Compte:
    # Votre code ici
    pass


def transfert(
    compte_source: Compte,
    compte_cible: Compte,
    demandeur: str,
    montant: int,
) -> tuple[Compte, Compte]:
    # Votre code ici
    pass


def solde(compte: Compte, demandeur: str) -> int:
    # Votre code ici
    pass
