import sys
import threading
import tkinter as tk
import speech_recognition
import pyttsx3 as tts
from neuralintents import GenericAssistant
import brixy
import os
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class Assistant:
    def __init__(self):
        self.brixy = brixy
        self.recognizer = speech_recognition.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty('rate', 150)
        self.assistant = GenericAssistant('intents.json', intent_methods={"send_email": self.send_email})
        self.assistant = GenericAssistant('intents.json', intent_methods={"save_user_name": self.save_user_name})
        self.assistant.train_model()
        self.root = tk.Tk()
        self.root.title("Brixy")
        self.label = tk.Label(self.root, text="Assistant", font=("Arial", 20))
        self.label.pack()
        threading.Thread(target=self.run_assistant).start()
        self.root.mainloop()

    def save_user_name(self):
        try:
            with speech_recognition.Microphone as mic:
                program_files = Path("D:\\Program Files (x86)")
                if program_files.is_dir():
                    Dex = Path("D:\\Program Files (x86)\\Dexcorp Softwares Limited")
                    if Dex.is_dir():
                        Brixy = Path("D:\\Program Files (x86)\\Dexcorp Softwares Limited\\Brixy")
                        if Brixy.is_dir():
                            Users = "user_name.txt"
                            self.speaker.say("i do not know your name. plase tell me your name")
                            self.speaker.runAndWait()
                            audio = self.recognizer.listen(mic)
                            user_name = self.recognizer.recognize_google(audio)
                            with open (Brixy.joinpath(Users), 'a') as f:
                                for item in user_name:
                                    f.write(item +'\n')
                                self.speaker.say("I have saved your name in my brain")
                                self.speaker.runAndWait()
                                self.speaker.say("the next time you ask me i will be able to tell your name")
                                self.speaker.runAndWait()
                        else:
                            os.mkdir(Brixy)
                            Users = "user_name.txt"
                            self.speaker.say("you never told me your name before. so I do not know your name.")
                            self.speaker.runAndWait()
                            self.speaker.say("now tell me your name so that i can remember")
                            self.speaker.runAndWait()
                            audio = self.recognizer.listen(mic)
                            user_name = self.recognizer.recognize_google(audio)
                            with open (Brixy.joinpath(Users), 'a') as f:
                                for item in user_name:
                                    f.write(item +'\n')
                                self.speaker.say("I have saved your name in my brain")
                                self.speaker.runAndWait()
                                self.speaker("the next time you ask me i will be telling you , your name")
                                self.speaker.runAndWait()
                    else:
                        os.mkdir(Dex)
                        Brixy = Path("D:\\Program Files (x86)\\Dexcorp Softwares Limited\\Brixy")
                        os.mkdir(Brixy)
                        Users = 'user_name.txt'
                        self.speaker.say("i do not know your name. can you tell me your name so that i can save it in my brain")
                        self.speaker.runAndWait()
                        audio = self.recognizer.listen(mic)
                        user_name = self.recognizer.recognize_google(audio)
                        with open (Brixy.joinpath(Users), 'a') as f:
                            for item in user_name:
                                f.write(item +'\n')
                            self.speaker.say("I have saved your name in my brain")
                            self.speaker.runAndWait()
                            self.speaker.say("the next time you ask me i will be able to tell your name")
                            self.speaker.runAndWait()


                else:
                    os.mkdir(program_files)
                    Dex = Path("D:\\Program Files (x86)\\Dexcorp Softwares Limited")
                    os.mkdir(Dex)
                    Brixy = Path("D:\\Program Files (x86)\\Dexcorp Softwares Limited\\Brixy")
                    os.mkdir(Brixy)
                    Users = 'user_name.txt'
                    self.speaker.say("i do not know your name. plase tell me your name")
                    self.speaker.runAndWait()
                    audio = self.recognizer.listen(mic)
                    user_name = self.recognizer.recognize_google(audio)
                    # user_name = user_name.lower()
                    with open (Brixy.joinpath(Users), 'a') as f:
                        for item in user_name:
                            f.write(item +'\n')
                        self.speaker.say("I have saved your name in my brain")
                        self.speaker.runAndWait()
                        self.speaker.say("the next time you ask me i will be able to tell your name")
                        self.speaker.runAndWait()
        except:
            self.speaker.say("I could not save your name in my brain. there may be some logical error in my programm. please contact my developer")
            self.speaker.runAndWait()
                




    def send_email(self):
        try:
            with speech_recognition.Microphone() as mic:
                self.speaker.say("what is the email address")
                self.speaker.runAndWait()
                audio = self.recognizer.listen(mic)
                to = self.recognizer.recognize_google(audio)
                to = to.lower()
                self.speaker.say("what should i write")
                self.speaker.runAndWait()
                audio = self.recognizer.listen(mic)
                compose = MIMEText(self.recognizer.recognize_google(audio))
                self.brixy.SendEmail(to, compose)
                self.speaker.say("email has been sent")
        except:
            self.speaker.say("sorry i was not able to send this email")
            
            

    def run_assistant(self):
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)
                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()
                    if "brixy" or "hey brixy" or "aye brixy" or "brixyy" or "brixxy" in text:
                        self.label.config(fg="green")
                        audio = self.recognizer.listen(mic)
                        text = self.recognizer.recognize_google(audio)
                        text = text.lower()
                        if text == "stop" or text == "exit" or text == "quit" or text == "bye" or text == "goodbye" or text == "go to sleep" or text == "sleep":
                            self.speaker.say("Goodbye")
                            self.speaker.runAndWait()
                            self.speaker.stop
                            self.root.destroy()
                            sys.exit()
                        else:
                            if text is not None:
                                response = self.assistant.request(text)
                                if response is not None:
                                    self.speaker.say(response)
                                    self.speaker.runAndWait()
                                self.label.config(fg="black")
            except:
                self.label.config(fg="black")
                continue


Assistant()