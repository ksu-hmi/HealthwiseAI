import openai

# Set your OpenAI GPT-3 API key
openai.api_key = 'your -api-key'

# Function to generate a response from GPT-3
def generate_healthwise_response(user_input):
    try:
        prompt = f"User: {user_input}\nChatbot:"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].text.strip()
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
