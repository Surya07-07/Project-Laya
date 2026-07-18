from dataclasses import dataclass
from datetime import datetime


@dataclass
class Message:
    role: str
    text: str
    timestamp: datetime
