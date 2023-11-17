import os
from openai import OpenAI

# Set your OpenAI GPT-3 API key
client = OpenAI(api_key=os.environ['TXHpyUizxQUVFWNOJAsWR6QK2JEzEngl79leJoMifNFDpa6D9tgoyeHOWZ7wcve9AQP0Sa5qptVz40c22EWGDFgTpIsRGzZVWP2QQtPCoz9KzMWTVVtqRa3KLDJSjIni'])

# Function to generate a response from GPT-3
def generate_healthwise_response(user_input):
    try:
        prompt = f"User: {user_input}\nChatbot:"
        response = client.ChatCompletion.create(
            model="text-davinci-003",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Start the HealthWiseAI conversation
print("Welcome to HealthWiseAI! How can I assist you with your health today?")

while True:
    user_input = input("User: ")

    if user_input.lower() == 'exit':
        print("HealthWiseAI: Thank you for using HealthWiseAI. Have a healthy day!")
        break

    bot_response = generate_healthwise_response(user_input)
    print("HealthWiseAI:", bot_response)
