import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random
import requests
import json
import subprocess
import threading
import time


class VoiceAssistant:
    def __init__(self):
        # Initialize speech recognition and text-to-speech
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.tts_engine = pyttsx3.init()

        # Configure TTS settings
        self.setup_tts()

        # Adjust for ambient noise
        print("Adjusting for ambient noise... Please wait.")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)

        self.listening = False

    def setup_tts(self):
        """Configure text-to-speech settings"""
        voices = self.tts_engine.getProperty('voices')
        # Try to set a female voice (optional)
        for voice in voices:
            if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
                self.tts_engine.setProperty('voice', voice.id)
                break

        # Set speech rate and volume
        self.tts_engine.setProperty('rate', 180)
        self.tts_engine.setProperty('volume', 0.9)

    def speak(self, text):
        """Convert text to speech"""
        print(f"Assistant: {text}")
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    def listen(self):
        """Listen for voice commands"""
        try:
            with self.microphone as source:
                print("Listening...")
                # Listen for audio with timeout
                audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=5)

            # Recognize speech
            command = self.recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command

        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            self.speak("Sorry, I'm having trouble with speech recognition.")
            return None

    def get_time(self):
        """Get current time"""
        now = datetime.datetime.now()
        time_string = now.strftime("%I:%M %p")
        return f"The current time is {time_string}"

    def get_date(self):
        """Get current date"""
        now = datetime.datetime.now()
        date_string = now.strftime("%A, %B %d, %Y")
        return f"Today is {date_string}"

    def search_web(self, query):
        """Search the web"""
        search_query = query.replace("search for", "").replace("look up", "").strip()
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(url)
        return f"Searching for {search_query}"

    def open_application(self, app_name):
        """Open Windows applications"""
        app_commands = {
            'notepad': 'notepad.exe',
            'calculator': 'calc.exe',
            'paint': 'mspaint.exe',
            'browser': 'msedge.exe',
            'edge': 'msedge.exe',
            'chrome': 'chrome.exe',
            'firefox': 'firefox.exe',
            'file explorer': 'explorer.exe',
            'task manager': 'taskmgr.exe',
            'control panel': 'control.exe',
        }

        app_name = app_name.lower()
        for app, command in app_commands.items():
            if app in app_name:
                try:
                    subprocess.Popen(command)
                    return f"Opening {app}"
                except:
                    return f"Sorry, I couldn't open {app}"

        return "I don't know how to open that application"

    def tell_joke(self):
        """Tell a random joke"""
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why did the math book look so sad? Because it had too many problems!"
        ]
        return random.choice(jokes)

    def get_weather(self, city=""):
        """Get weather information (requires API key)"""

        api_key = "YOUR_API_KEY"

        if not city:
            city = "London"  # Default city

        if api_key == "7efd5e8858654d7b9b925206253006":
            return "Weather feature requires an API key. Please get one from OpenWeatherMap and update the code."

        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url, timeout=5)
            data = response.json()

            if response.status_code == 200:
                temp = data['main']['temp']
                description = data['weather'][0]['description']
                return f"The weather in {city} is {description} with a temperature of {temp} degrees Celsius"
            else:
                return "Sorry, I couldn't get the weather information"
        except:
            return "Sorry, I couldn't connect to the weather service"

    def process_command(self, command):
        """Process voice commands and return appropriate response"""
        if not command:
            return None

        # Greeting commands
        if any(word in command for word in ['hello', 'hi', 'hey']):
            greetings = [
                "Hello! How can I help you today?",
                "Hi there! What can I do for you?",
                "Hey! I'm here to assist you."
            ]
            return random.choice(greetings)

        # Time commands
        elif any(word in command for word in ['time', 'clock']):
            return self.get_time()

        # Date commands
        elif any(word in command for word in ['date', 'today', 'day']):
            return self.get_date()

        # Search commands
        elif any(word in command for word in ['search', 'look up', 'find']):
            return self.search_web(command)

        # Open application commands
        elif 'open' in command:
            app_name = command.replace('open', '').strip()
            return self.open_application(app_name)

        # Weather commands
        elif 'weather' in command:
            return self.get_weather()

        # Joke commands
        elif any(word in command for word in ['joke', 'funny', 'laugh']):
            return self.tell_joke()

        # Exit commands
        elif any(word in command for word in ['exit', 'quit', 'goodbye', 'bye', 'stop']):
            return "Goodbye! Have a great day!"

        # Help commands
        elif 'help' in command:
            return ("I can help you with: telling time and date, searching the web, "
                    "opening applications, telling jokes, and getting weather information. "
                    "Just speak naturally!")

        # Default response for unrecognized commands
        else:
            responses = [
                "I'm not sure how to help with that. Try asking for help to see what I can do.",
                "I didn't understand that command. Say 'help' to see what I can do.",
                "Sorry, I don't know how to do that yet. Ask me for help to see my abilities."
            ]
            return random.choice(responses)

    def start_listening(self):
        """Main listening loop"""
        self.speak("JARVIS activated. Say 'hello' to start or 'exit' to quit.")

        while True:
            command = self.listen()

            if command:
                response = self.process_command(command)

                if response:
                    self.speak(response)

                    # Check for exit command
                    if any(word in command for word in ['exit', 'quit', 'goodbye', 'bye', 'stop']):
                        break

            # Small delay to prevent excessive CPU usage
            time.sleep(0.1)


def main():
    """Main function to start the voice assistant"""
    print("Windows Voice Assistant")
    print("======================")
    print("Make sure you have a microphone connected and working.")
    print("Installing required packages if not already installed...")

    try:
        assistant = VoiceAssistant()
        assistant.start_listening()

    except KeyboardInterrupt:
        print("\nVoice assistant stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("\nMake sure you have installed the required packages:")
        print("pip install speechrecognition pyttsx3 requests pyaudio")


if __name__ == "__main__":
    main()

"""""
Voice Commands you can try:
- "Hello" or "Hi" - Greet the assistant
- "What time is it?" - Get current time
- "What's the date?" - Get current date
- "Search for Python tutorials" - Search the web
- "Open notepad" - Open applications
- "Tell me a joke" - Get a random joke
- "What's the weather?" - Get weather info (needs API key)
- "Help" - Get list of commands
- "Exit" or "Goodbye" - Stop the assistant
"""




