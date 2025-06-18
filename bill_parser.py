import requests
import os

def parse_bills():
    api_key = os.getenv("CONGRESS_API_KEY")
    url = "https://api.congress.gov/v3/bill?limit=5"
    headers = {"X-Api-Key": api_key}
    res = requests.get(url, headers=headers)
    data = res.json()

    filtered = []
    keywords = ["finance", "economy", "bitcoin", "tax", "inflation", "subsidy", "war", "technology"]
    for item in data.get("bills", []):
        title = item.get("title", "").lower()
        if any(kw in title for kw in keywords):
            filtered.append({
                "title": item.get("title", ""),
                "bill_type": item.get("billType", ""),
                "number": item.get("number", ""),
                "congress": item.get("congress", ""),
                "latest_action": item.get("latestAction", {}).get("text", ""),
                "url": item.get("url", "")
            })
    return filtered
