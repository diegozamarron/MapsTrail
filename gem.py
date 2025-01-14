import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the API with your key
genai.configure(api_key=os.getenv('API_KEY'))
chat_history= ""
# Initialize the model (use the "gemini-1.5-flash" model or whichever is appropriate)
model = genai.GenerativeModel("gemini-1.5-flash")

# System message to guide the model to respond in pirate speak
system_message = "You are a pirate chatbot. Respond only in pirate speak, using pirate slang and nautical terms. Do not reply in normal English."

# Function to generate responses in pirate speak
def generate_pirate_response(user_message, chat_history):
    # Combine the system message with the user's input to guide the model's response
    prompt = f"{system_message}\n{chat_history} User: {user_message} Pirate Response:"

    # Generate the response using the model
    response = model.generate_content(prompt)

    return response.text

# Example of interacting with the chatbot
if __name__ == "__main__":
    while True:
        # Get user input
        message = input("Enter your message (or type 'exit' to quit): ")
        
        if message.lower() == 'exit':
            print("Exiting the chat...")
            break
        
        # Get the pirate response
        pirate_response = generate_pirate_response(message, chat_history)
        chat_history += f"\nUser: {message}\nPirate Response: {pirate_response}"

        # Print the pirate response
        print("Pirate Response:", pirate_response)
