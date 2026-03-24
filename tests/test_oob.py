import pytest

from oob_training.compte_bancaire_oob import (
    CompteCourant,
    CompteDepot,
    CompteJoint,
    LivretA,
)


def test_oob() -> None:
    # Isabelle ouvre un compte courant et ajoute 1300 €
    cc_isabelle = CompteCourant("isabelle")
    cc_isabelle.depot("isabelle", 1300)

    # Jean ouvre un compte epargne et ajoute 1000 €
    cd_jean = CompteDepot("jean")
    cd_jean.depot("jean", 1000)

    # Jean ouvre un livret A et ajoute 1200 €
    la_jean = LivretA("jean")
    la_jean.depot("jean", 1200)

    # Isabelle et Jean ouvre un compte joint et dépose 6500 €
    cj_isabelle = CompteJoint("isabelle", "jean")
    cj_isabelle.depot("isabelle", 6500)

    # Isabelle transfert 500 € de son compte courant vers le compte joint
    cc_isabelle.transfert(cj_isabelle, "isabelle", 500)

    # Jean retire 60 e de son livret A
    la_jean.retrait("jean", 60)

    # DÉBUT DES TESTS
    # Test des soldes des comptes
    assert cc_isabelle.solde("isabelle") == 800
    assert la_jean.solde("jean") == 1140
    assert cj_isabelle.solde("isabelle") == 7000

    # L'utilisateur n'a pas les droits d'accès
    with pytest.raises(ValueError):
        cc_isabelle.retrait("jean", 500)

    # Le compte ne peut pas avoir de solde négatif
    with pytest.raises(ValueError):
        cd_jean.retrait("jean", 2000)

    # Le livret A ne peut pas avoir plus de 29500 €
    with pytest.raises(ValueError):
        la_jean.depot("jean", 29_000)

    cc_isabelle.depot("isabelle", 30_000)
    with pytest.raises(ValueError):
        cc_isabelle.transfert(la_jean, "isabelle", 30_000)

    assert cc_isabelle.solde("isabelle") == 30800
