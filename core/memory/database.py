import sqlite3
from datetime import datetime

from core.security.encryption import EncryptionManager


class Database:

    def __init__(self):

        self.connection = sqlite3.connect("data/memory.db", check_same_thread=False)

        self.cursor = self.connection.cursor()

        self.encryption = EncryptionManager()

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

    def save(self, key, value, memory_type, importance):

        encrypted_value = self.encryption.encrypt(value)

        existing = self.get(key)

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
                    encrypted_value,
                    memory_type,
                    importance,
                    datetime.now().isoformat(),
                    key,
                ),
            )

        else:

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
                    encrypted_value,
                    memory_type,
                    importance,
                    datetime.now().isoformat(),
                    datetime.now().isoformat(),
                ),
            )

        self.connection.commit()

    def get(self, key):

        self.cursor.execute(
            """
            SELECT value
            FROM memories
            WHERE key=?
            """,
            (key,),
        )

        row = self.cursor.fetchone()

        if row:

            return self.encryption.decrypt(row[0])

        return None

    def get_all(self):

        self.cursor.execute("""
            SELECT
            key,
            value,
            memory_type,
            importance,
            created_at,
            last_used

            FROM memories

            """)

        rows = self.cursor.fetchall()

        result = []

        for row in rows:

            result.append(
                (
                    row[0],
                    self.encryption.decrypt(row[1]),
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                )
            )

        return result

    def delete(self, key):

        self.cursor.execute(
            """
            DELETE FROM memories
            WHERE key=?
            """,
            (key,),
        )

        self.connection.commit()

        return True
