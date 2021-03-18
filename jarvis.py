import pyttsx3 #pip install
import datetime
engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    #Time=datetime.datetime.now().strftime("%H:%M:%S") #for 24 hour clock
    Time=datetime.datetime.now().strftime("%I:%M:%S") #for 12 hour clock
    speak("The current time is")
    speak(Time)

#time_() uncomment this to use time_()

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

#date_() uncomment this to use date_()

def wishme():
    speak("Welcome back Reekraj Roy!!")
    time_()
    date_()

wishme()