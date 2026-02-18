import random
from ingestion import arxiv_ingestor
from ingestion import hackernews
from ingestion.content_fetcher import fetch_full_article


def run_daily():

    sources = {
        "arx_quant": arxiv_ingestor.get_arxiv_quant(),
        "arx_ai": arxiv_ingestor.get_arxiv_ai(),
        "hackernews": hackernews.get_hackernews_ai()
    }

    random_daily_source = random.choice(list(sources.keys()))

    articles = sources[random_daily_source]

    random_daily_article = random.choice(articles)

    print(random_daily_article)



if __name__ == "__main__":
    run_daily()