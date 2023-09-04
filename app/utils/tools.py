def format_list(a_list):
    return ",\n".join(map(str, a_list))


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
