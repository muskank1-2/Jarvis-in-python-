import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
    elif "open chatgpt" in command.lower():
        webbrowser.open("https://chatgpt.com")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ",1)[1]
        try:
          link = musiclibrary.music[song]  # Get the song link from the library
          webbrowser.open(link)
        except KeyError:
          speak(f"Sorry, I couldn't find the song {song}. Please try another.")



if __name__ == "__main__":
    speak("Initializing Jack")
    while True:
        r = sr.Recognizer()
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if word.lower() == "jack":
                speak("How may I help you?")
                # Listen for the command
                with sr.Microphone() as source:
                    print("Jack is active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    process_command(command)

        except Exception as e:
            print(f"Error: {e}")
