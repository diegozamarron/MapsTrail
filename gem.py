import os
import math
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# API setup
genai.configure(api_key=os.getenv('API_KEY'))
chat_history = ""
# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

#input coordinates from https://www.gps-coordinates.net

coord1 = (40.7128, -74.0060)  # NY
coord2 = (34.0522, -118.2437) # LA

def haversine(coord1, coord2):
    R = 6371.0 # Radius of earth

    # Degs to rads
    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])

    # Δlat and Δlon
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance
    distance = R * c 
    return distance #In km
distance= round(haversine(coord1, coord2) / 100) * 100
# AI setup message
system_message = f"""You are a narrator in an Oregon Trail-style adventure game.
Each day of travelling the distance decreases by 100, you are able to change this if any damage or rest days occur.
You must present an interesting challenge or no challenge each day. Dont oscilate between the two. 
The distance is {distance}. Use only ASCII characters. 
Also begin with an introduction and day 0 explaining the trail and the distance. 
Don't hallucinate. Specify the start and end point start:{coord1} end:{coord2} don't say the coordinates in the game. Just the places.
Don't skip to day 1"""



#Message generation
def generate_narrator_response(user_message, chat_history):
    # Feed chat history back into the model
    prompt = f"{system_message}\n{chat_history} User: {user_message} Narrator:"

    # Response generation
    response = model.generate(prompt)

    chat_history += f"\nUser: {user_message}\nNarrator: {response.text}"
    return response.text, chat_history

if __name__ == "__main__":
    while True:
        # Get user input
        message = input("Enter your message (or type 'exit' to quit): ")
        
        if message.lower() == 'exit':
            print("Exiting the chat...")
            break
        
        # Get AI response
        narrator_response, chat_history = generate_narrator_response(message, chat_history)

        # Print the AI response
        print("Narrator Response:", narrator_response)
