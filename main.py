import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
from googlesearch import search

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say("I am your mk")
engine.say("What can I do for you?")
engine.runAndWait()


def talk(command):
    engine.say(command)
    engine.runAndWait()


def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            commands = listener.recognize_google(voice)
            commands = commands.lower()
            if "mk" in commands:
                command = commands.replace("mk", "")
                print("You:" + command)
    except:
        pass
    return command


def run_mk():
    command = take_command()
    if "play" in command:
        song = command.replace("play", "")
        print("MK: playing " + song)
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime('%I %M %p')
        print("MK : current time is " + time)
        talk("current time is" + time)

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 5)
        print("MK : " + info)
        talk(info)

    elif "search" in command:
        find = command.replace("search ", "")
        results = list(search(find))
        if results:
            info = "https://www.google.com/search?q=" + find
            print("MK : Here are the search results for " + find)
            webbrowser.open_new_tab(info)
            talk("Here are the search results for " + find)

    elif "date" in command:
        print("MK : I have a headache, sorry")
        talk("I have a headache, sorry")

    elif "are you single" in command:
        print("MK : No, I am in relationship with wifi")
        talk("No, I am in relationship with wifi")

    elif "joke" or "jokes" in command:
        joke = pyjokes.get_joke()
        print("MK : " + joke)
        talk(joke)

    else:
        print("MK : Please say the command again")
        talk("Please say the command again")


run_mk()
