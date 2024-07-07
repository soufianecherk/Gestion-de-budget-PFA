import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# ID de la ligne à supprimer
id_to_delete = 12  # Remplacez par l'ID réel que vous souhaitez supprimer

# Exécution de la requête DELETE
cursor.execute("DELETE FROM users WHERE id = ?", (id_to_delete,))

# Validation de la suppression en commitant la transaction
conn.commit()

# Fermeture de la connexion
conn.close()