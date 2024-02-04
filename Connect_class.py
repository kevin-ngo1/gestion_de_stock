import mysql.connector

class DatabaseConnect():
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "n21217916"
        self.database = "store"
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        print("Connexion")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Deconnexion")

