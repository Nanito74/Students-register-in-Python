import sqlite3
 
class Repositorio:
    def __init__(self):
        self.bd = sqlite3.connect("db.sqlite")
        self.cursor = self.bd.cursor()

# Importa un módulo para interactuar con SQLite para conectarse con el archivo de BD. Además defino un cursor para recorrer la BD