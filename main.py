

import os
import time
from dotenv import load_dotenv
from google import genai

# Step 1: Load API key from .env
load_dotenv()

# Step 2: Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "Gemini API key not found! "
        "Please check your .env file."
    )

# Step 3: Initialize Gemini client
client = genai.Client(api_key=api_key)

print("Welcome to My First LLM Application!")

# Step 4: Get user input
question = input("\nEnter your question: ")

# Step 5: Make API call with retry
max_retries = 3

for attempt in range(max_retries):
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=question
        )

        # Step 6: Display response
        print("\nLLM Response:")
        print(response.text)
        break

    except Exception as e:
        error = str(e)

        if "503" in error or "UNAVAILABLE" in error:
            if attempt < max_retries - 1:
                wait_time = 10 * (2 ** attempt)

                print(
                    f"\nServer busy. Retrying in "
                    f"{wait_time} seconds..."
                )

                time.sleep(wait_time)
            else:
                print("\nGemini server is still busy.")
                print("Please try again later.")

        else:
            print("\nSomething went wrong:")
            print(e)
            break
