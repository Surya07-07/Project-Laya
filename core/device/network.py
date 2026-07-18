import socket


class NetworkManager:

    def info(self):

        hostname = socket.gethostname()

        try:

            ip = socket.gethostbyname(hostname)
        except Exception:
            ip = "Unknown"

        return {"hostname": hostname, "ip": ip}
