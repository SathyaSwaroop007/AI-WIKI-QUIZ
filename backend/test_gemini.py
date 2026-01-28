import google.generativeai as genai
"""
Utility script to validate LLM connectivity for quiz generation service.
"""
# Configure API
GEMINI_API_KEY = "AIzaSyABCoCTQ4hwd5O8-oWjnZ2j2H02qYa1Xis"
genai.configure(api_key=GEMINI_API_KEY)

print("Testing Gemini API connection...\n")

# List available models
print("Available models:")
try:
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"  - {model.name}")
    print()
except Exception as e:
    print(f"Error listing models: {e}\n")

# Try to generate content with different model names
model_names = [
    'gemini-2.5-flash',
    'gemini-2.0-flash',
    'gemini-flash-latest',
    'gemini-2.5-pro',
    'models/gemini-2.5-flash',
]
print("Testing model initialization:\n")
for model_name in model_names:
    try:
        print(f"Trying {model_name}...", end=" ")
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Say 'Hello, this model works!'")
        print(f" SUCCESS")
        print(f"   Response: {response.text}\n")
        print(f" Use this model name: '{model_name}'\n")
        break
    except Exception as e:
        print(f" FAILED: {str(e)[:100]}\n")
        continue
else:
    print("\n No working model found. Please check your API key.")
    print("\nTry: pip install --upgrade google-generativeai")
