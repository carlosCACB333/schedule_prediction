import pyodbc
import os
from utils.tools import row_to_dict, rows_to_list

server = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

str_cnxn = (
    "Driver={ODBC Driver 18 for SQL Server};"
    f"Server={server};"
    f"Database={database};"
    f"UID={username};"
    f"PWD={password};"
    "Trusted_Connection=no;Encrypt=no;TrustServerCertificate=no;Connection Timeout=30;"
)


class Odbc:
    def __init__(self):
        self.cnxn = pyodbc.connect(str_cnxn)
        self.cursor = self.cnxn.cursor()

    def get_connection(self):
        return self.cnxn

    def execute(self, query):
        self.cursor.execute(query)
        return self

    def fetchone(self):
        return row_to_dict(self.cursor)

    def fetchall(self):
        return rows_to_list(self.cursor)

    def close(self):
        self.cursor.close()
        self.cnxn.close()
