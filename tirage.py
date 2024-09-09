import sqlite3
import random
from datetime import datetime

def tirer_au_sort():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Récupérer tous les utilisateurs
    cursor.execute("SELECT * FROM users")
    utilisateurs = cursor.fetchall()

    # Récupérer les utilisateurs tirés récemment (par exemple, dans les 4 dernières semaines)
    cursor.execute('''
        SELECT user_id FROM draws
        WHERE date >= date('now', '-28 days')
    ''')
    tires_recentement = cursor.fetchall()
    ids_tires_recentement = [id[0] for id in tires_recentement]

    # Filtrer les utilisateurs pour exclure ceux qui ont été tirés récemment
    utilisateurs_disponibles = [u for u in utilisateurs if u[0] not in ids_tires_recentement]

    # Vérifier qu'il y a assez d'utilisateurs disponibles pour un tirage
    if len(utilisateurs_disponibles) < 4:
        print("Pas assez d'utilisateurs disponibles pour un tirage.")
        return

    # Tirer 4 utilisateurs aléatoires parmi les utilisateurs disponibles
    utilisateurs_tires = random.sample(utilisateurs_disponibles, 4)

    # Enregistrer le tirage dans la table draws
    for utilisateur in utilisateurs_tires:
        user_id = utilisateur[0]
        date_tirage = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        cursor.execute('''
            INSERT INTO draws (user_id, date)
            VALUES (?, ?)
        ''', (user_id, date_tirage))

    conn.commit()

    print("Les utilisateurs suivants ont été tirés au sort :")
    for utilisateur in utilisateurs_tires:
        print(f"- {utilisateur[2]} {utilisateur[1]} (Email : {utilisateur[3]})")

    conn.close()
