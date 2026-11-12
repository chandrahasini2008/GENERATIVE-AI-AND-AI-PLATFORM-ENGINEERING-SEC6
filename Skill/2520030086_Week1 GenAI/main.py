
import os
from dotenv import load_dotenv
from google import genai

# Step 1: Load environment variables
load_dotenv()

# Step 2: Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. Check your .env file."
    )

# Step 3: Create Gemini client
client = genai.Client(api_key=api_key)

# Step 4: Ask user for a question
print("Welcome to My First LLM Application!")

question = input("\nEnter your question: ")

# Step 5: Generate AI response
try:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=question
    )

    # Step 6: Display response
    print("\nLLM Response:")
    print(response.text)

except Exception as e:
    print("\nSomething went wrong:")
    print(e)
