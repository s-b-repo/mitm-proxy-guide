from mitmproxy import http
import json

API_TOKEN_KEY = "api_access_token"
API_TOKEN_VALUE = "key"

def request(flow: http.HTTPFlow) -> None:
    # Only proceed if HTTPS
    if flow.request.scheme != "https":
        return

    headers = flow.request.headers

    # 1. Inject token into headers (only if not present)
    if API_TOKEN_KEY not in headers:
        headers[API_TOKEN_KEY] = API_TOKEN_VALUE

    # 2. Inject token into JSON body (only if it's JSON and key is missing)
    content_type = headers.get("Content-Type", "")
    if "application/json" in content_type:
        try:
            body = flow.request.get_text()
            if body and body.strip()[0] in ['{', '[']:
                json_body = json.loads(body)
                if isinstance(json_body, dict) and API_TOKEN_KEY not in json_body:
                    json_body[API_TOKEN_KEY] = API_TOKEN_VALUE
                    flow.request.set_text(json.dumps(json_body))
        except Exception:
            pass  # Silently skip if any issue
