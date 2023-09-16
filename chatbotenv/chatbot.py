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
        except sr.UnknownValueError:
            print("me --> No speech detected")
            self.text = ""
        except sr.RequestError as e:
            print(f"me --> Recognition request failed: {str(e)}")
            self.text = ""

    def wake_up(self, text):
        return True if self.name.lower() in text.lower() else False
    
    @staticmethod
    def text_to_speech(text):
        if text:
            print("AI --> ", text)
            speaker = gTTS(text=text, lang="en", slow=False)
            speaker.save("res.mp3")
            os.system("afplay res.mp3")
            os.remove("res.mp3")
        else:
            print("AI --> No text to speak")



if __name__ == '__main__':

    ai = ChatBot(name = "Thursday")
    while True:
        ai.speech_to_text()

        res = "I'm here to assist you. Please say my name to wake me up."
        # detect wake up call
        if ai.wake_up(ai.text):
            res = "Hello I am Thursday the AI, what can I do for you?"


        ai.text_to_speech(res)
