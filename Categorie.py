import mysql.connector

class Category():
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def add_category(self, name):
        query = "INSERT INTO category (name) VALUES (%s)"
        values = (name)
        try:
            self.db_connector.cursor.execute(query, values)
            self.db_connector.connection.commit()
            print("Catégorie ajoutée avec succès.")
        except mysql.connector.Error as err:
            print(f"Erreur lors de l'ajout de la catégorie : {err}")

    def delete_category(self, category_id):
        query = "DELETE FROM category WHERE id = %s"
        values = (category_id)
        try:
            self.db_connector.cursor.execute(query, values)
            self.db_connector.connection.commit()
            print("Catégorie supprimée avec succès.")
        except mysql.connector.Error as err:
            print(f"Erreur lors de la suppression de la catégorie : {err}")

    def update_category(self, category_id, name):
        query = "UPDATE category SET name=%s WHERE id=%s"
        values = (name, category_id)
        try:
            self.db_connector.cursor.execute(query, values)
            self.db_connector.connection.commit()
            print("Catégorie mise à jour avec succès.")
        except mysql.connector.Error as err:
            print(f"Erreur lors de la mise à jour de la catégorie : {err}")

