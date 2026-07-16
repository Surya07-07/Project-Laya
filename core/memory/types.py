from enum import Enum


class MemoryType(Enum):
    PERMANENT = "permanent"
    IMPORTANT = "important"
    TEMPORARY = "temporary"
    IGNORE = "ignore"