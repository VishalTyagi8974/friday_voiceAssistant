import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import random

eng=pyttsx3.init('sapi5')
voices = eng.getProperty('voices')
eng.setProperty('voice',voices[1].id)

def speak(audio):
    eng.say(audio)
    eng.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>3 and hour<12:
        speak("goodmorning friend")
        speak('i am friday, how may i help you?')

    elif hour>=12 and hour<17:
        speak("goodafternoon friend")
        speak('i am friday, how may i help you?')
    else:
        speak("goodevening friend")
        speak('i am friday, how may i help you?')

def takecommand():
    '''it takes microphone input from user'''
    a=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        a.pause_threshold=1
        a.energy_threshold=300
        audio= a.listen(source)

    try:
        print('recognizing...')
        order=a.recognize_google(audio,language='en-in')
        print(f"you said {order}")

    except Exception as e:
        print(e)
        print("please say it again...")
        return 'nothing'
    return order


if __name__ == '__main__':
    wishme()

    while True:
        ask= takecommand().lower()
        if 'friday' in ask:
            speak("yes my friend?")

            for i in range(3):

                query = takecommand().lower()
                if 'wikipedia' in query:
                    query= query.replace('wikipedia','')
                    results=wikipedia.summary(query,sentences=2)
                    speak('according to wikipedia')
                    print(results)
                    speak(results)
                    break

                elif 'open youtube' in query:
                    webbrowser.open("http://youtube.com")
                    break

                elif "search the web site" in query:
                    urll= query.replace("search the web site ","")
                    webbrowser.open("http://"+urll)

                elif "search on net" in query:
                    query=query.replace("search on net","")
                    webbrowser.open(query)

                elif 'open word' in query:
                    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
                    break

                elif 'open excel' in query:
                    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
                    break

                elif 'open google' in query:
                    os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
                    break

                elif 'music' in query:
                    music_dir="c://songs"
                    songs= os.listdir(music_dir)
                    print(songs)
                    len_of_songs= len(songs)-1
                    random_song= random.randint(0,len_of_songs)
                    os.startfile(os.path.join(music_dir,songs[random_song]))
                    break

                elif 'date' in query:
                    ti= datetime.date.today()
                    speak(f"sir today is {ti}")
                    break

                elif 'time' in query:
                    t=datetime.datetime.now().strftime('%H:%M:%S')
                    speak(f"sir, today is {t}")
                    break

                elif 'open pycharm' in query:
                    filepath=r"C:\Program Files\JetBrains\PyCharm Community Edition 2022.2.3\bin\pycharm64.exe"
                    speak("opening pycharm...")
                    os.startfile(filepath)
                    break

                else:
                    speak("i didn't recognized friend")

        elif 'shutup' or 'shutdown' in ask:
            speak('ok sir, thankyou')
            exit()

        else:
            print(f"you said {ask}")
            continue














            