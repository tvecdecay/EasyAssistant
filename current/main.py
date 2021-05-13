import speech_recognition as lang
from appclasses import *

allDict = getAll()

def listen():
    MListener = lang.Recognizer()
    with lang.Microphone() as mic:
        text = MListener.listen(mic)
        try:
            recognized_text = MListener.recognize_google(text, language="") # Remove language argument if you want your assistant in English.
            print(recognized_text)
        except:
            pass
    try:
        format = allDict[recognized_text.lower()]
        format.start()
    except:
        pass
    return 1
    
while listen(): 
    continue
