# AI Voice Assistant (Level 6) bro
# Features: weather, jokes, open websites and apps, search google, tell time, say hi, listen voice
# Author: Biwash Bhattarai (me)
# Github: https://github.com/BIwashbhatarai

import pyttsx3  # speak out text
import speech_recognition as sr  # listen from mic and get text
import pyjokes  # jokes lol
import webbrowser  # open web pages
from datetime import datetime  # get time now
import requests  # for weather API
import subprocess  # open programs like notepad

api_key = ""  # put ur openweather api key here
USER_NAME = "Biwash"  # my name duh

# some sites i want quick open
site_dict = {
    "youtube": "https://www.youtube.com/",
    "google": "https://www.google.com/",
    "python beginner project": "https://github.com/BIwashbhatarai/python-beginner-projects",
    "python real world project": "https://github.com/BIwashbhatarai/PythonRealWorldProjects",
    "linkedin": "https://www.linkedin.com/in/biwash-bhattarai/"
}

def speechtxt(text):
    # make computer talk text you give
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)  # voice #0 is good
    engine.setProperty("rate", 150)  # speed not too fast
    engine.say(text)
    engine.runAndWait()

def txtspeech():
    # listen mic and convert to text
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # ignore noise a bit
        audio = recognizer.listen(source)
        try:
            print("🧠 Recognizing...")
            return recognizer.recognize_google(audio).lower().strip()
        except sr.UnknownValueError:
            print("❌ I no understand, say again plz")
            return ""
        except sr.RequestError:
            print("⚠️ API not working, try later")
            return ""

def getWeather(city, api_key):
    # get weather from openweather api
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        desc = data['weather'][0]['description']
        return f"The temperature of {city} is {temp} °C and {desc}"
    else:
        return "Weather info not found, sorry."

def greetuser():
    # say good morning, afternoon or evening
    hour = datetime.now().hour
    if 5 <= hour < 12:
        speechtxt(f"Good morning {USER_NAME}")
    elif 12 <= hour < 18:
        speechtxt(f"Good afternoon {USER_NAME}")
    else:
        speechtxt(f"Good evening {USER_NAME}")

def main():
    greetuser()
    while True:
        command = txtspeech()
        if not command:
            continue  # if empty just listen again
        print(f"You said: {command}")

        if "your name" in command:
            speechtxt(f"My name is Jarvis. How i help you, {USER_NAME}?")

        elif "old are you" in command:
            speechtxt("I am AI. I no have age.")

        elif "time" in command:
            time_str = datetime.now().strftime("%I:%M %p")
            speechtxt(f"Now time is {time_str}")

        elif "joke" in command:
            joke = pyjokes.get_joke()
            print(f"Joke: {joke}")
            speechtxt(joke)

        elif "weather" in command:
            # get city if said or default kathmandu
            city = command.split('weather in')[-1].strip() if "weather in" in command else "kathmandu"
            weather_report = getWeather(city, api_key)
            print(weather_report)
            speechtxt(weather_report)

        elif command.startswith("open "):
            opened = False
            for site in site_dict:
                if site in command:
                    speechtxt(f"Opening {site}")
                    webbrowser.open(site_dict[site])
                    opened = True
                    break

            if opened:
                continue  # website opened no need open apps

            # open windows apps if asked
            if "notepad" in command:
                speechtxt("Opening Notepad")
                subprocess.Popen("notepad.exe")
                opened = True
            elif "calculator" in command:
                speechtxt("Opening Calculator")
                subprocess.Popen("calc.exe")
                opened = True
            elif "cmd" in command or "command prompt" in command:
                speechtxt("Opening CMD")
                subprocess.Popen("cmd.exe")
                opened = True
            elif "paint" in command:
                speechtxt("Opening Paint")
                subprocess.Popen("mspaint.exe")
                opened = True

            if not opened:
                speechtxt(f"Sorry {USER_NAME}, i dont know what open.")

        elif command.startswith("search") or "search for " in command or "google" in command:
            if "search for" in command:
                query = command.split("search for", 1)[1]
            elif "search google for" in command:
                query = command.split('search google for', 1)[1]
            elif "search" in command:
                query = command.split("search", 1)[1]
            elif "google" in command:
                query = command.split("google", 1)[1]
            else:
                query = ''

            if query.strip():
                search_url = f"https://www.google.com/search?q={query.strip().replace(' ', '+')}"
                speechtxt(f'Searching google for {query.strip()}')
                webbrowser.open(search_url)
            else:
                speechtxt("What you want me to search?")

        elif "quit" in command or "exit" in command:
            speechtxt(f"Bye {USER_NAME}, see you later.")
            break

        else:
            speechtxt(f"Sorry {USER_NAME}, I no understand that.")

if __name__ == "__main__":
    main()
