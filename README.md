# Gestion de comptes bancaires

L'objectif de ce TP est d'implémenter un code qui gère des comptes bancaires. Ce TP vous demandera d'implémenter ce code deux fois : le premier en restant sur un paradigme procédural, puis la seconde implémentation ou chaque compte bancaire sera un objet.

## Spécifications
Voici les spécifications qui vous sont demandées de vérifier pour vos implémentations :
 - Quatre types de comptes sont possibles :
    - le compte courant
    - le compte de dépot
    - le livret A
    - le compte joint
 - Un compte est constitué d'un propriétaire et d'un solde
 - Seul le propriétaire d'un compte peut faire un retrait
 - Un propriétaire peut déposer de l'argent ou en retirer (sauf cas particuliers. Voir plus bas)
 - Un propriétaire peut transférer de l'argent (avec les mêmes contraintes que pour le retrait ou le dépot) sur un de ses comptes ou d'un autre propriétaire

En fonction du type de compte, un certain nombre de contraintes sont à vérifier :
 - Un compte de dépot ne peut pas avoir un solde négatif
 - Un livret A ne peut pas avoir un solde supérieur à 29 500 €
 - Un compte joint doit avoir deux propriétaires

 ## Suite d'opérations
Le code dans `tests/test_imperatif.py` va effectuer une série d'actions bancaires et quelques vérifications à l'issue de celles-ci.
Pour fonctionner, le code nécessite l'implémentation de cinq fonctions dans `src/oob_training/compte_bancaire_oob.py`.

Commencer par lire et comprendre le code.

## Implémentation impérative
Le code de test `tests/test_imperatif.py` doit pouvoir s'exécuter normalement. Vous allez devoir implémenter les méthodes :
 - `creer_comptes`
 - `depot`
 - `retrait`
 - `transfert`
 - `solde`

Lorsqu'un compte sera créé, il sera ajouté dans le registre des comptes.
À vous d'implémenter ces fonctions. Vous pouvez ajouter toutes les fonctions ou structures de données que vous souhaitez, mais ne créez pas de classes pour le moment.

Vous pouvez tenter de lancer les tests à tout moment.

## Implémentation objet

Même exercice que précédemment, mais vous devrez cette fois implémenter les différents types de compte bancaire en tant qu'objet dans `src/oob_training/compte_bancaire_oob.py`.

Toutes les classes de compte que vous créerez devront hériter de la classe `Compte` que vous devez également définir.

Le code de test correspondant est dans le fichier `tests/test_oob.py`.