import sqlite3
import os

DB_NAME = "datos_generados.db"

class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect(DB_NAME)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                apellido TEXT,
                edad TEXT,
                documento TEXT UNIQUE,
                pais TEXT,
                ciudad TEXT,
                idioma TEXT,
                tipo TEXT
            )
        """)
        self.connection.commit()

    def insert_user(self, user_dict):
        self.cursor.execute("""
            INSERT OR IGNORE INTO usuarios (nombre, apellido, edad, documento, pais, ciudad, idioma, tipo)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user_dict["nombre"],
            user_dict["apellido"],
            user_dict["edad"],
            user_dict["documento"],
            user_dict["pais"],
            user_dict["ciudad"],
            user_dict["idioma"],
            user_dict["tipo"]
        ))
        self.connection.commit()

    def close(self):
        self.connection.close()
    
    def get_all_users(self):
        self.cursor.execute("SELECT * FROM usuarios")
        return self.cursor.fetchall()

