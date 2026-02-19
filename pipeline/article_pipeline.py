import random
from ingestion import arxiv_ingestor, hackernews

def get_random_article():

    sources = {
        "arx_quant": arxiv_ingestor.get_arxiv_quant(),
        "arx_ai": arxiv_ingestor.get_arxiv_ai(),
        "hackernews": hackernews.get_hackernews_ai()
    }

    random_daily_source = random.choice(list(sources.keys()))

    articles = sources[random_daily_source]

    random_daily_article = random.choice(articles)

    return random_daily_article