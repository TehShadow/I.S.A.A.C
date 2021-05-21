from math import trunc
from sys import float_repr_style
import speech_recognition as sr
from time import ctime, sleep
import webbrowser
import time
from voice import engine
from bot import bot
from admin import admin
import pyautogui
from spotify import *




r = sr.Recognizer()

def talk(text):
    engine.say(text)
    engine.runAndWait()
    return

def gerenal_exists(terms,voice):
    for term in terms:
        if term in voice:
            return True

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def spotify_exists(terms,action):
    for term in terms:
        if term in action:
            return True

def become_active(terms):
    for term in terms:
        if term in bot.name:
            bot.awake()
            return True

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            talk(ask)
        audio = r.listen(source , 5 , 5 )
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            if(voice_data == ''):
                return
            talk('Sorry, i did not get that')
        except sr.RequestError:
            talk('Sorry, my speech service is down')

        # print(f'{voice_data.lower()}')
        return voice_data.lower()


def respond(voice_data):
    try:
            if there_exists(["what is your name","what's your name","tell me your name"]):
                talk(f"My name is {bot.name[0]}")
                return

            if there_exists(["what time is it","time","what's the time"]):
                time = ctime().split(" ")[3].split(":")[0:2]
                if time[0] == "00":
                    hours = '12'
                else:
                    hours = time[0]
                minutes = time[1]
                time = hours + " hours and " + minutes + "minutes"
                talk(time)

                return
            if there_exists(["spotify"]):
                try:
                    action = record_audio("What do you want me to do on spotify sir?")

                    if spotify_exists(["pause" , "stop"] , action):
                        pause_spotify()
                        return
                    if spotify_exists(["start" , "resume"] ,action):
                        Start_Resume()
                        return
                    if spotify_exists(["volume" , "number"], action):
                        number = record_audio("number sir?")
                        number = int(number)
                        volume(number)
                        return
                    if spotify_exists(["skip","next"],action):
                        next()
                        return
                    if spotify_exists(["previous","before"] , action):
                        previous()
                        return
                    if spotify_exists(["shuffle","random"],action):
                        shuffle()
                        return
                    if spotify_exists(["search","find","look"],action):
                        query = record_audio("What should i search for sir?")
                        anwser = record_audio("Is that a track sir?")
                        if gerenal_exists(["yes","i","yea"],anwser):
                            result = search_Spotify(query)
                        else: 
                            result = search_Spotify(query,type="artist")
                        if(result):
                            trackName=result["trackName"]
                            trackURI = result["track"]
                            artistName = result["artistName"]
                            talk(f"I found {trackName} by {artistName}")
                            anwser = record_audio("Shoud i add it to the queue sir?")
                            if gerenal_exists(["yes","i","yea"],anwser):
                                add_to_queue(trackURI)
                        return
                except:
                    talk("Something went wrong with spotify sir ... maybe you should see the console")
            if there_exists(["youtube"]):
                search = record_audio("What do you want me to search for on youtube?")
                url = f"https://www.youtube.com/results?search_query={search}"
                webbrowser.get().open(url)
                talk(f'Here is what i found on youtube about {search}')
            if there_exists(["search","google"]):

                search = record_audio('What do you want to search for sir?')
                url = f'https://google.com/search?q={search}'
                webbrowser.get().open(url)
                talk(f'Here is what i found for {search} on google')
                return

            if there_exists(["find location", "location" , "find" , "area"]):

                search = record_audio('What is the location sir?')
                # print(search)
                url = f'https://google.nl/maps/place/{search}/&amp;'
                webbrowser.get().open(url)
                talk(f'Here is the location of {search} sir')
                return

            if there_exists(["capture","my screen","screenshot"]):

                myScreenshot = pyautogui.screenshot()
                myScreenshot.save(R'C:\Users\Shadow\OneDrive\Desktop\lightshot\screenshot.png')
                talk("took a picture of your screen sir")
                return
                
            if there_exists(["sleep","leave"]):
                talk(f'Going to sleep mode')
                bot.setSleep()

                return
            if there_exists(["exit" ,"quit","shutdown","power off"]):

                bot.quit()
                return
    except:
            if voice_data == None:
                return
            else:
                talk('Something went wrong...can you repeat sir')
    return



admin = admin()
bot = bot()


sleep(1)

talk(f"Welocome back {admin.name}")
while(bot.BotStatus):

    print("listening...")
    startCommand = record_audio()
    if(become_active([startCommand])):

        talk("How can i help you sir?")

        while(bot.isBotawake):
            print("next?")
            voice_data = record_audio()
            print(f'Q: {voice_data}')
            respond(voice_data)

talk("GoodBye sir...")
           