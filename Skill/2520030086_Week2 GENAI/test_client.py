
from abc import ABC, abstractmethod
import requests
import time


class LLMProvider(ABC):

    @abstractmethod
    def generate(self, prompt):
        pass


class GeminiProvider(LLMProvider):

    def __init__(self, api_key):
        from google import genai
        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt):

        for attempt in range(3):
            try:
                response = self.client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )

                return response.text

            except Exception as e:
                error = str(e)

                if "503" in error and attempt < 2:
                    print("Gemini server busy. Retrying...")
                    time.sleep(5)

                else:
                    return f"Gemini Error: {error}"


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


class LLMClient:

    def __init__(self, provider):
        self.provider = provider

    def generate(self, prompt):
        return self.provider.generate(prompt)
