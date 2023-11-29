import openai
import getpass
# Initialize OpenAI API
openai.api_key = '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'

def get_user_input(prompt):
    return input(prompt)

def get_ai_response(prompt):
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)
    return response.choices[0].text.strip()

def main():
    print("Welcome to HealthWise!")
    username = getpass.getpass("Please enter your username: ")
    print(f"Hello, {username}!")
    
    while True:
        print("\n1. Talk to the doctor")
        print("2. Exit")
        choice = get_user_input("Choose an option: ")
        
        if choice == '1':
            feeling = get_user_input("How are you feeling today? ")
            symptoms = get_user_input("Can you describe your symptoms? ")
            
            # Concatenate user inputs for AI model
            prompt = f"I am feeling {feeling}. My symptoms are {symptoms}."
            
            # Get AI response
            ai_response = get_ai_response(prompt)
            print(f"AI Diagnosis: {ai_response}")
            
        elif choice == '2':
            print("Thank you for using HealthWise. Goodbye!")
            break

if __name__ == "__main__":
    main()

# While many large language models are open source, not all of them provide free API access. Here are a few that do:

#    Hugging Face: Hugging Face provides a free tier for their API, which includes access to several pre-trained models1.
#    DeepAI: DeepAI offers a free tier for their Text Generation API1.
#    OpenAI: OpenAI provides a pay-as-you-go API for GPT-3, but they do offer free access for research purposes upon request1.

# Please note that while these services offer free tiers, there may be limitations on the number of requests or the amount of compute time available. Always check the specific terms and conditions of each service. Also, remember that using these models responsibly and ethically is crucial, especially when dealing with user data.