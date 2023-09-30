import pyodbc
import os

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


class ODBC:
    def __init__(self):
        self.cnxn = pyodbc.connect(str_cnxn)
        self.cursor = self.cnxn.cursor()

    def connect(self):
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


def row_to_dict(cursor):
    row = cursor.fetchone()
    if not row:
        return None
    return dict(zip([column[0] for column in cursor.description], row))


def rows_to_list(cursor):
    data = []
    row = row_to_dict(cursor)
    while row:
        data.append(row)
        row = row_to_dict(cursor)
    return data
