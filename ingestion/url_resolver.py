import requests

# ingestion/url_resolver.py
import requests

def resolve_url(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    try:
        r = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
        return r.url
    except Exception as e:
        print("URL resolution failed:", e)
        return url