"""
SQL Injection Example
This function is the only one you are permitted
to modify for the lab assignment.

Note: if you aren't familiar with str.format, here
is a link to the docs:
https://docs.python.org/3/library/stdtypes.html#str.format
"""


def create_search_query(account_id: int, search_term: str):
    """
    Creation of SQL query with protection against SQL injection.
    :param account_id: int
    :param search_term: str
    :return: tuple (query, parameters)
    """
    q = 'SELECT * FROM trnsaction ' \
        'WHERE trnsaction.account_id = ? ' \
        'AND trnsaction.memo LIKE ?'

    # Ensure parameters are properly passed with wildcard for search term
    params = (account_id, f'%{search_term}%')

    return q, params







