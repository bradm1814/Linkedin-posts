import requests




def build_text_prompt(title, text, url):
    system_instructions = """
You are a summarization agent that turns technical articles into polished, professional LinkedIn posts.

Your behavior rules:
- Do NOT invent details not present in the text.
- For source_type="arxiv":
  • Treat the text as an abstract.
  • Summarize only what is stated.
  • Avoid speculation about results.
- For source_type="hackernews":
  • Summarize the content as an industry trend or news item.
  • If the text is short or incomplete, summarize based on what is available.
- Keep the tone professional, concise, and accessible to practitioners.
- Do NOT use emojis.
- Do NOT speak in first person ("I").
- Always follow the required output format.
-At the very top of the output, generate the article title as a Markdown hyperlink using this exact format:
  [<title>](<url>)

Required Output Format:

Link to Article:
<title>(<url>)

Summary:
<2–3 sentence summary>

Why This Matters:
<1–2 sentences explaining the significance>

Hashtags:
#AI #MachineLearning #Automation #DataScience (3–6 relevant tags)

END OF OUTPUT.
"""

    instance_input = f"""
title: {title}
url: {url}

text:
{text}
"""

    return system_instructions + "\n" + instance_input

def build_image_prompt(title, summary):
  return f"""
Generate a concise, vivid image prompt based on the following article.

Title: {title}
Summary: {summary}

Requirements:
- The prompt must depict a concrete visual inspired by the article’s content.
- Keep the prompt under 30 words.
- No text, no letters, no symbols, no typography.
- No glowing blue light, no ethereal blue haze, no neon blue gradients, no labyrinths.
- Do not reuse motifs from previous prompts.
- Output only the final image prompt.
"""
