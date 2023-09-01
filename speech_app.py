import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import webbrowser

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print(f"Sorry, there was an error connecting to Google's servers: {e}")
        return ""

def speak(text):
    tts = gTTS(text=text, lang="en")
    tts.save("output.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.quit()
    os.remove("output.mp3")

def search_wikipedia(query):
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}+site:wikipedia.org"
    webbrowser.open(search_url)

def open_youtube_music():
    webbrowser.open("https://www.youtube.com/watch?v=your_music_video_id")

def search_google(query):
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(search_url)

def main():
    speak("Hello! I'm your speech assistant. How can I assist you today?")
    while True:
        query = listen().lower()
        if "exit" in query:
            speak("Goodbye!")
            break
        elif "wikipedia" in query:
            search_query = query.replace("wikipedia", "").strip()
            search_wikipedia(search_query)
            speak(f"Here is what I found about {search_query} on Wikipedia.")
        elif "play music" in query:
            open_youtube_music()
            speak("Sure, I'm opening YouTube to play music for you.")
        elif "search" in query:
            search_query = query.replace("search", "").strip()
            search_google(search_query)
            speak(f"Here are the search results for {search_query}.")
        else:
            response = "You said: " + query
            speak(response)

if __name__ == "__main__":
    main()
