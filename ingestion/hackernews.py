import requests

HN_TOP_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

AI_KEYWORDS = [
    "ai", "machine learning", "ml", "deep learning", "neural", "llm",
    "transformer", "openai", "anthropic", "gpt", "robot", "automation"
]

def get_hackernews_ai(max_items=5):
    try:
        top_ids = requests.get(HN_TOP_URL, timeout=10).json()
    except Exception:
        return []
    
    articles = []

    for story_id in top_ids[:100]:

        try:
            data = requests.get(HN_ITEM_URL.format(story_id), timeout=10).json()
        except Exception:
            continue

        if not data or "title" not in data:
            continue

        title = data["title"].lower()

        if any(keyword in title for keyword in AI_KEYWORDS):
            articles.append({
                "title": data["title"],
                "summary": "",
                "link": data.get("url", "")
            })
        
        if len(articles) >= max_items:
            break
    
    return articles

