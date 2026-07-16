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

            expires_at TEXT
        )
        """)

        self.connection.commit()

    def save(
        self,
        key,
        value,
        memory_type="permanent",
        importance=5,
        expires_at=None
    ):

        now = datetime.now().isoformat()

        self.cursor.execute("""
        INSERT OR REPLACE INTO memories
        (
            key,
            value,
            memory_type,
            importance,
            created_at,
            last_used,
            expires_at
        )
        VALUES
        (?,?,?,?,?,?,?)
        """,
        (
            key,
            value,
            memory_type,
            importance,
            now,
            now,
            expires_at
        ))

        self.connection.commit()

    def get(self, key):

        self.cursor.execute(
            "SELECT value FROM memories WHERE key=?",
            (key,)
        )

        row = self.cursor.fetchone()

        if row:

            self.cursor.execute(
                """
                UPDATE memories
                SET last_used=?
                WHERE key=?
                """,
                (
                    datetime.now().isoformat(),
                    key
                )
            )

            self.connection.commit()

            return row[0]

        return None

    def all(self):

        self.cursor.execute(
            "SELECT * FROM memories"
        )

        return self.cursor.fetchall()