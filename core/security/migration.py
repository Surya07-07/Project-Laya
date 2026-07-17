import sqlite3
from core.security.encryption import EncryptionManager


class MemoryMigration:


    def __init__(self):

        self.db_path = "data/memory.db"

        self.encryption = EncryptionManager()



    def migrate(self):

        connection = sqlite3.connect(
            self.db_path
        )

        cursor = connection.cursor()


        cursor.execute(
            """
            SELECT id,value
            FROM memories
            """
        )


        memories = cursor.fetchall()


        migrated = 0


        for memory_id, value in memories:


            # Skip already encrypted values

            if value.startswith("gAAAA"):

                continue


            encrypted = self.encryption.encrypt(
                value
            )


            cursor.execute(
                """
                UPDATE memories

                SET value=?

                WHERE id=?
                """,
                (
                    encrypted,
                    memory_id
                )
            )


            migrated += 1



        connection.commit()

        connection.close()


        return migrated