from newspaper import Article
from ingestion.url_resolver import resolve_url

def fetch_full_article(url):
    try:
        real_url = resolve_url(url)
        article = Article(real_url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print(f"failed to fetch article: {e}")
        return None