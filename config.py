"""
J.A.R.V.I.S Configuration Settings
Store your API keys and settings here
"""

import os

# AI Assistant Name
AI_NAME = "J.A.R.V.I.S"
AI_FULL_NAME = "Just A Rather Very Intelligent System"

# Greeting settings
FORMAL_MODE = True  # If True, uses formal greetings

# Response settings
DEBUG_MODE = False  # If True, prints debug information

# OpenAI API Key
# ⚠️ IMPORTANT: Replace 'your-api-key-here' with your actual API key from https://platform.openai.com/api/keys
OPENAI_API_KEY = "your-api-key-here"

# You can also load from environment variable:
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-api-key-here")
