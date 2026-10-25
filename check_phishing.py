import socket
import ssl
from urllib.parse import urlparse

while True:
    url = input("\nEnter website URL (q to quit): ").strip()
    if url.lower() == "q":
        break

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    host = urlparse(url).hostname

    try:
        # 1. Website உண்மையிலேயே இருக்கா?
        socket.gethostbyname(host)

        # 2. Valid HTTPS certificate இருக்கா?
        context = ssl.create_default_context()
        with socket.create_connection((host, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=host):
                pass

        print("✅ This is a CORRECT website. It is SAFE.")
    except Exception:
        print("❌ This is a WRONG website. It is NOT SAFE!")