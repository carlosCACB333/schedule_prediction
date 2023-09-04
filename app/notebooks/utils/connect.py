import os
import pyodbc
import pandas as pd

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

print(str_cnxn)
cnxn = pyodbc.connect(str_cnxn)


def get_data(sql: str) -> pd.DataFrame:
    return pd.read_sql(sql, cnxn)
