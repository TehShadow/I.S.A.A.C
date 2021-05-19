import speech_recognition as sr
from time import ctime, sleep
import webbrowser
import time
from voice import engine
from bot import bot
from admin import admin

r = sr.Recognizer()

def talk(text):
    engine.say(text)
    engine.runAndWait()
    return

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            talk('Sorry, i did not get that')
        except sr.RequestError:
            talk('Sorry, my speech service is down')
        return voice_data


def respond(voice_data):
    if "what is your name" in voice_data:
        talk("My name is Isaac")
    if "what time is it" in voice_data:
        talk(ctime())
    if "search" in voice_data:
        search = record_audio('What do you want to search for?')
        url = f'https://google.com/search?q={search}'
        webbrowser.get().open(url)
        talk(f'Here is what i found for {search}')
    if "find location" in voice_data:
        search = record_audio('What is the location?')
        url = f'https://google.nl/maps/place/{search}/&amp;'
        webbrowser.get().open(url)
        talk(f'Here is the location of {search}')
    if "exit" in voice_data:
        exit()


time.sleep(1)

admin = admin()
bot = bot()



print("How can i help you?")
while(1):
    voice_data = record_audio()
    print("Done")
    print(f'Q: {voice_data}')
    respond(voice_data)
