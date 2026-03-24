import pytest

from oob_training.compte_bancaire_imperatif import (
    creer_compte,
    depot,
    retrait,
    solde,
    transfert,
)
from oob_training.structures import TypeCompte


def test_imperatif() -> None:
    # Isabelle ouvre un compte courant et ajoute 1300 €
    cc_isabelle = creer_compte(TypeCompte.COMPTE_COURANT, "isabelle")
    cc_isabelle = depot(cc_isabelle, "isabelle", 1300)

    # Jean ouvre un compte epargne et ajoute 1000 €
    cd_jean = creer_compte(TypeCompte.COMPTE_DEPOT, "jean")
    cd_jean = depot(cd_jean, "jean", 1000)

    # Jean ouvre un livret A et ajoute 1200 €
    la_jean = creer_compte(TypeCompte.LIVRET_A, "jean")
    la_jean = depot(la_jean, "jean", 1200)

    # Isabelle et Jean ouvre un compte joint et dépose 6500 €
    cj_isabelle = creer_compte(TypeCompte.COMPTE_JOINT, "isabelle", "jean")
    cj_isabelle = depot(cj_isabelle, "isabelle", 6500)

    # Isabelle transfert 500 € de son compte courant vers le compte joint
    cc_isabelle, cj_isabelle = transfert(cc_isabelle, cj_isabelle, "isabelle", 500)  # noqa: F821

    # Jean retire 60 e de son livret A
    la_jean = retrait(la_jean, "jean", 60)

    cc_isabelle = depot(cc_isabelle, "isabelle", 30_000)

    # DÉBUT DES TESTS
    # Test des soldes des comptes
    assert solde(cc_isabelle, "isabelle") == 30800
    assert solde(la_jean, "jean") == 1140
    assert solde(cj_isabelle, "isabelle") == 7000

    # Le compte ne peut pas avoir de solde négatif
    with pytest.raises(ValueError):
        retrait(cd_jean, "jean", 2000)

    # L'utilisateur n'a pas les droits d'accès
    with pytest.raises(ValueError):
        retrait(cc_isabelle, "jean", 500)

    # Le livret A ne peut pas avoir plus de 29500 €
    with pytest.raises(ValueError):
        depot(la_jean, "jean", 29_000)

    # Le livret A de Jean ne peut pas avoir plus de 29500 €
    with pytest.raises(ValueError):
        cc_isabelle, la_jean = transfert(cc_isabelle, la_jean, "isabelle", 30_000)

    assert solde(cc_isabelle, "isabelle") == 30800
