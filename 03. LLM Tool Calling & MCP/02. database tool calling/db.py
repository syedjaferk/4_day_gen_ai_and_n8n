import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def execute_query(query: str):
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    try:
        with conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]

        return {
            "columns": columns,
            "rows": rows[:20]
        }

    except Exception as e:
        return {"error": str(e)}

    finally:
        conn.close()
