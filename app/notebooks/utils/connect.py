import sys

sys.path.append("/app")
import pandas as pd
from libs.odbc import ODBC


def get_data(sql: str) -> pd.DataFrame:
    cnxn = ODBC().connect()
    return pd.read_sql(sql, cnxn)
