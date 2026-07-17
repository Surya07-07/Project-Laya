from core.device.system_info import SystemInfo
from core.device.storage import StorageManager
from core.device.network import NetworkManager


class DeviceManager:

    def __init__(self):

        self.system = SystemInfo()

        self.storage = StorageManager()

        self.network = NetworkManager()

    def summary(self):

        return {

            "system": self.system.info(),

            "network": self.network.info(),

            "drives": self.storage.drives()

        }
