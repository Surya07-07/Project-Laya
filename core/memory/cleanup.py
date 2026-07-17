import sqlite3



class MemoryCleanup:


    def __init__(self):

        self.connection = sqlite3.connect(
            "data/memory.db",
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()



    def clear_temporary(self):


        self.cursor.execute(

            """
            DELETE FROM memories
            WHERE memory_type='temporary'
            """

        )


        self.connection.commit()


        return True