import os
import google.generativeai as genai

class TimeAgent:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def get_local_time(self, city: str) -> str:
        prompt = f"What is the current local time in {city}?"
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            # It's good practice to log the exception here
            # print(f"API Error: {e}") 
            return "Error: Could not retrieve time from API."
