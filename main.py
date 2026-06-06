"""
J.A.R.V.I.S - Just A Rather Very Intelligent System
Main AI Assistant Program
"""

import os
from datetime import datetime

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

# Basic AI response function
def get_response(user_input):
    """Generate a response based on user input"""
    user_input = user_input.lower()
    
    # Simple keyword-based responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! I am J.A.R.V.I.S. How can I assist you today?"
    
    elif "what is your name" in user_input:
        return "I am J.A.R.V.I.S - Just A Rather Very Intelligent System. At your service."
    
    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}"
    
    elif "date" in user_input:
        current_date = datetime.now().strftime("%B %d, %Y")
        return f"Today's date is {current_date}"
    
    elif "help" in user_input:
        return """I can help you with:
        - Greeting (say 'hello')
        - Time and date queries
        - Simple calculations
        - General questions
        
        What would you like to know?"""
    
    else:
        return "I'm still learning. Could you rephrase that or ask me something else?"

# Main function
def main():
    """Main program loop"""
    print("=" * 50)
    print(greet_user())
    print("=" * 50)
    print("\nType 'exit' to quit\n")
    
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
