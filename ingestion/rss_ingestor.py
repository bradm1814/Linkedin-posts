import feedparser

def get_ai_news(max_items=5):
    url=("https://news.google.com/rss/search?"
        "q=artificial+intelligence&hl=en-US&gl=US&ceid=US:en")
    
    feed = feedparser.parse(url)
    return [{
        "title": entry.title,
        "summary": entry.get("summary", ""),
        "link": entry.link
    }for entry in feed.entries[:max_items]]

def get_manufacturing_news(max_items=5):
    url=("https://news.google.com/rss/search?"
        "q=manufacturing+automation+OR+industry+4.0+OR+robotics+manufacturing"
        "&hl=en-US&gl=US&ceid=US:en")
    
    feed = feedparser.parse(url)
    return [{
        "title": entry.title,
        "summary": entry.get("summary", ""),
        "link": entry.link
    }for entry in feed.entries[:max_items]]
    
def get_quant_news(max_items=5):
    url=("https://news.google.com/rss/search?"
        "q=quantitative+finance+OR+algorithmic+trading+OR+systematic+trading"
        "&hl=en-US&gl=US&ceid=US:en")
    
    feed = feedparser.parse(url)
    return [{
        "title": entry.title,
        "summary": entry.get("summary", ""),
        "link": entry.link
    }for entry in feed.entries[:max_items]]


