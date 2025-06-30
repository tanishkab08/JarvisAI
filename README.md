# 🎙️ Windows Voice Assistant (Jarvis AI)

A simple Windows-based voice assistant built with Python. This assistant can perform tasks like answering questions, telling jokes, reporting the time and date, searching the web, opening applications, and fetching weather updates.

---

## ✨ Features

- 🔊 Speech Recognition
- 🗣️ Text-to-Speech (TTS)
- ⏰ Get Current Time and Date
- 🌐 Web Search
- 🗂️ Open Windows Applications
- 🌦️ Get Weather Information (via OpenWeatherMap API)
- 😂 Tell Random Jokes
- 💻 Simple Command Processing

---

## 🚀 Getting Started

### 📦 Install Required Libraries

Make sure Python 3 is installed. Install the dependencies using:

bash
pip install -r requirements.txt
pip install speechrecognition pyttsx3 requests pyaudio
Note: If pyaudio gives installation errors on Windows, use:
pip install pipwin
pipwin install pyaudio

🔑 Weather API Setup (Optional)
To enable the weather feature:

Go to OpenWeatherMap.

Create a free account and generate an API key.

Open the Python file and replace:
api_key = "YOUR_API_KEY"
with:
api_key = "YOUR_OPENWEATHERMAP_API_KEY"

🏃‍♂️ Run the Assistant
python filename.py

Replace filename.py with your Python script name

🎙️ Voice Commands You Can Try
"Hello" / "Hi" / "Hey" — Greet the assistant

"What time is it?" — Get current time

"What's the date today?" — Get the current date

"Search for Python tutorials" — Search on Google

"Open notepad", "Open calculator" — Open Windows apps

"Tell me a joke" — Hear a joke

"What's the weather?" — Get weather updates (needs API key)

"Help" — Get a list of commands

"Exit" / "Goodbye" / "Stop" — Exit the assistant

📁 Project Structure
├── voice_assistant.py  # Main Python script
├── README.md           # Project readme
├── requirements.txt    # Python dependencies

🛠 Requirements
Python 3.x

Microphone

Windows OS (for app opening commands)

💡 Future Improvements
Add support for sending emails.

Set alarms and reminders.

Add news, quotes, or motivational features.

Cross-platform support (Linux, Mac).

🤝 Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

📜 License
This project is open-source and free to use.

❤️ Acknowledgements
OpenWeatherMap API

SpeechRecognition

pyttsx3

Python

yaml
Copy
Edit

---




