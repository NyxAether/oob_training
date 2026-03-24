from oob_training.structures import TypeCompte

Compte = tuple[TypeCompte, int, str, str | None]


def creer_compte(
    type_compte: TypeCompte, proprietaire: str, proprietaire2: str | None = None
) -> Compte:
    assert (type_compte is TypeCompte.COMPTE_JOINT) != (proprietaire2 is None)
    return type_compte, 0, proprietaire, proprietaire2


def _verifier_proprietaire(compte: Compte, demandeur: str) -> None:
    if not est_proprietaire(compte, demandeur):
        raise ValueError(f"{demandeur} n'est pas autorisé à agir sur le compte.")


def _set_montant(compte: Compte, montant: int) -> Compte:
    type_compte, solde, p1, p2 = compte
    if type_compte is TypeCompte.LIVRET_A and solde + montant > 29500:
        raise ValueError("Seuil maximal de 29 500 € atteint")
    if type_compte is TypeCompte.COMPTE_DEPOT and solde + montant < 0:
        raise ValueError("Solde insuffisant")
    return type_compte, solde + montant, p1, p2


def depot(compte: Compte, demandeur: str, montant: int) -> Compte:
    _verifier_proprietaire(compte, demandeur)
    return _set_montant(compte, montant)


def retrait(compte: Compte, demandeur: str, montant: int) -> Compte:
    _verifier_proprietaire(compte, demandeur)
    return _set_montant(compte, -montant)


def transfert(
    compte_source: Compte, compte_cible: Compte, demandeur: str, montant: int
) -> tuple[Compte, Compte]:
    _verifier_proprietaire(compte_source, demandeur)
    compte_source = _set_montant(compte_source, -montant)
    compte_cible = _set_montant(compte_cible, montant)
    return compte_source, compte_cible


def solde(compte: Compte, demandeur: str) -> int:
    _verifier_proprietaire(compte, demandeur)
    return compte[1]


def est_proprietaire(compte: Compte, personne: str) -> bool:
    _, _, p1, p2 = compte
    return personne == p1 or p2 is not None and personne == p2
