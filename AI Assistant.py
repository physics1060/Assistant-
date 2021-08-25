#Project jarvis
import speech_recognition as sr 
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import os

from wikipedia.wikipedia import search

#Text To Speech

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)
newVoiceRate = 140
engine.setProperty('rate',newVoiceRate)

def speak(audio):  #here audio is var which contain text
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("good morning sir i am virtual assistant jarvis")
    elif hour>=12 and hour<18:
        speak("good afternoon sir i am virtual assistant jarvis") 
    else:
        speak("good evening sir i am virtual assistant jarvis")  

#now convert audio to text
# 
def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)
    try:
        print("Recognising.") 
        text = r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:                #For Error handling
        speak("sorry...")
        print("Can't recognize,say properly") 
        return "none"
    return text

#for main function                               
if __name__ == "__main__":
    wishMe()
    while True:
        query = takecom().lower()

        if "wikipedia" in query:
            speak("searching details....Wait")
            query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        elif 'open youtube' in query or "open video online" in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")
        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")  
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")      
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")    
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("opening google")
            
        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")
            
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail") 
            
        elif 'open linkedIn' in query:
            webbrowser.open("https://www.linkedin.com/feed/") 
            speak("opening linkedin")  
             
        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")
        elif 'open outlook' in query:
            webbrowser.open("https://outlook.office.com/mail/inbox")
            speak("opening outlook")   
        elif 'open ebay' in query:
            webbrowser.open("https://www.ebay.com")
            speak("opening ebay")
        elif 'search in chrome' in query:
             speak("What should I search?")
             chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
             search = takecom().lower()
             webbrowser.get(chromepath).open_new_tab(search + ".com")
        elif 'music from pc' in query or "music" in query:
            speak("ok i am playing music")
            music_dir = './music'
            musics = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,musics[0]))
        elif 'video from pc' in query or "video" in query:
            speak("ok i am playing videos")
            video_dir = './video'
            videos = os.listdir(music_dir)
            os.startfile(os.path.join(video_dir,videos[0]))  
        elif 'good bye' in query:
            speak("good bye")
            exit()
        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')
        elif "restart" in query:
            speak("Restarting the system within few second")
            os.system('shutdown /r /t 1') 
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okay ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takecom()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')  
        elif 'make you' in query or 'created you' in query or 'develop you' in query:
            ans_m = " For your information Aadarsha Sir Created me ! He is my creator and only he can destroy me."
            print(ans_m)
            speak(ans_m)
        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Jarvis an A I based computer program but i can help you lot like your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)
        elif "hello" in query or "hello Jarvis" in query:
            hel = "Hello Aadarsha Sir! How May i Help you.."
            print(hel)
            speak(hel)
        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name my self ! Jarvis"  
            print(na_me)
            speak(na_me)
        elif "your feeling" in query:
            print("feeling Very crazy after meeting with you")
            speak("feeling Very crazy after meeting with you") 
        elif query == 'none':
            continue 
        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
            ex_exit = 'I love spending time with you and being assisted by you,but now you are supposed to go!i am very sad..ok goodbye'
            speak(ex_exit)
            exit()
        elif "Set a reminder" in query:
            speak("What should I remind you??")
            data = takecom()
            speak("you said me to remind" + data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()
        else:
            temp = query.replace(' ','+')
            g_url="https://www.google.com/search?q="    
            res_g = 'sorry! i didnt understand but i search from internet to give your answer!Is it okay'
            print(res_g)
            speak(res_g)
            webbrowser.open(g_url+temp)
