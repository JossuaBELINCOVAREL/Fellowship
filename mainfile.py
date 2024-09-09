import db_utils
import tirage

# Créer la table des utilisateurs (si elle n'existe pas déjà)
db_utils.creer_table()

# Créer la table des tirages (si elle n'existe pas déjà)
db_utils.creer_table_draws()

# Ajouter quelques utilisateurs
db_utils.ajouter_utilisateur('Dupont', 'Jean', 'jean.dupont@example.com')
db_utils.ajouter_utilisateur('Martin', 'Sophie', 'sophie.martin@example.com')
db_utils.ajouter_utilisateur('Durand', 'Pierre', 'pierre.durand@example.com')
db_utils.ajouter_utilisateur('Leroy', 'Alice', 'alice.leroy@example.com')

# Effectuer le tirage
tirage.tirer_au_sort()

# Lister les utilisateurs pour vérifier
# db_utils.lister_utilisateurs()
