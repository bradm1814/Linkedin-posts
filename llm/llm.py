import requests

class LocalLLM:
    def __init__(self, model_name="mistral"):
        self.model_name = model_name
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt):
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False
        }
    
        response = requests.post(self.url, json=payload)
        response.raise_for_status()

        data = response.json()
        return data.get("response", "").strip()
