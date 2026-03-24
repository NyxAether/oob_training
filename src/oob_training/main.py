from oob_training.compte_bancaire_imperatif import (
    creer_compte,
    depot,
    retrait,
    solde,
    transfert,
)
from oob_training.compte_bancaire_oob import (
    CompteCourant,
    CompteDepot,
    CompteJoint,
    LivretA,
)
from oob_training.structures import TypeCompte


def suite_actions_imperatif() -> None:
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
    cc_isabelle, cj_isabelle = transfert(cc_isabelle, cj_isabelle, "isabelle", 500)

    # Jean retire 60 e de son livret A
    la_jean = retrait(la_jean, "jean", 60)

    cc_isabelle = depot(cc_isabelle, "isabelle", 30_000)

    # DÉBUT DES TESTS
    # Test des soldes des comptes
    assert solde(cc_isabelle, "isabelle") == 30800
    assert solde(la_jean, "jean") == 1140
    assert solde(cj_isabelle, "isabelle") == 7000

    # Le compte ne peut pas avoir de solde négatif
    try:
        retrait(cd_jean, "jean", 2000)
    except ValueError:
        print("Solde insuffisant correctement détecté")
    else:
        print("Une erreur aurait dû se produire")

    # L'utilisateur n'a pas les droits d'accès
    try:
        retrait(cc_isabelle, "jean", 500)
    except ValueError:
        print("Retrait non autorisé correctement détecté")
    else:
        print("Une erreur aurait dû se produire")

    # Le livret A ne peut pas avoir plus de 29500 €
    try:
        depot(la_jean, "jean", 29_000)
    except ValueError:
        print("Seuil max détecté")
    else:
        print("Une erreur aurait dû se produire")

    # Le livret A de Jean ne peut pas avoir plus de 29500 €
    try:
        cc_isabelle, la_jean = transfert(cc_isabelle, la_jean, "isabelle", 30_000)
    except ValueError:
        print("Seuil max détecté")
    else:
        print("Une erreur aurait dû se produire")

    assert solde(cc_isabelle, "isabelle") == 30800


def suite_actions_oob() -> None:
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
    try:
        cc_isabelle.retrait("jean", 500)
    except ValueError:
        print("Retrait non autorisé correctement détecté")
    else:
        print("Une erreur aurait dû se produire")

    # Le compte ne peut pas avoir de solde négatif
    try:
        cd_jean.retrait("jean", 2000)
    except ValueError:
        print("Solde insuffisant correctement détecté")
    else:
        print("Une erreur aurait dû se produire")

    # Le livret A ne peut pas avoir plus de 29500 €
    try:
        la_jean.depot("jean", 29_000)
    except ValueError:
        print("Seuil max détecté")
    else:
        print("Une erreur aurait dû se produire")

    cc_isabelle.depot("isabelle", 30_000)
    try:
        cc_isabelle.transfert(la_jean, "isabelle", 30_000)
    except ValueError:
        print("Seuil max détecté")
    else:
        print("Une erreur aurait dû se produire")

    assert cc_isabelle.solde("isabelle") == 30800


# suite_actions_imperatif()
# suite_actions_oob()
