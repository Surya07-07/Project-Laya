from core.device.app_database import AppDatabase
from core.device.network import NetworkManager
from core.device.storage import StorageManager
from core.device.system_info import SystemInfo


class DeviceManager:

    def __init__(self):

        self.system = SystemInfo()

        self.storage = StorageManager()

        self.network = NetworkManager()

        self.apps = AppDatabase()

    def initialize(self):

        print("🔍 Scanning Installed Applications...")

        database = self.apps.scan()

        self.apps.save()

        print(f"✅ Indexed {len(database)} applications")

    def summary(self):

        return {
            "system": self.system.info(),
            "network": self.network.info(),
            "drives": self.storage.drives(),
            "applications": len(self.apps.load()),
        }
