import sqlite3

conn = sqlite3.connect("memory.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS conversations(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id TEXT,
    query TEXT
)
""")

conn.commit()


def save_conversation(customer_id, query):
    cursor.execute(
        """
        INSERT INTO conversations
        (customer_id, query)
        VALUES (?,?)
        """,
        (customer_id, query)
    )

    conn.commit()


def get_last_issue(customer_id):
    cursor.execute(
        """
        SELECT query
        FROM conversations
        WHERE customer_id=?
        ORDER BY id DESC
        LIMIT 1
        """,
        (customer_id,)
    )

    result = cursor.fetchone()

    if result:
        return result[0]

    return "No previous issue found."