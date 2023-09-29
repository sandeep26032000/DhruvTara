# pip install speechrecognition
# pip install .\PyAudio-0.2.11-cp38-cp38-win32.whl
# pip install pyttsx3 

import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def SpeakText(command):	
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        try:
            
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            SpeakText("Did you say"+text)
            
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio2 = r.listen(source)
            try:
                text2 = r.recognize_google(audio2)
                if text2 == "yes" :
                    print(text2 + " go to object detection")
                elif text2 == "no" :
                    print(text2 + " Speak again")
                    #SpeakText("Speak Again")
                    
                
            
            except:
                print("Sorry could not recognize what you said")


        except:
            print("Sorry could not recognize what you said")


