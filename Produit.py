import mysql.connector
from Connect_class import DatabaseConnect

class Product():
    def __init__(self):
        self.db_connector = DatabaseConnect()
        self.db_connector.connect()

    def add_product(self, name, description, price, quantity, category_id):
        query = f"INSERT INTO product (name, description, price, quantity, id_category) VALUES ('{name}','{description}',{price},'{quantity}','{category_id}')"
        try:
            self.db_connector.cursor.execute(query)
            self.db_connector.connection.commit()
            print("Produit ajouté avec succès.")
        except mysql.connector.Error as err:
            print(f"Erreur lors de l'ajout du produit : {err}")

    def delete_product(self, product_id):
        query = f"DELETE FROM product WHERE id = {product_id}"
        try:
            self.db_connector.cursor.execute(query)
            self.db_connector.connection.commit()
            print("Produit supprimé avec succès.")
        except mysql.connector.Error as err:
            print(f"Erreur lors de la suppression du produit : {err}")

    def update_product(self, product_id, name, description, price, quantity, category_id):
        query = f"UPDATE product SET name='{name}', description='{description}', price={price}, quantity={quantity}, id_category={category_id} WHERE id={product_id}"
        try:
            self.db_connector.cursor.execute(query)
            self.db_connector.connection.commit()
            print("Produit mis à jour avec succès.")
        except mysql.connector.Error as err:
            print(f"Erreur lors de la mise à jour du produit : {err}")

    def get_all_products(self):
        query = "SELECT * FROM product"
        try:
            self.db_connector.cursor.execute(query)
            products = self.db_connector.cursor.fetchall()
            return products
        except mysql.connector.Error as err:
            print(f"Erreur lors de la récupération des produits : {err}")
            return None






    



