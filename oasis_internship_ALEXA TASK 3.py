import speech_recognition as sr
import pyttsx3
import PyPDF2
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pandas as pd


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def  take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
    
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '') 
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'how are you' in command:
        talk('I am fine')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'book' in command:
        book = open('python programming.pdf', 'rb')
        pdfReader = PyPDF2.PdfReader(book)
        pages = len(pdfReader.pages)
        print(pages)
        speaker = pyttsx3.init()
        for num in range(pages):
             page = pdfReader.pages[num]
             text = page.extract_text()
             speaker.say(text)
             speaker.runAndWait()

    
    elif "read csv" in command:
        

        url = "https://raw.githubusercontent.com/business-science/free_r_tips/master/001_read_multiple_files/data/audi.csv"

        df = pd.read_csv(url)

        print(df)
        talk(df)

   

    else:
        talk('Please say the command again.')
    

while True:
    run_alexa()
