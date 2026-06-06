"""
J.A.R.V.I.S - Just A Rather Very Intelligent System
Main AI Assistant Program with ChatGPT Integration
"""

import os
from datetime import datetime
from config import OPENAI_API_KEY

# Try to import OpenAI - install if needed
try:
    from openai import OpenAI
except ImportError:
    print("Installing OpenAI library...")
    os.system("pip install openai")
    from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Simple greeting function
def greet_user():
    """Greet the user based on time of day"""
    hour = datetime.now().hour
    
    if hour < 12:
        greeting = "Good morning, Sir/Madam."
    elif hour < 18:
        greeting = "Good afternoon, Sir/Madam."
    else:
        greeting = "Good evening, Sir/Madam."
    
    return greeting

# ChatGPT response function
def get_response(user_input):
    """Get a response from ChatGPT"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are J.A.R.V.I.S, a helpful and intelligent AI assistant. Be concise and friendly in your responses."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"I encountered an error: {str(e)}"

# Main function
def main():
    """Main program loop"""
    print("=" * 60)
    print(greet_user())
    print("=" * 60)
    print("\nI'm now connected to ChatGPT! Ask me anything!")
    print("Type 'exit' to quit\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() == "exit":
                print("J.A.R.V.I.S: Shutting down. Goodbye, Sir/Madam.")
                break
            
            if not user_input:
                continue
            
            response = get_response(user_input)
            print(f"J.A.R.V.I.S: {response}\n")
        
        except KeyboardInterrupt:
            print("\n\nJ.A.R.V.I.S: Shutting down. Goodbye, Sir/Madam.")
            break

if __name__ == "__main__":
    main()
