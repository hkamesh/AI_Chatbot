import wikipediaapi
import re
import math
import openai

# Initialize Wikipedia and OpenAI
wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='MyChatbot/1.0 (https://example.com/contact; kamesh.h.2023.cse@ritchennai.edu.in)'
)

# OpenAI API Key
openai.api_key = 'YOUR_OPENAI_API_KEY'  # Replace with a valid OpenAI key

def get_response(user_input):
    user_input = user_input.strip().lower()

    # ✅ Handle math calculations
    try:
        if re.match(r'^[0-9+\-*/(). sqrtlogsinco]+$', user_input):
            result = eval(user_input, {"sqrt": math.sqrt, "log": math.log, "sin": math.sin, "cos": math.cos})
            return f"The answer is {result}"
    except Exception:
        pass

    # ✅ Search Wikipedia for general information
    try:
        query = user_input.replace("wikipedia ", "").strip()
        page = wiki.page(query)
        if page.exists():
            return page.summary.split('\n')[0]
    except Exception:
        pass

    # ✅ Handle common questions
    common_answers = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hello! How can I help you today?",
        "what is the capital of france?": "The capital of France is Paris.",
        "who discovered gravity?": "Gravity was discovered by Sir Isaac Newton.",
        "who is elon musk?": "Elon Musk is the CEO of SpaceX and Tesla.",
        "who invented the telephone?": "Alexander Graham Bell invented the telephone.",
        "what is the speed of light?": "The speed of light is approximately 299,792 kilometers per second."
    }
    if user_input in common_answers:
        return common_answers[user_input]

    # ✅ AI Fallback (OpenAI)
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=f"User: {user_input}\nAI:",
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"OpenAI Error: {e}")
        return "AI service is currently unavailable."

    return "I don't know the answer to that. Please try again."

