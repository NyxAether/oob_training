class Compte:
    def __init__(self, proprietaire: str) -> None:
        self._proprietaire = proprietaire
        self._solde = 0

    def _verifier_proprietaire(self, demandeur: str) -> None:
        if not self.est_proprietaire(demandeur):
            raise ValueError(f"{demandeur} n'est pas autorisé à agir sur le compte.")

    def _ajoute_solde(self, montant: int) -> None:
        self._solde += montant

    def depot(self, demandeur: str, montant: int) -> None:
        self._verifier_proprietaire(demandeur)
        self._ajoute_solde(montant)

    def retrait(self, demandeur: str, montant: int) -> None:
        self._verifier_proprietaire(demandeur)
        self._ajoute_solde(-montant)

    def solde(self, demandeur: str) -> int:
        self._verifier_proprietaire(demandeur)
        return self._solde

    def transfert(self, autre: "Compte", demandeur: str, montant: int) -> None:
        self._verifier_proprietaire(demandeur)
        self._ajoute_solde(-montant)
        try:
            autre._ajoute_solde(montant)
        except ValueError as e:
            self._ajoute_solde(montant)
            raise e

    def est_proprietaire(self, proprietaire: str) -> bool:
        return self._proprietaire == proprietaire


class CompteCourant(Compte):
    pass


class CompteDepot(Compte):
    def _ajoute_solde(self, montant: int) -> None:
        if self._solde + montant < 0:
            raise ValueError("Pas de découvert possible.")
        super()._ajoute_solde(montant)


class LivretA(Compte):
    def _ajoute_solde(self, montant: int) -> None:
        if self._solde + montant > 29500:
            raise ValueError("Plafond dépassé.")
        super()._ajoute_solde(montant)


class CompteJoint(Compte):
    def __init__(self, proprietaire: str, proprietaire2: str) -> None:
        super().__init__(proprietaire)
        self._proprietaire2 = proprietaire2

    def est_proprietaire(self, proprietaire: str) -> bool:
        return proprietaire in {self._proprietaire, self._proprietaire2}
