from pprint import pprint
from core.device.device_manager import DeviceManager

device = DeviceManager()

info = device.summary()

print("=" * 60)
print("DEVICE INFORMATION")
print("=" * 60)

pprint(info)
