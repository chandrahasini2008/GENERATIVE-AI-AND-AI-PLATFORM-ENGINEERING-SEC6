
from abc import ABC, abstractmethod
import requests
import time


# Base Provider
class LLMProvider(ABC):

    @abstractmethod
    def generate(self, prompt):
        pass


# Gemini Provider
class GeminiProvider(LLMProvider):

    def __init__(self, api_key):
        from google import genai
        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt):

        try:
            response = self.client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

            return response.text

        except Exception as e:
            return f"Gemini Error: {e}"


# Ollama Provider
class OllamaProvider(LLMProvider):

    def __init__(self, model="llama3.2"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt):

        try:
            response = requests.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=120
            )

            response.raise_for_status()

            return response.json()["response"]

        except requests.exceptions.RequestException as e:
            return f"Ollama Error: {e}"


# Main LLM Client
class LLMClient:

    def __init__(self, provider):
        self.provider = provider

    def generate(self, prompt):
        return self.provider.generate(prompt)
