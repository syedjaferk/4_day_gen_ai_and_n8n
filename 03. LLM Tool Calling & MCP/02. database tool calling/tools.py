tools = [
    {
        "type": "function",
        "function": {
            "name": "run_sql_query",
            "description": """
            Run a SQL query on the PostgreSQL database. It's capable of executing all type of select queries.

            """,
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "A SELECT SQL query"}
                },
                "required": ["query"],
            },
        },
    }
]
