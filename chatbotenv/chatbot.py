import numpy as np
import speech_recognition as sr
from gtts import gTTS 
# using the Google Text to Speech library to save mp3 files on file system,
# which can be easily played back
import os


''' 
SPEECH RECOGNITION
    Natural Language Processing has a several subfields, 
    this project utilises the speech recognition.

'''

class ChatBot():
    def __init__(self,name):
        print("------- Booting up", name, "-------")
        self.name = name
        self.text = ''

    def speech_to_text(self):
        voice_recogniser = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Listening...")
            audio = voice_recogniser.listen(mic)
        try:
            self.text = voice_recogniser.recognize_google(audio)
            print("me -->  ", self.text)
        except:
            print("me --> ERROR")


    def wake_up(self, text):
        return True if self.name.lower() in text.lower() else False
    
    @staticmethod
    def text_to_speech(text):
        print("AI --> ", text)
        speaker = gTTS(text = text, lang = "en", slow = False)
        speaker.save("res.mp3")
        os.system("afplay res.mp3")
        os.remove("res.mp3")



if __name__ == '__main__':

    ai = ChatBot(name = "Thursday")
    while True:
        ai.speech_to_text()

        res = ""
        # detect wake up call
        if ai.wake_up(ai.text) is True:
            res = "Hello I am Thursday the AI, what can I do for you?"


        ai.text_to_speech(res)
