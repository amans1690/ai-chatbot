from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

def chat_with_openai(user_input):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=user_input
    )

    return response

def start_chatbot():
    print("👋 Welcome! I'm your chatbot. Type 'exit' to end the chat.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye! 👋")
            break
        response = chat_with_openai(user_input)
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    start_chatbot()
