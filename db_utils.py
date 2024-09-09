import sqlite3

def creer_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    
    conn.commit()
    conn.close()

def ajouter_utilisateur(nom, prenom, email):
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO users (nom, prenom, email)
            VALUES (?, ?, ?)
        ''', (nom, prenom, email))

        conn.commit()
        print(f"L'utilisateur {prenom} {nom} a été ajouté avec succès.")
    
    except sqlite3.IntegrityError:
        print(f"L'utilisateur avec l'email {email} existe déjà dans la base.")
    
    finally:
        conn.close()

def lister_utilisateurs():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    utilisateurs = cursor.fetchall()

    for utilisateur in utilisateurs:
        print(utilisateur)

    conn.close()

def creer_table_draws():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Création de la table pour les tirages
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS draws (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    
    conn.commit()
    conn.close()
