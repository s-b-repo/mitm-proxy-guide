from mitmproxy import http
import json

API_KEY = "sk-1234567890abcdef"
TARGET_DOMAIN = "target-api.com"

def request(flow: http.HTTPFlow) -> None:
    # Only work on target domain and HTTPS
    if flow.request.scheme != "https" or TARGET_DOMAIN not in flow.request.host:
        return

    headers = flow.request.headers

    # Add API key to header only if missing
    if "Authorization" not in headers:
        headers["Authorization"] = f"Bearer {API_KEY}"

    # Add API key to JSON body if applicable
    if "application/json" in headers.get("Content-Type", ""):
        try:
            raw = flow.request.get_text()
            # Skip if empty or invalid JSON
            if raw and raw.strip()[0] in ["{", "["]:
                data = json.loads(raw)
                if isinstance(data, dict) and "api_key" not in data:
                    data["api_key"] = API_KEY
                    flow.request.set_text(json.dumps(data))
        except Exception:
            pass  # Skip silently if any issue
