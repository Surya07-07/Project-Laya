import requests
from core.security.permissions import PermissionManager

pm = PermissionManager()

def secure_get(url):
    if not pm.request_permission("HTTP_GET", url):
        print("Request blocked by user.")
        return None

    try:
        response = requests.get(url, timeout=10)
        return response.text
    except Exception as e:
        return f"Error: {e}"

