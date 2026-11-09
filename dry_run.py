import json
from pathlib import Path
from urllib.parse import urlparse


def main():
    config_path = Path(__file__).with_name("config.json")
    config = json.loads(config_path.read_text(encoding="utf-8"))

    url = config.get("url")
    service = config.get("service")
    if not isinstance(url, str) or not urlparse(url).scheme or not urlparse(url).netloc:
        raise ValueError("config.json must contain a valid URL.")
    if not isinstance(service, str) or not service.strip():
        raise ValueError("config.json must contain a service name.")

    print("Local dry-run only; no network requests or service actions were performed.")
    print(f"Configured service: {service}")
    print(f"Configured target: {url}")
    print(f"Comment ID configured: {'yes' if config.get('comment_id') else 'no'}")
    print("CAPTCHA solving and proxy settings were not used.")


if __name__ == "__main__":
    main()
