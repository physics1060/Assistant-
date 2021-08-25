import pyttsx3
import speech_recognition as sr
import os
def input_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
    import time
    time.sleep(2)
    return Query


def Speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
	
Speak("Do you want to shutdown your computer?")
while True:
    command = input_commands()
    if "no" in command:
        Speak("Thank u sir I will not shut down the computer")
        break
    if "ok" in command:
        # Shutting down
        Speak("Good bye boss Shutting the computer")
        os.system("shutdown /s /t 10")
        break
    Speak("Say that again sir")
