import sqlparse

FORBIDDEN_KEYWORDS = [
    "INSERT", "UPDATE", "DELETE", "DROP",
    "ALTER", "TRUNCATE", "CREATE", "GRANT"
]

def validate_sql(query: str):
    parsed = sqlparse.parse(query)

    if not parsed:
        return False, "Invalid SQL"

    statement = parsed[0]

    if statement.get_type() != "SELECT":
        return False, "Only SELECT queries are allowed"

    upper_query = query.upper()

    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in upper_query:
            return False, f"Forbidden keyword detected: {keyword}"

    return True, "Valid query"
