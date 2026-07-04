import sqlite3
from pathlib import Path


class Database:
    def __init__(self):
        db_path = Path("data") / "memory.db"

        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def initialize(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE,
            value TEXT
        )
        """)
        self.connection.commit()

    def save(self, key, value):
        self.cursor.execute("""
        INSERT OR REPLACE INTO memories(key, value)
        VALUES(?, ?)
        """, (key, value))
        self.connection.commit()

    def get(self, key):
        self.cursor.execute(
            "SELECT value FROM memories WHERE key=?",
            (key,)
        )

        row = self.cursor.fetchone()

        if row:
            return row[0]

        return None