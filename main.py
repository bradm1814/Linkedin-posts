import torch
from pipeline.article_pipeline import get_random_article
from posting.post_builder import build_post
from llm.prompt_builder import build_text_prompt, build_image_prompt
from llm.text_generator import LocalLLM
from image_generator.image_generator import FluxImageGenerator



def run_daily():
    article = get_random_article()

    text_prompt = build_text_prompt(article["title"], article["summary"], article["link"])

    image_prompt = build_image_prompt(article["title"], article["summary"]) 

    TextAgent = LocalLLM()
    
    summary = TextAgent.generate(text_prompt)
    print(text_prompt)
    print(image_prompt)

    image_prompt = TextAgent.generate(image_prompt)
    del TextAgent
    torch.cuda.empty_cache()

    print(image_prompt)

    ImageAgent = FluxImageGenerator()

    picture = ImageAgent.generate(image_prompt)

    cleaned_summary = build_post(summary)

    print(cleaned_summary)

if __name__ == "__main__":
    run_daily()