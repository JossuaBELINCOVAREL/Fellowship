# Fellowship

# Projet : Application kool

## Description
Cette application permet de tirer au sort 4 utilisateurs aléatoires chaque semaine à partir d'une base de données. L'objectif est de créer un moment de convivialité entre personnes en télétravail. Les utilisateurs sont stockés dans une base de données SQLite, et l'application vérifie que les mêmes utilisateurs ne sont pas sélectionnés plusieurs fois avant que tout le monde ait été tiré au sort.

## Fonctionnalités
- **Ajout d'utilisateurs** : Ajouter des utilisateurs avec nom, prénom et email.
- **Tirage aléatoire** : Sélection de 4 utilisateurs aléatoires chaque semaine.
- **Stockage des tirages** : Un historique des tirages est conservé pour éviter de tirer les mêmes personnes plusieurs fois avant que tout le monde ait été tiré.
- **Automatisation** : Le tirage est programmé pour avoir lieu chaque semaine.

## Technologies Utilisées
- **Python 3** : Langage de programmation.
- **SQLite** : Base de données pour stocker les utilisateurs et les tirages.

## Prérequis

### Logiciels nécessaires :
1. **Python 3.x** : [Télécharger Python ici](https://www.python.org/downloads/)
2. **Pip** : Gestionnaire de packages Python (généralement installé avec Python).
3. **Virtualenv (Optionnel)** : Pour créer un environnement virtuel propre à votre projet.

## Étapes pour Exécuter le Projet

1. **Cloner le projet** sur votre machine ou copier les fichiers source dans un dossier.

   Si le projet est hébergé sur un dépôt Git, vous pouvez utiliser la commande suivante pour le cloner :

   ```bash
   git clone <URL_DU_REPOSITORY>
   ```
2. **Créer un environnement virtuel** (optionnel mais recommandé)

   Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances du projet. Voici comment en créer un :

   ```bash
   python -m venv env
   env\Scripts\activate
   ```
   Cela créera un environnement virtuel dans le dossier et l'activera.

3. **Exécuter le script principal**

    Exécutez le fichier mainfile.py pour voir comment tout fonctionne. Cela permettra de :

    - Créer la base de données users.db (si elle n'existe pas déjà).
    - Ajouter des utilisateurs à la base de données.
    - Effectuer un tirage au sort parmi les utilisateurs.

    Utilisez cette commande pour exécuter le script :  

    ```bash
    python mainfile.py
    ```
    Si tout est configuré correctement, le script affichera les utilisateurs ajoutés et le résultat du tirage au sort.

## Personnalisation

Si vous souhaitez personnaliser le nombre d'utilisateurs tirés ou les règles de sélection, vous pouvez modifier le fichier tirage.py et adapter la logique en fonction de vos besoins.

## Contribution

Si vous souhaitez contribuer à ce projet :

   - Clonez le repository
   - Créez une nouvelle branche (git checkout -b ma-branche).
   - Faites vos modifications.
   - Soumettez une Pull Request.