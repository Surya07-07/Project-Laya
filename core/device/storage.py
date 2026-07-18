import psutil


class StorageManager:

    def drives(self):

        drives = []

        for part in psutil.disk_partitions():

            try:

                usage = psutil.disk_usage(part.mountpoint)

            except Exception:

                continue

            drives.append(
                {
                    "device": part.device,
                    "mount": part.mountpoint,
                    "filesystem": part.fstype,
                    "total_gb": round(usage.total / 1024**3, 2),
                    "free_gb": round(usage.free / 1024**3, 2),
                }
            )

        return drives
