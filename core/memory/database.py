import sqlite3
from datetime import datetime


class Database:

    def __init__(self):

        self.connection = sqlite3.connect(
            "data/memory.db",
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()


    def initialize(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            key TEXT UNIQUE,

            value TEXT,

            memory_type TEXT,

            importance INTEGER,

            created_at TEXT,

            last_used TEXT,

            expires_at TEXT,

            encrypted INTEGER DEFAULT 0
        )
        """)

        self.connection.commit()


    def save(
        self,
        key,
        value,
        memory_type,
        importance
    ):

        existing = self.get(key)

        now = datetime.now().isoformat()


        if existing is not None:

            self.cursor.execute(
                """
                UPDATE memories
                SET value=?,
                    memory_type=?,
                    importance=?,
                    last_used=?
                WHERE key=?
                """,
                (
                    value,
                    memory_type,
                    importance,
                    now,
                    key
                )
            )

            self.connection.commit()
            return


        self.cursor.execute(
            """
            INSERT INTO memories
            (
                key,
                value,
                memory_type,
                importance,
                created_at,
                last_used
            )

            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                key,
                value,
                memory_type,
                importance,
                now,
                now
            )
        )

        self.connection.commit()



    def get(self, key):

        self.cursor.execute(
            """
            SELECT value
            FROM memories
            WHERE key=?
            """,
            (key,)
        )

        row = self.cursor.fetchone()

        if row:
            return row[0]

        return None



    def get_all(self):

        self.cursor.execute(
            """
            SELECT
            key,
            value,
            memory_type,
            importance,
            created_at,
            last_used

            FROM memories

            ORDER BY importance DESC
            """
        )

        return self.cursor.fetchall()



    def delete(self, key):

        self.cursor.execute(
            """
            DELETE FROM memories
            WHERE key=?
            """,
            (key,)
        )

        self.connection.commit()



    def cleanup_expired(self):

        now = datetime.now().isoformat()

        self.cursor.execute(
            """
            DELETE FROM memories

            WHERE expires_at IS NOT NULL
            AND expires_at < ?
            """,
            (now,)
        )

        self.connection.commit()