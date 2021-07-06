import time
import pyttsx3
import datetime
import os
import cv2
import random
import requests
import wikipedia
import webbrowser
import socket
import pywhatkit as kit
import smtplib  # this module is used to send email to anyone : pip install secure-smptlib
import sys
import pyjokes
import speech_recognition as sr
import docx
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


# text to speech
def speak(audio):  # converts in audio
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# to voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"

    return query


# wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("good afternoon")
    else:
        speak("good evening")
    assname = ("jarvis mohit mudgal sir")
    speak(f"I am your {assname}")
    speak("How can i help you")


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mudgalmohit30@gmail.com', '')
    server.sendmail('2019pietcsnivesh116@poornima.org', to, content)
    server.close()


if __name__ == '__main__':

    # takecommand()
    wish()

    while True:
        # if 1:
        query = takecommand().lower()
        # logic building for task

        if "open notepad" in query:
            speak("opening notepad sir")
            npath = "C:\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
        elif "open chrome" in query:
            speak("opening google chrome")
            gpath = "C:\\Users\\pc\\AppData\\Local\\Google\\chrome\\Application\\chrome.exe"
            os.startfile(gpath)

        elif "open adobe reader" in query:
            speak("opening adobe reader")
            apath = "C:\Program Files (x86)\Adobe\\Reader 10.0\\Reader\\AcroRd32.exe"
            os.startfile(apath)
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "open eclipse" in query:
            speak("opening eclipse")
            lpath = "C:\\Users\\pc\\eclipse\\java-latest-released\\eclipse\\eclipse.exe"
            os.system(lpath)
        elif 'play music' in query or "play song" in query:

            n = random.randint(0,10)
            print(n)
            speak("Here you go with music")
            # music_dir = "E:\\SONGS\\new song"
            music_dir = "E:\\SONGS\\new song"
            song = os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir, song[n]))
        # online task

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            # print(results)
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
            z = takecommand().lower()
            if " fine " in query:
                speak("thats good sir")
            else:
                speak("all will be good sir")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Mohit Mudgal")
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak("jarvis 3.0")
        # ip address and computer name
        elif "hostname" in query:
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            print("your computer name  is :" + hostname)
            print("your ip address is :" + IPAddr)
            speak(f"Your Computer Name is:{hostname}")
            speak(f"Your Computer IP Address is:{IPAddr}")

        elif "open google" in query:
            speak("sir , what should  I serach on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
        elif "send message" in query:
            speak("what msg do you want to send")
            m = takecommand().lower()
            kit.sendwhatmsg("+918302588287", m, 12, 11)
            # there should be gap of 2 minutes to send message
        elif "play videos on youtube" in query:
            speak("tell me song which you want to play")
            sm = takecommand().lower()
            kit.playonyt(sm)  # this function works as a play songs on youtube
        elif "email to nivesh" in query:
            try:
                speak("what should i say")
                content = takecommand().lower()
                to = "niveshsoni9251@gmail.com"
                sendemail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry sir i am not able to send the email")

        elif "just shut up" in query:
            speak("thanks for using me,have a good day")
            sys.exit()
        # to close any application
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")
        elif "close adobe reader" in query:
            speak("okay sir, closing adobe reader")
            os.system("taskkill /f /im AcroRd32.exe")
        elif "close google chrome" in query:
            speak("closing chrome")
            os.system("taskkill /f /im chrome.exe")
        elif "close eclipse" in query:
            speak("closing eclipse")
            os.system("taskkill /f /im eclipse.exe")
        # to set an alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = 'F://songs'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif "shutdown  system" in query:
            os.system("shutdown /s /t 5")
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")
        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "weather" in query:
            api_key = '88525598d371dba3025e6b852e211052'
            speak("tell me the city to know weather!")
            i = takecommand().lower()

            complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + i + "&appid=" + api_key
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()

            # create variables to store and display dataa
            temp_city = ((api_data['main']['temp']) - 273.15)
            weather_desc = api_data['weather'][0]['description']
            hmdt = api_data['main']['humidity']
            wind_spd = api_data['wind']['speed']
            pressure_wind = api_data['main']['pressure']
            print("-------------------------------------------------------------")
            print("-------------------------------------------------------------")
            speak("Current temperature is: {:.2f} deg C".format(temp_city))
            speak(f"Current weather desc is {weather_desc} ")
            speak(f"Current Humidity  is {hmdt}%")
            speak(f"Current wind speed  is {wind_spd} kmph")
            speak(f"current pressure is is {pressure_wind} atm")
        elif "open" in query:
            doc=docx.Document()
            parag=doc.add_paragraph("hello")
            doc.save("mohit.docx")
            os.system("start mohit.docx")

        # speak("----------------------SIR , DO YOU HAVE OTHER WORK-------------------------")
#qwertyucomment