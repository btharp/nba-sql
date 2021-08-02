"""
Misc utilities.
"""


def season_id_to_int(season_id):
    """
    Util to convert a season_id to an int.
    """
    return int(season_id[:4])


def get_rowset_mapping(result_sets, column_names):
    """
    Returns a list of mapped fields to the passed headers.
    """

    headers = result_sets['headers']
    return {column: headers.index(column.upper()) for column in column_names}


def column_names_from_table(db, table_name):
    """
    Gets the column names from a db table.
    """

    columns = db.get_columns(table_name)
    mapped = [column.name for column in columns]

    # season_id is our construct, and isn't returned by any NBA endpoint.
    if 'season_id' in mapped:
        mapped.remove('season_id')

    # Ignore autogenerated id columns.
    if 'id' in mapped:
        mapped.remove('id')

    return mapped

def chunk_list(in_list, n):
    """
    Chunk list into lists of length n.
    """
    return [in_list[i:i + n] for i in range(0, len(in_list), n)]
