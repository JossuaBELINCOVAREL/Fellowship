# Fellowship

# Projet : Application de Tirage au Sort Aléatoire

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
- **Faker** : Génération de faux utilisateurs pour les tests.

## Prérequis

### Logiciels nécessaires :
1. **Python 3.x** : [Télécharger Python ici](https://www.python.org/downloads/)
2. **Pip** : Gestionnaire de packages Python (généralement installé avec Python).
3. **Virtualenv (Optionnel)** : Pour créer un environnement virtuel propre à votre projet.

### Bibliothèques Python à installer :
Vous aurez besoin de la librairie `Faker` pour générer des faux utilisateurs.

#### Installation des dépendances :

Ouvrez un terminal dans le dossier de votre projet et exécutez la commande suivante pour installer `Faker` :

```bash
pip install faker
```

#### Étapes pour Exécuter le Projet

1. **Cloner le projet** sur votre machine ou copier les fichiers source dans un dossier.

   Si le projet est hébergé sur un dépôt Git, vous pouvez utiliser la commande suivante pour le cloner :

   ```bash
   git clone <URL_DU_REPOSITORY>
   ```

