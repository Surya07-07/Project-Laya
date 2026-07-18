import platform
import socket

import psutil


class SystemInfo:

    def info(self):

        vm = psutil.virtual_memory()

        disk = psutil.disk_usage("/")

        boot = psutil.boot_time()

        return {
            "hostname": socket.gethostname(),
            "os": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "cpu_physical": psutil.cpu_count(False),
            "cpu_logical": psutil.cpu_count(True),
            "ram_total_gb": round(vm.total / 1024**3, 2),
            "ram_available_gb": round(vm.available / 1024**3, 2),
            "disk_total_gb": round(disk.total / 1024**3, 2),
            "disk_free_gb": round(disk.free / 1024**3, 2),
            "boot_time": boot,
        }
