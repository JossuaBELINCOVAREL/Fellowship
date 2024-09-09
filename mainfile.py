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
db_utils.ajouter_utilisateur('Garcia', 'Matthew', 'matthew.garcia@example.com')
db_utils.ajouter_utilisateur('Johnson', 'Olivia', 'olivia.johnson@example.com')
db_utils.ajouter_utilisateur('Martinez', 'Christopher', 'christopher.martinez@example.com')
db_utils.ajouter_utilisateur('Davis', 'Emma', 'emma.davis@example.com')
db_utils.ajouter_utilisateur('Lopez', 'Isabella', 'isabella.lopez@example.com')
db_utils.ajouter_utilisateur('Perez', 'Liam', 'liam.perez@example.com')
db_utils.ajouter_utilisateur('Brown', 'Sophia', 'sophia.brown@example.com')
db_utils.ajouter_utilisateur('Wilson', 'James', 'james.wilson@example.com')
db_utils.ajouter_utilisateur('Moore', 'Amelia', 'amelia.moore@example.com')
db_utils.ajouter_utilisateur('Jackson', 'Lucas', 'lucas.jackson@example.com')
db_utils.ajouter_utilisateur('Harris', 'Charlotte', 'charlotte.harris@example.com')
db_utils.ajouter_utilisateur('White', 'Benjamin', 'benjamin.white@example.com')
db_utils.ajouter_utilisateur('Thomas', 'Mia', 'mia.thomas@example.com')
db_utils.ajouter_utilisateur('Anderson', 'Elijah', 'elijah.anderson@example.com')
db_utils.ajouter_utilisateur('Clark', 'Ava', 'ava.clark@example.com')
db_utils.ajouter_utilisateur('Robinson', 'Mason', 'mason.robinson@example.com')
db_utils.ajouter_utilisateur('Walker', 'Ethan', 'ethan.walker@example.com')
db_utils.ajouter_utilisateur('Young', 'Harper', 'harper.young@example.com')
db_utils.ajouter_utilisateur('Hall', 'Alexander', 'alexander.hall@example.com')
db_utils.ajouter_utilisateur('Allen', 'Lily', 'lily.allen@example.com')


# Effectuer le tirage
tirage.tirer_au_sort()

# Lister les utilisateurs pour vérifier
# db_utils.lister_utilisateurs()
