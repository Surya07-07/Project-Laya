from core.memory.database import Database
from core.memory.ranker import MemoryRanker
from core.memory.extractor import MemoryExtractor
from core.memory.semantic import SemanticMemory

from core.guardian.guardian import Guardian

from core.memory.privacy.permission import MemoryPermission
from core.memory.privacy.audit import MemoryAudit


class MemoryService:

    def __init__(self):

        self.db = Database()

        self.ranker = MemoryRanker()

        self.extractor = MemoryExtractor()

        self.semantic = SemanticMemory()

        self.guardian = Guardian()

        self.permission = MemoryPermission()

        self.audit = MemoryAudit()

    def remember(self, key, value):

        text = f"{key} {value}"

        security = self.guardian.check_memory(text)

        if not security["allowed"]:

            return {
                "status": "blocked",
                "reason": security["reason"]
            }

        approval = self.permission.check(text)

        if approval["status"] == "permission_required":

            return {
                "status": "permission_required",
                "reason": approval["reason"],
                "data": text
            }

        decision = self.ranker.rank(text)

        self.db.save(
            key,
            value,
            decision["type"].value,
            decision["score"]
        )

        self.audit.write(
            "SAVE",
            key
        )

        return {
            "status": "saved",
            "key": key,
            "type": decision["type"].value,
            "score": decision["score"]
        }

    def remember_sentence(self, sentence):

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

    def approve_memory(self):

        pending = self.permission.approve()

        if pending is None:

            return {
                "status": "no_pending_memory"
            }

        self.audit.write(
            "APPROVED",
            pending
        )

        return {
            "status": "approved",
            "memory": pending
        }

    def reject_memory(self):

        self.permission.reject()

        self.audit.write(
            "REJECTED",
            "pending"
        )

        return {
            "status": "rejected"
        }

    def recall(self, key):

        return self.db.get(key)

    def memories(self):

        return self.db.get_all()

    def forget(self, key):

        exists = self.db.get(key)

        if exists is None:

            return {
                "status": "not_found",
                "key": key
            }

        self.db.delete(key)

        self.audit.write(
            "DELETE",
            key
        )

        return {
            "status": "deleted",
            "key": key
        }
