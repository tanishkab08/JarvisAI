import datetime
import webbrowser
import speech_recognition as sr
import pyttsx3
import openai


def say(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1

    try:
        audio = r.listen(source, timeout=5, phrase_time_limit=10)
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not catch that.")
        say("Sorry, I did not catch that.")
    except sr.WaitTimeoutError:
        print("Timed out.")
        say("You were silent too long.")
    return ""

if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am Jarvis AI")
    while True:
      print("Listening...")
      query = takeCommand()
      sites = [["youtube", "https://www.youtube.com"],["wikipedia", "https://www.wikipedia.com"],["google", "https://www.google.com"],["spotify", "https://www.spotify.com"] ]
      for site in sites:
        if f"open {site[0]}" in query.lower():
           say(f"Opening {site[0]} Mam...")
           webbrowser.open(site[1])

      if "the time" in query:
          strfTime = datetime.datetime.now().strftime("%H:%M:%S")
          say(f"Mam the time is {strfTime}")

# Set your OpenAI API key
openai.api_key = "sk-Your-OpenAI-API-Key-Here"  # <-- Replace this

# Function to speak text aloud
def say(text):
    engine.say(text)
    engine.runAndWait()

# Function to ask OpenAI
def ask_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or use "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("Error with OpenAI:", e)
        say("There was an error with OpenAI.")
        return "I'm sorry, something went wrong."

# Main loop
say("Hello! Ask me anything.")
while True:
    query = takeCommand()
    if query:
        if "exit" in query or "quit" in query:
            say("Goodbye!")
            break
        response = ask_openai(query)
        print(f"AI: {response}")
        say(response)



