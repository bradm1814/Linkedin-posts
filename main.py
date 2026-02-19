import random
from pipeline.article_pipeline import get_random_article
from summarization.summarizer import build_prompt
from llm.llm import LocalLLM


def run_daily():

    article = get_random_article()

    prompt = build_prompt(article["title"], article["summary"], article["link"])

    Agent = LocalLLM()

    summary = Agent.generate(prompt)

    print(summary)

if __name__ == "__main__":
    run_daily()