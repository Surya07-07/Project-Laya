from core.memory.database import Database
from core.memory.ranker import MemoryRanker
from core.memory.extractor import MemoryExtractor
from core.memory.semantic import SemanticMemory
from core.guardian.guardian import Guardian


class MemoryService:


    def __init__(self):

        self.db = Database()

        self.ranker = MemoryRanker()

        self.extractor = MemoryExtractor()

        self.semantic = SemanticMemory()

        self.guardian = Guardian()



    def remember(self, key, value):

        text = f"{key} {value}"


        # Guardian security check
        security = self.guardian.check_memory(text)


        if not security["allowed"]:

            return {
                "status": "blocked",
                "reason": security["reason"]
            }



        # Decide importance
        decision = self.ranker.rank(text)



        # Save encrypted memory
        self.db.save(

            key,

            value,

            decision["type"].value,

            decision["score"]

        )


        return {

            "status": "saved",

            "key": key,

            "value": value,

            "type": decision["type"].value,

            "score": decision["score"]

        }



    def remember_sentence(self, sentence):


        # Extract memory from sentence

        memory = self.extractor.extract(sentence)


        if memory is None:

            return {

                "status": "ignored",

                "reason": "No memory detected"

            }



        key, value = memory



        return self.remember(

            key,

            value

        )



    def recall(self, key):

        value = self.db.get(key)


        if value is None:

            return None


        return value



    def search(self, question):

        key = self.semantic.find_key(question)


        if key is None:

            return None


        return self.db.get(key)



    def memories(self):

        return self.db.get_all()



    def forget(self, key):

        self.db.delete(key)


        return {

            "status": "deleted",

            "key": key

        }